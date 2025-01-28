# PyAttend Attendance Taker

This is my script to take attendance.

## Changelog:

1/28/2025 by @AzzieDev
* Split the code into four specific function calls to recycle code.
* Display a different message for second iteration set for potentially absent students.
* Add more positive responses to accepted criteria and convert to lowercase.
* Refactored to snake_case variable names.
* Created Student class type to store first and last names.
* Further documentation.

1/27/2025 by @RoniNoone
* Added Try/Except to prevent error when canceling file open.
* Added filename to make code more dynamic for use with multiple CSVs
* Modularized for readability
* Took out references to CSIT 111, and made messaging more generic for use with other classes.
* Added list of potential responses to increase readability
* Edited display text slightly "they" to "you" etc. 

1/26/2025 by @AzzieDev
* Project initialized by David Katz
* The File Open dialog at the beginning can be used to select a CSV file
exported from Brightspace's Grades page for the given course.
* After a loop of all students in the roster, we repeat once to make sure we
got everyone, and then finally save the list of absent students in a dated file.
