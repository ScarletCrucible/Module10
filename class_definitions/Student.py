import re # regex library
"""
Leia Decker
lmdecker@dmacc.edu
March 27 2022
"""

class Student:
	"""Student class"""
	def __init__(self, lname, fname, major, gpa=0.0):
		# valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
		reg = "[a-zA-Z-]+"

		# If an argument doesn't match the regex (only alphabetical chars & hyphen), raise error
		if re.fullmatch(reg, lname) is None or re.fullmatch(reg, fname) is None or re.fullmatch(reg, major) is None:
			raise ValueError

		# If gpa is not a float or is not in the range (0-5, based on 5.0 gpa scale)
		if not isinstance(gpa, float) or gpa < 0.0 or gpa > 5.0:
			raise ValueError

		self.last_name = lname
		self.first_name = fname
		self.major = major
		self.gpa = gpa

	def __str__(self):
		return self.last_name + ", " + self.first_name + "; " + self.major + " major with " + str(self.gpa) + " gpa"


# Wasn't sure where instructions wanted main
if __name__ == '__main__':
	stud1 = Student("Smith", "Steven", "Business", 3.4)
	print(str(stud1))

	stud2 = Student("Foland-Hollinger", "Marsha", "Agriculture", 4.2)
	print(str(stud2))