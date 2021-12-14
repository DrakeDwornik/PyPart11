import unittest
import grade_book
from datetime import date


class TestPerson(unittest.TestCase):
    def test_update_first_name(self):
        testing_person = grade_book.Person("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_person.update_first_name(4)
        testing_person = grade_book.Person("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        testing_person.update_first_name("Jane")
        self.assertEqual("Jane", testing_person.first_name)

    def test_update_last_name(self):
        testing_person = grade_book.Person("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_person.update_last_name(4)
        testing_person = grade_book.Person("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        testing_person.update_last_name("Doe")
        self.assertEqual("Doe", testing_person.last_name)

    def test_update_dob(self):
        testing_person = grade_book.Person("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_person.update_dob(4)
        testing_person = grade_book.Person("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        testing_person.update_dob((2000, 1, 31))
        self.assertEqual(date(2000, 1, 31), testing_person.dob)

    def test_update_status(self):
        testing_person = grade_book.Person("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_person.update_status(4)
        testing_person.update_status(grade_book.AliveStatus.Deceased)
        self.assertEqual(grade_book.AliveStatus.Deceased, testing_person.alive)


class TestInstructor(unittest.TestCase):
    def test_update_first_name(self):
        testing_instructor = grade_book.Instructor("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_instructor.update_first_name(4)
        testing_instructor = grade_book.Instructor("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        testing_instructor.update_first_name("Jane")
        self.assertEqual("Jane", testing_instructor.first_name)

    def test_update_last_name(self):
        testing_instructor = grade_book.Instructor("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_instructor.update_last_name(4)
        testing_instructor = grade_book.Instructor("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        testing_instructor.update_last_name("Doe")
        self.assertEqual("Doe", testing_instructor.last_name)

    def test_update_dob(self):
        testing_instructor = grade_book.Instructor("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_instructor.update_dob(4)
        testing_instructor = grade_book.Instructor("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        testing_instructor.update_dob((2000, 1, 31))
        self.assertEqual(date(2000, 1, 31), testing_instructor.dob)

    def test_update_status(self):
        testing_instructor = grade_book.Instructor("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_instructor.update_status(4)
        testing_instructor.update_status(grade_book.AliveStatus.Deceased)
        self.assertEqual(grade_book.AliveStatus.Deceased, testing_instructor.alive)
        print(testing_instructor.instructor_id)