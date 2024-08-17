#!/usr/bin/python3
"""File storage for AirBnB project"""

from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel
from models.state import State
import json
import shlex


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path: Path to the JSON file.
        __objects: Dictionary to store objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects or filtered by class.

        Args:
            cls: Optional class type to filter objects.

        Returns:
            Dictionary of all objects or filtered by class.
        """
        if cls:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        return self.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary.

        Args:
            obj: The object to add.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        my_dict = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = value.pop("__class__")
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects if it exists.

        Args:
            obj: The object to delete.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Reloads the objects from the JSON file."""
        self.reload()
