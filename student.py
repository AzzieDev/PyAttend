# A Student class to contain a first and last name
class Student:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
	# Print the full name of the student as the object representation
	def __str__(self):
		full_name_representation = self.first_name + " " + self.last_name
		return full_name_representation
