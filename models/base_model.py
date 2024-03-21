#!/usr/bin/python3
"""This contains the base model for the AirBnB Clone Project"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """This is the base model of the AirBnB clone Project"""

    def __init__(self):
        """The __init__ method has the following instance attributes
        Attributes:
            id (str): Assigned with an uuid4 when an instance is created.
            created_at (datetime): Assigned with current datetime when an
                instance is created.
            updated_at (datetime): Assigned with the current datetime when and
            instance is created.
                And it is updated everytime an object is changed.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute 'update_at' with the current
        datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict containing all keys/values of __dict__ of the
        instance"""
        self.created_at = self.created_at.isoformat(timespec='microseconds')
        self.updated_at = self.updated_at.isoformat(timespec='microseconds')
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        return (new_dict)
