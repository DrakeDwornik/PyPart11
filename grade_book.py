from enum import Enum
from datetime import date
import logging
from uuid import uuid4
from typing import Any


class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class CohortType(Enum):
    Java = 0
    Data = 1

class Cohort():
    def __init__(self, cohort_type: CohortType, major_num: int, minor_num: int):
        if type(cohort_type) != CohortType:
            logging.error('Cohort type must be a CohortType')
            raise TypeError
        else:
            self.cohort_type = cohort_type
        # try:
        self.major_num = int(major_num)
        self.minor_num = minor_num

    def __repr__(self) -> str:
        return f"{self.cohort_type.name} {self.major_num}.{self.minor_num}"


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


class Student(Person):
    def __init__(self, first_name: str, last_name: str, dob: tuple, alive: AliveStatus):
        super().__init__(first_name, last_name, dob, alive)
        self.student_id = f"Student_{uuid4()}"


class ZipCodeStudent(Student):
    def __init__(self, first_name: str, last_name: str, dob: tuple, alive: AliveStatus, cohort: str):
        super().__init__(first_name, last_name, dob, alive)
        self.cohort = ""

    def update_cohort(self, cohort):
        if type(cohort) != str:
            logging.error('Cohort must be a string')
            raise TypeError
        else:
            self.cohort = cohort
