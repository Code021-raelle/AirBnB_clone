#!/usr/bin/python3
""" Module for TestConsole class"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Class to test HBNBCommand methods"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def capture_stdout(self, command):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(command)
            return f.getvalue().strip()

    def test_help(self):
        help_text = self.capture_stdout("help")
        self.assertTrue("Documented commands" in help_text)

    def test_help_quit(self):
        help_text = self.capture_stdout("help quit")
        self.assertTrue("Quit command" in help_text)

    def test_create(self):
        output = self.capture_stdout("create BaseModel")
        self.assertTrue("- created -" in output)

    def test_show(self):
        output = self.capture_stdout("create BaseModel")
        obj_id = output.split()[-1]
        output = self.capture_stdout(f"show BaseModel {obj_id}")
        self.assertTrue(obj_id in output)

    def test_destroy(self):
        output = self.capture_stdout("create BaseModel")
        obj_id = output.split()[-1]
        output = self.capture_stdout(f"destroy BaseModel {obj_id}")
        self.assertTrue("- deleted -" in output)

    def test_all(self):
        output = self.capture_stdout("all")
        self.assertTrue("BaseModel" in output)

    def test_count(self):
        output = self.capture_stdout("create BaseModel")
        output = self.capture_stdout("create BaseModel")
        count_output = self.capture_stdout("BaseModel.count()")
        self.assertEqual(count_output, "2")

    def test_update(self):
        output = self.capture_stdout("create BaseModel")
        obj_id = output.split()[-1]
        output = self.capture_stdout(f"update BaseModel {obj_id} name 'test_name'")
        self.assertTrue("- updated -" in ouput)

    def test_show_instance_not_found(self):
        output = self.capture_stdout("show BaseModel 12345")
        self.assertEqual(output, "** no instance found **")

    def test_destroy_instance_not_found(self):
        output = self.capture_stdout("destroy BaseModel 12345")
        self.assertEqual(output, "** no instance found **")

    def test_update_invalid_dictionary(self):
        output = self.capture_stdout("create BaseModel")
        obj_id = output.split()[-1]
        output = self.capture_stdout(f"update BaseModel {obj_id} {'invalid_dictionary'}")
        self.assertEqual(output, "** invalid dictionary **")

    def test_update_no_instance_found(self):
        output = self.capture_stdout(f"update BaseModel 12345 {'{'name': 'test_name'}'}")
        self.assertEqual(output, "** no instance found **")

    def test_update_instance_invalid_id(self):
        output = self.capture_stdout("create BaseModel")
        output = self.capture_stdout(f"update BaseModel invalid_id {'{'name': 'test_name'}'}")
        self.assertEqual(output, "** no instance found **")

    def test_update_missing_attributes(self):
        output = self.capture_stdout("create BaseModel")
        obj_id = output.split()[-1]
        output = self.capture_stdout(f"update BaseModel {obj_id}")
        self.assertEqual(output, "** dictionary missing **")

    def test_update_class_missing(self):
        output = self.capture_stdout("update")
        self.assertEqual(output, "** class name missing **")

    def test_invalid_command(self):
        output = self.capture_stdout("invalid_command")
        self.assertEqual(output, "** Unknown syntax: invalid_command")

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_show_with_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue(obj_id in f.getvalue().strip())

    def test_show_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("show BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found")

    def test_create_missing_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClassName")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_with_attributes(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel name='test_name' age=25")
            self.assertTrue("- create -" in f.getvalue().strip())

    def test_destroy_missing_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy InvalidClassName")
            self.assertEqual(f.getvalue().strip(), "*** class doesn't exist **")

    def test_destroy_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_invalid_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_classname(self):
        with patch('sys.stdout',  new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update InvalidClassName")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_invalid_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_dictionary(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** dictionary missing **")

    def test_update_invalid_dictionary(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 12345 {'invalid_dictionary}")
            self.assertEqual(f.getvalue().strip(), "** invalid dictionary **")


if __name__ == '__main__':
    unittest.main()
