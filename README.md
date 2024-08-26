# Student-Management-App
A Python application for managing student profiles, courses, and grades. Features include profile creation, course enrollment, grade tracking, and GPA calculation. Utilizes Python's standard libraries (csv, os, re) with no external dependencies. 

Features
Student Management: Allows the creation of a student profile with ID, name, age, gender, and email.
Course Management: Enables students to add, remove, and view courses.
Grade Management: Provides functionality to add, update, and view grades, as well as calculate GPA.
Input Validation: Validates user input for names, emails, student IDs, ages, and gender.
Usage
Create a Student Profile:

get_student_object() prompts the user for their name, email, student ID, age, and gender.
Input is validated for correctness. The loop restarts from the beginning if any input is invalid, rather than resuming from the invalid input point.
Course Operations:

add_course(): Adds a new course after validating course details.
remove_course(): Removes a course based on course ID.
Grade Operations:

add_grade(): Adds a grade to a specified course.
update_grade(): Updates the grade for a specified course.
View Information:

print_grades(): Displays all grades for the student.
get_gpa(): Calculates and displays the GPA based on grades.
print_all_courses(): Lists all enrolled courses.

Notes
This application uses only Python's standard libraries (csv, os, re) and no external packages.
The input validation in get_student_object() currently restarts the entire input process from the beginning if any input is invalid. There is a need to modify this so that the loop continues from the point where invalid input was entered.

Code Overview
Student class: Manages student attributes and operations.
Course class: Represents course details.
get_student_object(): Gathers and validates student information.
run_app(student_object): Main application loop that interacts with the user.
Feel free to fork and contribute to enhance the functionality and usability of this student management system!
