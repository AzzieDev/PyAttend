import csv
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

'''
This is my script for CSIT 111 to take attendance.

The File Open dialog at the beginning can be used to select a CSV file
exported from Brightspace's Grades page for the given course.

After a loop of all students in the roster, we repeat once to make sure we
got everyone, and then finally save the list of absent students in a dated file.
'''

# Create a barebones GUI window necessary for the file dialog
root = tk.Tk()
root.withdraw()  # Hide the window

print("Export a CSV file from Brightspace Course --> Grades --> Export --> Export to CSV")
print("Ensure both First Name and Last Name are checked")

# Show a file open dialog to get file for later
file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")], title="Open CSV export from Brightspace's Grades page")
# Lists of students
potentially_absent = []
marked_absent = []

print("Attendance for CSIT 111")
# Read the CSV file exported from Brightspace's Grades page
with open(file_path, mode='r') as file:
	# Create a CSV DictReader object to parse the file
	csv_reader = csv.DictReader(file)

	# Loop through the rows in the CSV file
	for student in csv_reader:
		# Print each name using dictionary lookups
		print("\n" + student.get('First Name') + " " + student.get('Last Name'))
		# Wait for user input on student presence
		presence = input("\nAre they here?\n")
		if presence == "yes" or presence == "present" or presence == "p" or presence == "y":
			print("Welcome to CSIT 111, " + student.get('First Name') + "!\n")
		else:
			potentially_absent.append(student.get('First Name') + ' ' + student.get('Last Name'))
			print("Added " + student.get('First Name') + " to the potentially absent list for later.\n")

print("That's the whole course roster. Now repeating potentially absent students.\n")

# Loop through the list of potentially absent students
for name in potentially_absent:
	print(name)
	presence = input("\nAre they here?\n")
	if presence == "yes" or presence == "present" or presence == "p" or presence == "y":
		print("Welcome to CSIT 111, " + name + "!\n")
	else:
		marked_absent.append(name)
		print("Marked " + name + " as absent.\n")
# Generate a filename for today's absentees
absent_file = "absent-" + datetime.today().strftime('%m-%d-%Y' + ".txt")

# Open the absent file for writing/appending
with open(absent_file, 'a') as file:
	# Append the final absentee list
	print("Absentee list:")
	for name in marked_absent:
		print(name)
		file.write(name + "\n")
