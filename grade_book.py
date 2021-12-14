from enum import Enum
from datetime import date
import logging
from uuid import uuid4
from typing import Any


class AliveStatus(Enum):
    Deceased = 0
    Alive = 1


class Person:
    def __init__(self, first_name: str, last_name: str, dob: tuple, alive: AliveStatus):
        self.first_name = ""
        self.last_name = ""
        self.dob = ""
        self.alive = ""
        self.update_first_name(first_name)
        self.update_last_name(last_name)
        self.update_dob(dob)
        self.update_status(alive)

    def update_first_name(self, first_name: str):
        if type(first_name) != str:
            logging.error('Firstname must be a string')
            raise TypeError
        else:
            self.first_name = first_name

    def update_last_name(self, last_name: str):
        if type(last_name) != str:
            logging.error('Lastname must be a string')
            raise TypeError
        else:
            self.last_name = last_name

    def update_dob(self, dob: tuple):
        try:
            self.dob = date(*dob)
        except TypeError:
            logging.error('dob must be a 3-tuple of a date')
            raise TypeError

    def update_status(self, status: AliveStatus):
        if type(status) != AliveStatus:
            logging.error('Status must be of type AliveStatus')
            raise TypeError
        else:
            self.alive = status

class Instructor(Person):
    def __init__(self, first_name: str, last_name: str, dob: tuple, alive: AliveStatus):
        super().__init__(first_name, last_name, dob, alive)
        self.instructor_id = f"Instructor_{uuid4()}"
