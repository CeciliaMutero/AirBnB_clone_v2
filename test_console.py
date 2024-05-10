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

