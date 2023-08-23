#!/usr/bin/python3
"""A unit test module for the console"""

import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from tests import clear_stream


class TestHBNBCommand(unittest.TestCase):
    """ class for testing HBNBCommand"""
    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """tests def create wit filestorage"""
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            cons.onecmd('create City name="Texas"')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            self.assertIn('City.{}'.format(mdl_id), storage.all().keys())
            cons.onecmd('show City {}'.format(mdl_id))
            self.assertIn("'name': 'Texas'", cout.getvalue().strip())
            clear_stream(cout)
            cons.onecmd('create User name="Josh" age=34 height=5.7')
            mdl_id = cout.getvalue().strip()
            self.assertIn('User.{}'.format(mdl_id), storage.all().keys())
            clear_stream(cout)
            cons.onecmd('show User {}'.format(mdl_id))
            self.assertIn("'name': 'Josh'", cout.getvalue().strip())
            self.assertIn("'age': 34", cout.getvalue().strip())
            self.assertIn("'height': 5.7", cout.getvalue().strip())

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_create(self):
        """Tests create command with the dbase storage.
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            with self.assertRaises(sqlalchemy.exc.OperationalError):
                cons.onecmd('create User')
            clear_stream(cout)
            cons.onecmd('create User email="josh@email.com" password="123"')
            mdl_id = cout.getvalue().strip()
            dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = dbc.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(mdl_id))
            result = cursor.fetchone()
            self.assertTrue(result is not None)
            self.assertIn('josh@email.com', result)
            self.assertIn('123', result)
            cursor.close()
            dbc.close()

    
