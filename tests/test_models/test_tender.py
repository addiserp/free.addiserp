#!/usr/bin/python3
"""
Contains the TestTenderDocs classes
"""

from datetime import datetime
import inspect
import models
from models import tender
from models.base_model import BaseModel
import pep8
import unittest
Tender = tender.Tender


class TestTenderDocs(unittest.TestCase):
    """Tests to check the documentation and style of Tender class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.tender_f = inspect.getmembers(Tender, inspect.isfunction)

    def test_pep8_conformance_tender(self):
        """Test that models/tender.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/tender.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_tender(self):
        """Test that tests/test_models/test_tender.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_tender.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_tender_module_docstring(self):
        """Test for the tender.py module docstring"""
        self.assertIsNot(tender.__doc__, None,
                         "tender.py needs a docstring")
        self.assertTrue(len(tender.__doc__) >= 1,
                        "tender.py needs a docstring")

    def test_tender_class_docstring(self):
        """Test for the Tender class docstring"""
        self.assertIsNot(Tender.__doc__, None,
                         "Tender class needs a docstring")
        self.assertTrue(len(Tender.__doc__) >= 1,
                        "Tender class needs a docstring")

    def test_tender_func_docstrings(self):
        """Test for the presence of docstrings in Tender methods"""
        for func in self.tender_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestTender(unittest.TestCase):
    """Test the Tender class"""
    def test_is_subclass(self):
        """Test that Tender is a subclass of BaseModel"""
        tender = Tender()
        self.assertIsInstance(tender, BaseModel)
        self.assertTrue(hasattr(tender, "id"))
        self.assertTrue(hasattr(tender, "created_at"))
        self.assertTrue(hasattr(tender, "updated_at"))

    def test_name_attr(self):
        """Test that Tender has attribute name, and it's an empty string"""
        tender = Tender()
        self.assertTrue(hasattr(tender, "name"))
        if models.storage_t == 'db':
            self.assertEqual(tender.name, None)
        else:
            self.assertEqual(tender.name, "")

    def test_tender_id_attr(self):
        """
        Test that Tender has attribute tender_id, and it's an empty string
        """
        tender = Tender()
        self.assertTrue(hasattr(tender, "id"))
        if models.storage_t == 'db':
            self.assertEqual(tender.id, None)
        else:
            self.assertEqual(tender.id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        c = Tender()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in c.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = Tender()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "Tender")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        tender = Tender()
        string = "[Tender] ({}) {}".format(tender.id, tender.__dict__)
        self.assertEqual(string, str(tender))
