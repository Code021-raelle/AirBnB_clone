#!/usr/bin/python3
""" Module for TestConsole class"""

import unittest
import sys
import io
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Class to test HBNBCommand methods"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def capture_stdout(self, command):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.console.onecmd(command)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()

    def test_help(self):
        output = self.capture_stdout("help")
        self.assertTrue("Documented commands" in output)

    def test_help_quit(self):
        output = self.capture_stdout("help quit")
        self.assertTrue("Quit command" in output)

    def test_create(self):
        output = self.capture_stdout("create BaseModel")
        self.assertTrue("- created -" in output)

    def test_show(self):
        obj_id = "some_object_id"
        output = self.capture_stdout(f"show BaseModel {obj_id}")
        self.assertIn(obj_id, output)

    def test_destroy(self):
        obj_id = "some_object_id"
        output = self.capture_stdout(f"destroy BaseModel {obj_id}")
        self.assertTrue("- deleted -" in output.strip())

    def test_all(self):
        output = self.capture_stdout("all")
        self.assertIn("BaseModel", output)

    def test_count(self):
        output = self.capture_stdout("count BaseModel")
        count_output = output.strip().split()[-1]
        self.assertEqual(count_output, "2")

    def test_update(self):
        output = self.capture_stdout("update BaseModel 12345 {'name': 'updated_name'}")
        self.assertIn("- updated -", output)

    def test_show_instance_not_found(self):
        output = self.capture_stdout("show BaseModel 12345")
        self.assertIn("** no instance found **", output)

    def test_destroy_instance_not_found(self):
        output = self.capture_stdout("destroy BaseModel 12345")
        self.assertEqual(output.strip(), "** no instance found **")

    def test_update_invalid_dictionary(self):
        output = self.capture_stdout("create BaseModel")
        obj_id = output.split()[-1]
        output = self.capture_stdout(
                f"update BaseModel {obj_id} {'invalid_dictionary'}")
        self.assertEqual(output, "** invalid dictionary **")

    def test_update_no_instance_found(self):
        obj_id = "12345"
        output = self.capture_stdout(
                f"update BaseModel {obj_id} {'name': 'test_name'}")
        self.assertEqual(output, "** no instance found **\n")

    def test_update_instance_invalid_id(self):
        output = self.capture_stdout("update BaseModel invalid_id {'name': 'test_name'}")
        self.assertEqual(output.strip(), "** no instance found **")

    def test_update_missing_attributes(self):
        output = self.capture_stdout("update BaseModel")
        self.assertEqual(output.strip(), "** dictionary missing **")

    def test_update_class_missing(self):
        output = self.capture_stdout("update")
        self.assertEqual(output.strip(), "** class name missing **")

    def test_invalid_command(self):
        output = self.capture_stdout("invalid_command").strip()
        self.assertEqual(output, "** Unknown syntax: invalid_command")

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF(self):
        with self.assertRaises(SystemExit):
            with patch('builtins.input', size_effect=EOFError):
                self.console.onecmd("EOF")

    def test_show_with_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue(obj_id in f.getvalue().strip())

    def test_show_invalid_id(self):
        output = self.capture_stdout("show BaseModel 1853dcbe-e5b4-41d6-8a96-2ef547347874")
        self.assertIn("** no instance found **", output)

    def test_create_missing_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_classname(self):
        output = self.capture_stdout("create InvalidClassName")
        self.assertEqual(output.strip(), "** class doesn't exist **")

    def test_create_with_attributes(self):
        output = self.capture_stdout("create BaseModel name='test_name' age=25")
        self.assertTrue("- create -" in output.strip())

    def test_destroy_missing_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_classname(self):
        output = self.capture_stdout("destroy InvalidClassName")
        self.assertEqual(output.strip(), "*** class doesn't exist **")

    def test_destroy_missing_instance_id(self):
        output = self.capture_stdout("destroy BaseModel")
        self.assertEqual(output.strip(), "** instance id missing **")

    def test_destroy_invalid_instance_id(self):
        output = self.capture_stdout("destroy BaseModel 12345")
        self.assertEqual(output.strip(), "** no instance found **")

    def test_update_missing_classname(self):
        with patch('sys.stdout',  new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update InvalidClassName")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_instance_id(self):
        output = self.capture_stdout("update")
        self.assertEqual(output.strip(), "** instance id missing **")

    def test_update_invalid_instance_id(self):
        output = self.capture_stdout("update BaseModel 12345")
        self.assertEqual(output.strip(), "** no instance found **")

    def test_update_missing_dictionary(self):
        output = self.capture_stdout("update BaseModel 12345")
        self.assertEqual(output.strip(), "** dictionary missing **")

    def test_update_invalid_dictionary(self):
        output = self.capture_stdout("update BaseModel 12345 {'invalid_dictionary}")
        self.assertEqual(output.strip(), "** invalid dictionary **")


if __name__ == '__main__':
    unittest.main()
