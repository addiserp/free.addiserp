# Free Tenders AddisERP
![Screenshot](static/images/hero.jpg)
## Introduction

Welcome to Free Tenders AddisERP – Your Seamless Tender Management Platform! This project was born out of a shared passion for simplifying the complex process of finding and applying for tenders. As individuals deeply connected to our community, we aimed to bridge the gap between businesses and opportunities, contributing to the growth of local businesses and empowering aspiring entrepreneurs.

[![Deployed Site](http://web-01.addiserp.tech/about)](http://54.227.128.161/)

This project simplifies the process of finding and applying for tenders. Connect with businesses and discover opportunities effortlessly with our user-friendly platform.

- **Project Blog Article:**
  - [Read our Blog](http://web-01.addiserp.tech/about)

### Team Members

- **Natnael Gedlu:**
  - [LinkedIn](https://www.linkedin.com/in/natnael-gedlu-26a279293/)
  - [GitHub](https://github.com/Natnael-Gedlu)

- **Mikias Gedlu:**
  - [LinkedIn](https://www.linkedin.com/in/mikias-gedlu-53954a1b8/)
  - [GitHub](https://github.com/addiserp)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   git clone https://github.com/addiserp/free.addiserp.git
   
2. Navigate to the project directory:

   cd free-tenders-addiserp

3. Install dependencies:

   pip install -r requirements.txt

4. Run the application:

   python main.py

## Usage

Explore opportunities, connect with businesses, and stay updated on the latest tenders in your area. Visit the live site [here](http://web-01.addiserp.tech/) to experience the platform.

## Related Projects

    https://github.com/addiserp/AirBnB_clone_v4.git

## Licensing

This project is licensed under the MIT License.

## Inspiration and Challenges

Our inspiration came from recognizing the need for a user-friendly solution in the tender management space. We envisioned a platform that not only streamlines the tender application process but also serves as a hub for businesses and entrepreneurs to connect and thrive.

**Technical Challenge:**
The primary technical challenge was creating a robust platform that integrates seamlessly with various databases, ensuring real-time updates on the latest tenders. Achieving an intuitive user interface while handling a large dataset posed challenges that demanded innovative solutions.

## Contributing
We welcome contributions! If you'd like to contribute, please follow our Contribution Guidelines.

## Learnings and Future Iterations

**Technical Learnings:**
The project provided valuable insights into database optimization, front-end development, and collaborative coding practices. We delved into technologies that enhance real-time data processing and user interactions.
## File Descriptions
[freeconsole.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to mysql database) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the database). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the mysql database). 

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [category.py](/models/category.py)
* [biddoc.py](/models/biddoc.py)
* [language.py](/models/language.py)
* [region.py](/models/region.py)
* [tender.py](/models/tender.py)
* [utype.py](/models/utype.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains DB Storage class that handles Databse connections :
[db_storage.py](/models/engine/db_storage.py) - connect to database using sqlalchemy
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the database 
* `def reload(self)` -  deserializes the JSON file to __objects
* `def count(self)` - count each models and their row size

#### `api/v1/ ` Api integration 
[app.py](/api/v1/app.py) - creates API instance
* route('/status) - inform the status of api using index.py file
* route('/biddocs) - retrives form biddocs table and Has GET/POST/PUT/DELETE functions
* route('/category) - retrives form categories table and Has GET/POST/PUT/DELETE functions
* route('/language) - retrives form languages table and Has GET/POST/PUT/DELETE functions
* route('/regions) - retrives form regions table and Has GET/POST/PUT/DELETE functions
* route('/tenders) - retrives form tenders table and Has GET/POST/PUT/DELETE functions
* route('/users) - retrives form users table and Has GET/POST/PUT/DELETE functions
* route('/tender_categories) - Link a Category object to a Tender

#### `static/assets/js/` Jquary functions
* freejs-load.js  - a jquary for loading leftside nav bars menu items(language,region & categories)
* freejs-search.js - a jquary for searching database using API POST method and retrive data and replace main section area in html


#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Set up for the doc tests
* `def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Test for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Test for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods

TestBaseModel class:
* `def test_is_base_model(self)` - Test that the instatiation of a BaseModel works
* `def test_created_at_instantiation(self)` - Test created_at is a pub. instance attribute of type datetime
* `def test_updated_at_instantiation(self)` - Test updated_at is a pub. instance attribute of type datetime
* `def test_diff_datetime_objs(self)` - Test that two BaseModel instances have different datetime objects

[/test_models/test_category.py](/tests/test_models/test_category.py) - Contains the TestcategoryDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_category(self)` - Test that models/category.py conforms to PEP8
* `def test_pep8_conformance_test_category(self)` - Test that tests/test_models/test_category.py conforms to PEP8
* `def test_category_module_docstring(self)` - Test for the category.py module docstring
* `def test_category_class_docstring(self)` - Test for the category class docstring

[/test_models/test_region.py](/tests/test_models/test_region.py) - Contains the TestregionDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_region(self)` - Test that models/region.py conforms to PEP8
* `def test_pep8_conformance_test_region(self)` - Test that tests/test_models/test_region.py conforms to PEP8
* `def test_region_module_docstring(self)` - Test for the region.py module docstring
* `def test_region_class_docstring(self)` - Test for the region class docstring

[/test_models/test_tender.py](/tests/test_models/test_tender.py) - Contains the TesttenderDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_tender(self)` - Test that models/tender.py conforms to PEP8
* `def test_pep8_conformance_test_tender(self)` - Test that tests/test_models/test_tender.py conforms to PEP8
* `def test_tender_module_docstring(self)` - Test for the tender.py module docstring
* `def test_tender_class_docstring(self)` - Test for the tender class docstring

## Examples of use
```
ubuntu@112121-web-01::~/free.addiserp$./freeconsole.py
(free) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(free) all MyModel
** class doesn't exist **
(free) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(free) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(free) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(free) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(free) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(free) quit
```

## Next Iteration:
In the future, we envision incorporating machine learning algorithms to provide personalized recommendations based on user preferences. Enhancements in data security and scalability will be a focus, ensuring the platform can handle increased user engagement.

## Screenshots

![Screenshot](static/images/Screenshot.png)
