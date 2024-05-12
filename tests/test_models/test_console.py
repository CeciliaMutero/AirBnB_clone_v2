#!/usr/bin/python3
import unittest
from console import HBNBCommand  # Import your console.py module
from unittest.mock import patch
from io import StringIO
from datetime import datetime


class TestConsoleCreateMethod(unittest.TestCase):
    """Test cases for the do_create method in the console"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_success(self, mock_stdout):
        """Test do_create method with valid arguments"""
        command = HBNBCommand()
        command.onecmd('create BaseModel name="test" my_number=123')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output != "")
        self.assertTrue(len(output.split("-")) == 5)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_missing_class_name(self, mock_stdout):
        """Test do_create method with missing class name"""
        command = HBNBCommand()
        command.onecmd('create')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_invalid_class_name(self, mock_stdout):
        """Test do_create method with invalid class name"""
        command = HBNBCommand()
        command.onecmd('create InvalidClassName')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """Test do_show method"""
        command = HBNBCommand()
        command.onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        command.onecmd('show BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output != "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        """Test do_destroy method"""
        command = HBNBCommand()
        command.onecmd('create BaseModel')
        command.onecmd('destroy BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        """Test do_all method"""
        command = HBNBCommand()
        command.onecmd('create BaseModel')
        command.onecmd('create User')
        command.onecmd('all')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output != "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        """Test do_count method"""
        command = HBNBCommand()
        command.onecmd('create BaseModel')
        command.onecmd('create BaseModel')
        command.onecmd('count BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "2")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        """Test do_update method"""
        command = HBNBCommand()
        command.onecmd('create BaseModel')
        command.onecmd('update BaseModel 1234')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output != "")


if __name__ == "__main__":
    unittest.main()
