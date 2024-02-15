#!/usr/bin/python3
"""Command Interpreter module"""

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """Command Interpreter class for AirBnB project"""

    prompt = '(hbnb) '

    def default(self, line):
        """Handle unknown syntax errors"""
        print("*** Unknown syntax: {}".format(line))

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program  gracefully"""
        print("")
        raise SystemExit

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in {"BaseModel", "User", "Place", "State", "City", "Amenity", "Review"}:
            print("** class doesn't exist **")
            return
        if class_name == "User":
            new_user = User()
            new_user.save()
            print(new_user.id)
        elif class_name == "Place":
            new_place = Place()
            new_place.save()
            print(new_place.id)
        elif class_name == "State":
            new_state = State()
            new_state.save()
            print(new_state.id)
        elif class_name == "City":
            new_city = City()
            new_city.save()
            print(new_city.id)
        elif class_name == "Amenity":
            new_amenity = Amenity()
            new_amenity.save()
            print(new_amenity.id)
        elif class_name == "Review":
            new_review = Review()
            new_review.save()
            print(new_review.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** instance id missing **")
            return
        if arg_list[0] not in {"BaseModel", "User", "Place", "State", "City", "Amenity", "Review"}:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        instance_id = arg_list[1]
        obj_key = "{}.{}".format(arg_list[0], instance_id)
        all_objs = storage.all()
        if obj_key in all_objs:
            print(all_objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** instance id missing **")
            return
        if arg_list[0] not in {
            "BaseModel", "User", "Place", "State", "City", "Amenity", "Review"}:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        instance_id = arg_list[1]
        obj_key = "{}.{}".format(arg_list[0], instance_id)
        all_objs = storage.all()
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances"""
        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return
        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in {"BaseModel", "User", "Place", "State", "City", "Amenity", "Review"}:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in storage.all(class_name).values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        arg_list = shlex.split(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        class_name = arg_list[0]
        if class_name[0] not in {
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
        }:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        instance_id = arg_list[1]
        obj_key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        obj = all_objs[obj_key]
        if len(arg_list) < 3:
            print("** dictionary missing **")
            return
        try:
            attr_dict = eval(arg_list[2])
        except SyntaxError:
            print("** invalid dictionary **")
            return
        if not isinstance(attr_dict, dict):
            print("** invalid dictionary **")
            return
        for key, value in attr_dict.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        obj.save()

    def do_count(self, arg):
        """Counts the number of instance of a class"""
        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in {"BaseModel", "User", "Place", "State", "City", "Amenity", "Review"}:
            print("** class doesn't exist **")
            return
        print(len(storage.all(class_name)))

    def do_User_count(self, arg):
        """Counts the number of User instances"""
        count = len([
            obj for obj in storage.all().values()
            if isinstance(obj, User)])
        print(count)

    def do_State_count(self, arg):
        """Counts the number of State instances"""
        count = len([
            obj for obj in storage.all().values()
            if isinstance(obj, State)])
        print(count)

    def do_City_count(self, arg):
        """Counts the number of City instances"""
        count = len([
            obj for obj in storage.all().values()
            if isinstance(obj, City)])
        print(count)

    def do_Place_count(self, arg):
        """Counts the number of Place instances"""
        count = len([
            obj for obj in storage.all().values()
            if isinstance(obj, Place)])
        print(count)

    def do_Amenity_count(self, arg):
        """Counts the number of Amenity instances"""
        count = len([
            obj for obj in storage.all().values()
            if isinstance(obj, Amenity)])
        print(count)

    def do_Review_count(self, arg):
        """Counts the number of Review instances"""
        count = len([
            obj for obj in storage.all().values()
            if isinstance(obj, Review)])
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
