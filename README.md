Django BulkSMS sending.
=======================

## Installation.

   The package is available on the python package manager.
   Install by using pip:

       pip install django-bulksms

## Passing django settings variable.

   To run the anything related to django, simply run the command below,
   passing the settings flag.

        django-admin check --settings=bulksms.settings_test

## Running test.

   To run the tests, run the command below:

        pytest --ds=bulksms.settings_test
