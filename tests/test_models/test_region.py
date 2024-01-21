#!/usr/bin/python3
"""
Contains the TestRegionDocs classes
"""

from datetime import datetime
import inspect
import models
from models import region
from models.base_model import BaseModel
import pep8
import unittest
Region = region.Region


class TestRegionDocs(unittest.TestCase):
    """Tests to check the documentation and style of Region class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.region_f = inspect.getmembers(Region, inspect.isfunction)

    def test_pep8_conformance_region(self):
        """Test that models/region.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/region.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_region(self):
        """Test that tests/test_models/test_region.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_region.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_region_module_docstring(self):
        """Test for the region.py module docstring"""
        self.assertIsNot(region.__doc__, None,
                         "region.py needs a docstring")
        self.assertTrue(len(region.__doc__) >= 1,
                        "region.py needs a docstring")

    def test_region_class_docstring(self):
        """Test for the Region class docstring"""
        self.assertIsNot(region.__doc__, None,
                         "region class needs a docstring")
        self.assertTrue(len(Region.__doc__) >= 1,
                        "region class needs a docstring")

    def test_region_func_docstrings(self):
        """Test for the presence of docstrings in Region methods"""
        for func in self.region_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestRegion(unittest.TestCase):
    """Test the Region class"""
    def test_is_subclass(self):
        """Test that Region is a subclass of BaseModel"""
        region = Region()
        self.assertIsInstance(region, BaseModel)
        self.assertTrue(hasattr(region, "id"))
        self.assertTrue(hasattr(region, "created_at"))
        self.assertTrue(hasattr(region, "updated_at"))

    def test_name_attr(self):
        """Test that Region has attribute name, and it's as an empty string"""
        region = Region()
        self.assertTrue(hasattr(region, "name"))
        if models.storage_t == 'db':
            self.assertEqual(region.name, None)
        else:
            self.assertEqual(region.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        s = Region()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_region" in new_d)
        for attr in s.__dict__:
            if attr != "_sa_instance_region":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = Region()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "Region")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        region = Region()
        string = "[Region] ({}) {}".format(region.id, region.__dict__)
        self.assertEqual(string, str(region))
