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


class TestStudent(unittest.TestCase):
    def test_update_first_name(self):
        testing_student = grade_book.Student("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_student.update_first_name(4)
        testing_student = grade_book.Student("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        testing_student.update_first_name("Jane")
        self.assertEqual("Jane", testing_student.first_name)

    def test_update_last_name(self):
        testing_student = grade_book.Student("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_student.update_last_name(4)
        testing_student = grade_book.Student("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        testing_student.update_last_name("Doe")
        self.assertEqual("Doe", testing_student.last_name)

    def test_update_dob(self):
        testing_student = grade_book.Student("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_student.update_dob(4)
        testing_student = grade_book.Student("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        testing_student.update_dob((2000, 1, 31))
        self.assertEqual(date(2000, 1, 31), testing_student.dob)

    def test_update_status(self):
        testing_student = grade_book.Student("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive)
        with self.assertRaises(TypeError):
            testing_student.update_status(4)
        testing_student.update_status(grade_book.AliveStatus.Deceased)
        self.assertEqual(grade_book.AliveStatus.Deceased, testing_student.alive)
        print(testing_student.student_id)


class TestZipCodeStudent(unittest.TestCase):
    def test_update_first_name(self):
        testing_zcw_student = grade_book.ZipCodeStudent("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive,
                                                        "Data 2.2")
        with self.assertRaises(TypeError):
            testing_zcw_student.update_first_name(4)
        testing_zcw_student = grade_book.ZipCodeStudent("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive,
                                                        "Data 2.2")
        testing_zcw_student.update_first_name("Jane")
        self.assertEqual("Jane", testing_zcw_student.first_name)

    def test_update_last_name(self):
        testing_zcw_student = grade_book.ZipCodeStudent("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive,
                                                        "Data 2.2")
        with self.assertRaises(TypeError):
            testing_zcw_student.update_last_name(4)
        testing_zcw_student = grade_book.ZipCodeStudent("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive,
                                                        "Data 2.2")
        testing_zcw_student.update_last_name("Doe")
        self.assertEqual("Doe", testing_zcw_student.last_name)

    def test_update_dob(self):
        testing_zcw_student = grade_book.ZipCodeStudent("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive,
                                                        "Data 2.2")
        with self.assertRaises(TypeError):
            testing_zcw_student.update_dob(4)
        testing_zcw_student = grade_book.ZipCodeStudent("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive,
                                                        "Data 2.2")
        testing_zcw_student.update_dob((2000, 1, 31))
        self.assertEqual(date(2000, 1, 31), testing_zcw_student.dob)

    def test_update_status(self):
        testing_zcw_student = grade_book.ZipCodeStudent("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive,
                                                        "Data 2.2")
        with self.assertRaises(TypeError):
            testing_zcw_student.update_status(4)
        testing_zcw_student.update_status(grade_book.AliveStatus.Deceased)
        self.assertEqual(grade_book.AliveStatus.Deceased, testing_zcw_student.alive)
        print(testing_zcw_student.student_id)

    def test_update_cohort(self):
        testing_zcw_student = grade_book.ZipCodeStudent("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive,
                                                        "Data 2.2")
        with self.assertRaises(TypeError):
            testing_zcw_student.update_last_name(4)
        testing_zcw_student = grade_book.ZipCodeStudent("John", "Smith", (1900, 12, 15), grade_book.AliveStatus.Alive,
                                                        "Data 2.2")
        testing_zcw_student.update_last_name("Java 1.0")
        self.assertEqual("Java 1.0", testing_zcw_student.cohort)
