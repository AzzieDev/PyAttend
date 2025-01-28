import csv
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
import os
 
'''
Original File by David Katz...

This is my script for CSIT 111 to take attendance.
 
The File Open dialog at the beginning can be used to select a CSV file
exported from Brightspace's Grades page for the given course.
 
After a loop of all students in the roster, we repeat once to make sure we
got everyone, and then finally save the list of absent students in a dated file.

Edits by Veronica Noone 1/27/2025

added Try/Except to prevent error when canceling file open.
Added filename to make code more dynamic for use with multiple CSVs
Modulairzed for readability
took our references to CSIT 111 and made messaging more generic for use with other classes.
Added list of potential responses to increase readability
Edited display text slighty "they" to "you" etc. 

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
posResponses = ["yes","y","yea","p","here"]
 

def takeAttendance():
    # Loop through the rows in the CSV file
    try:
        with open(file_path, mode='r') as file:
            # Create a CSV DictReader object to parse the file
            # Read the CSV file exported from Brightspace's Grades page
            csv_reader = csv.DictReader(file)
            print("Attendance from " + os.path.basename(file.name) + "\n")
            for student in csv_reader:
                    # Print each name using dictionary lookups
                    print(student.get('First Name') + " " + student.get('Last Name'))
            
                    # Wait for user input on student presence
                    presence = input("\nAre you here?\n")
                    if presence in posResponses:
                            print("Welcome to CSIT 111, " + student.get('First Name') + "!\n")
                    else:
                            potentially_absent.append(student.get('First Name') + ' ' + student.get('Last Name'))
                            print("Added " + student.get('First Name') + " to the potentially absent list for later.\n")
            print("That's the whole course roster. Now repeating potentially absent students.\n")
    except FileNotFoundError:
        print("FileNotFoundError: File not found.")
        quit()
#end takeAttendance 
        

def secChance(): 
    # Loop through the list of potentially absent students
    for name in potentially_absent:
            print(name)
            presence = input("\nAre they here?\n")
            if presence in posResponses:
                    print("Welcome to class, " + name + "!\n")
            else:
                    marked_absent.append(name)
                    print("Marked " + name + " as absent.\n")
                    
    # Generate a filename for today's absentees
    absent_file = "absent-" + datetime.today().strftime('%m-%d-%Y' + ".txt")
     
    # Open the absent file for writing/appending
    with open(absent_file, 'a') as file:
            # Append the final absentee list
            print("Absentee list:")
            file.write("Absentee list: \n")
            for name in marked_absent:
                    print(name)
                    file.write(name + "\n")
#end secChance

takeAttendance()
secChance()
