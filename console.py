#!/usr/bin/python3
"""Command Interpreter module"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command Interpreter class for AirBnB project"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program  gracefully"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** {}".format(e))

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            del all_objs[key]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        args = arg.split()
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objects.values()
            if type(obj).__name__ == args[0]])



    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** dictionary missing **")
            return
        try:
            dictionary = eval(" ".join(args[2:]))
        except ValueError as e:
            print("** invalid dictionary **")
            return
        obj = all_objs[key]
        for k, v in dictionary.items():
            if hasattr(obj, k):
                v = type(getattr(obj, k))(v)
            setattr(obj, k, v)
        obj.save()

    def do_User_count(self, arg):
        """Counts the number of User instances"""
        count = len([obj for obj in storage.all().values()
            if isinstance(obj, User)])
        print(count)


    def do_State_count(self, arg):
        """Counts the number of State instances"""
        count = len([obj for obj in storage.all().values()
            if isinstance(obj, State)])
        print(count)


    def do_City_count(self, arg):
        """Counts the number of City instances"""
        count = len([obj for obj in storage.all().values()
            if isinstance(obj, City)])
        print(count)


    def do_Place_count(self, arg):
        """Counts the number of Place instances"""
        count = len([obj for obj in storage.all().values()
            if isinstance(obj, Place)])
        print(count)


    def do_Amenity_count(self, arg):
        """Counts the number of Amenity instances"""
        count = len([obj for obj in storage.all().values()
            if isinstance(obj, Amenity)])
        print(count)


    def do_Review_count(self, arg):
        """Counts the number of Review instances"""
        count = len([obj for obj in storage.all().values()
            if isinstance(obj, Review)])
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
