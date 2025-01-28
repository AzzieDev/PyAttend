# Standard library
import csv
from datetime import datetime
import os
import tkinter as tk
from tkinter import filedialog

# Local
from student import Student

positive_responses = ["yes", "y", "yea", "p", "here", "present", "okay", "ok", "sure"]

# Show a file open dialog to get file for later
def get_roster_csv():
	# Create a barebones GUI window necessary for the file dialog
	root = tk.Tk()
	root.withdraw()  # Hide the window

	print("Export a CSV file from Brightspace Course --> Grades --> Export --> Export to CSV")
	print("Ensure both First Name and Last Name are checked")

	file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")],
										   title="Open CSV export from Brightspace's Grades page")
	return file_path
#end get_roster_csv

# Parses a roster export and generates a list of Student objects
def generate_list_from_roster(roster_file_path):
	students_from_roster = []
	# Loop through the rows in the CSV file
	try:
		with open(roster_file_path, mode='r') as file:
			# Create a CSV DictReader object to parse the file
			csv_reader = csv.DictReader(file)
			# Process the CSV file exported from Brightspace's Grades page
			for student in csv_reader:
				current_student = Student(student.get('First Name'), student.get('Last Name'))
				students_from_roster.append(current_student)
	except FileNotFoundError:
		print("FileNotFoundError: File not found.")
		quit()
	return students_from_roster
# end generate_list_from_roster

# Takes in a list of students and returns the list of potentially absent ones
def take_attendance(roster_list, repeat=False):
	potentially_absent = []
	# Read the CSV file exported from Brightspace's Grades page
	for student in roster_list:
		# Print each name using dictionary lookups
		print(student.first_name + " " + student.last_name)
		# Wait for user input on student presence
		presence = input("\nAre you here?\n")
		presence = presence.lower()
		if presence in positive_responses:
			print("Welcome to CSIT 111, " + student.first_name + "!\n")
		else:
			potentially_absent.append(student)
			if not repeat:
				print("Added " + student.first_name + " to the potentially absent list for later.\n")
			else:
				print("Marked " + student.first_name + " as absent.\n")
	return potentially_absent
# end take_attendance

# Store the list of absentees to file
def mark_absent(absent_students):
	# Generate a filename for today's absentees
	absent_file = "absent-" + datetime.today().strftime('%m-%d-%Y' + ".txt")

	# Open the absent file for writing/appending
	with open(absent_file, 'a') as file:
		# Append the final absentee list
		print("Absentee list:")
		file.write("Absentee list: \n")
		for name in absent_students:
			print(str(name))
			file.write(str(name) + "\n")
# end mark_absent

# Sequence of attendance:

# Get Roster
roster_file = get_roster_csv()
# Parse the roster into a list of students
print("Attendance from " + os.path.basename(roster_file) + "\n")
list_of_students = generate_list_from_roster(roster_file)
# Take Attendance, making a list of potentially absent students
potentially_absent_students = take_attendance(list_of_students)
# Re-take Attendance, making a list of absent students
print("That's the whole course roster. Now repeating potentially absent students.\n")
definitely_absent_students = take_attendance(potentially_absent_students, True)
# Save the absent students to a file
mark_absent(definitely_absent_students)
