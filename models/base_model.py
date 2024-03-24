#!/usr/bin/python3
"""This contains the base model for the AirBnB Clone Project"""
from datetime import datetime
from uuid import uuid4
from . import storage


class BaseModel:
    """This is the base model of the AirBnB clone Project"""

    def __init__(self, *args, **kwargs):
        """The __init__ method has the following instance attributes
        Attributes:
            id (str): Assigned with an uuid4 when an instance is created.
            created_at (datetime): Assigned with current datetime when an
                instance is created.
            updated_at (datetime): Assigned with the current datetime when and
            instance is created.
                And it is updated everytime an object is changed.
            kwargs (dict): Keyword attributes.
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if (key == 'created_at' or key == 'updated_at' and
                    isinstance(value, str)):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        storage.new(self)

    def __str__(self):
        """Returns [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute 'update_at' with the current
        datetime"""
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Generates and returns a dictionary representation of an instance
        method"""
        new_dict = {}
        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                v = v.isoformat(timespec='microseconds')
            new_dict[k] = v
        new_dict['__class__'] = self.__class__.__name__
        # self.created_at = self.created_at.isoformat(timespec='microseconds')
        # self.updated_at = self.updated_at.isoformat(timespec='microseconds')
        # new_dict = {**self.__dict__}
        # new_dict["__class__"] = self.__class__.__name__
        return (new_dict)
