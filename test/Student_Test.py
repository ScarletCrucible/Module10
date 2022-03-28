import unittest
import unittest as test
from class_definitions import Student as stud_obj
"""
Leia Decker
lmdecker@dmacc.edu
March 27 2022
"""


class StudentTesting(unittest.TestCase):
	def setUp(self):
		self.student = stud_obj("Doe", "John", "CIS", 4.0)

	def tearDown(self):
		del self.student

	def test_object_created_required_attributes(self):
		self.assertEqual(self.student.first_name, "John")
		self.assertEqual(self.student.last_name, "Doe")
		self.assertEqual(self.student.major, "CIS")

	def test_object_created_all_attributes(self):
		self.assertEqual(self.student.first_name, "John")
		self.assertEqual(self.student.last_name, "Doe")
		self.assertEqual(self.student.major, "CIS")
		self.assertEqual(self.student.gpa, 4.0)

	def test_student_str(self):
		self.assertEqual(str(self.student), "Doe, John; CIS major with 4.0 gpa")

	def test_object_not_created_error_last_name(self):
		with self.assertRaises(ValueError):
			stud = stud_obj("Doe1", "John", "CIS")

	def test_object_not_created_error_first_name(self):
		with self.assertRaises(ValueError):
			stud = stud_obj("Doe", "John1", "CIS")

	def test_object_not_created_error_major(self):
		with self.assertRaises(ValueError):
			stud = stud_obj("Doe", "John", "CIS1")

	def test_object_not_created_error_gpa(self):
		# Out of range
		with self.assertRaises(ValueError):
			stud = stud_obj("Doe", "John", "CIS", -0.1)

		with self.assertRaises(ValueError):
			stud = stud_obj("Doe", "John", "CIS", 5.1)

		# Not a float
		with self.assertRaises(ValueError):
			stud = stud_obj("Doe", "John", "CIS", 3)