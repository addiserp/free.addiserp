#!/usr/bin/python3
"""
Contains the TestBiddocDocs classes
"""

from datetime import datetime
import inspect
import models
from models import biddoc
from models.base_model import BaseModel
import pep8
import unittest
Biddoc = biddoc.Biddoc


class TestBiddocDocs(unittest.TestCase):
    """Tests to check the documentation and style of Biddoc class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.biddoc_f = inspect.getmembers(Biddoc, inspect.isfunction)

    def test_pep8_conformance_biddoc(self):
        """Test that models/biddoc.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/biddoc.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_biddoc(self):
        """Test that tests/test_models/test_biddoc.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_biddoc.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_biddoc_module_docstring(self):
        """Test for the biddoc.py module docstring"""
        self.assertIsNot(biddoc.__doc__, None,
                         "biddoc.py needs a docstring")
        self.assertTrue(len(biddoc.__doc__) >= 1,
                        "biddoc.py needs a docstring")

    def test_biddoc_class_docstring(self):
        """Test for the Biddoc class docstring"""
        self.assertIsNot(Biddoc.__doc__, None,
                         "Biddoc class needs a docstring")
        self.assertTrue(len(Biddoc.__doc__) >= 1,
                        "Biddoc class needs a docstring")

    def test_biddoc_func_docstrings(self):
        """Test for the presence of docstrings in Biddoc methods"""
        for func in self.biddoc_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestBiddoc(unittest.TestCase):
    """Test the Biddoc class"""
    def test_is_subclass(self):
        """Test that Biddoc is a subclass of BaseModel"""
        biddoc = Biddoc()
        self.assertIsInstance(biddoc, BaseModel)
        self.assertTrue(hasattr(biddoc, "id"))
        self.assertTrue(hasattr(biddoc, "created_at"))
        self.assertTrue(hasattr(biddoc, "updated_at"))

    def test_name_attr(self):
        """Test that Biddoc has attribute name, and it's as an empty string"""
        biddoc = Biddoc()
        self.assertTrue(hasattr(biddoc, "name"))
        if models.storage_t == 'db':
            self.assertEqual(biddoc.name, None)
        else:
            self.assertEqual(biddoc.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        am = Biddoc()
        # print(am.__dict__)
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Biddoc()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Biddoc")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        biddoc = Biddoc()
        string = "[Biddoc] ({}) {}".format(biddoc.id, biddoc.__dict__)
        self.assertEqual(string, str(biddoc))
