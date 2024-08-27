import csv
import os
import re
from typing import List, Dict, Optional

# Constants
VALID_EMAIL_DOMAINS = ["com", "edu", "net"]
VALID_GENDERS = ["m", "f", "male", "female"]

def main():
    student = Student.get_student()
    run_app(student) 

class Student: 
    def __init__(self, student_id: str, name: str, age: int, gender: str, email: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.courses_enrolled: List['Course'] = []
        self.grades: Dict[str, int] = {}

    def __repr__(self) -> str:
        return f"Name: {self.name}, ID: {self.student_id}, E-mail: {self.email}"    

    def __str__(self) -> str:
        return f"Student(name={self.name}, id={self.student_id}, email={self.email}, age={self.age}, gender={self.gender})"

    def add_course(self):
        course = self.get_course_input()
        if course:
            self.courses_enrolled.append(course)  

    def remove_course(self):
        if not self.courses_enrolled:
            print("No courses enrolled")
            return

        course_id = input("Enter the ID of the course you want to remove: ").strip()
        if not course_id:
            print("Course ID cannot be empty")
            return 
        
        course = self.find_course_by_id(course_id)
        if course:
            self.courses_enrolled.remove(course)
            print(f"Course with ID {course_id} removed!")
            self.grades.pop(course_id, None)
        else:
            print(f"Course with ID {course_id} not found")

    def add_grade(self):
        course_id = input("Enter the course ID to add grade: ").strip()
        if not course_id:
            print("Course ID cannot be empty")
            return
        
        grade = input("Enter the new grade: ").strip()
        if not grade.isdigit():
            print("Grade must be a number")
            return
        
        grade = int(grade)
        course = self.find_course_by_id(course_id)
        if course:
            self.grades[course_id] = grade
            print(f"Grade {grade} added to {course.course_name}")
        else:
            print(f"Course with ID {course_id} not found")

    def update_grade(self):
        course_id = input("Enter the course ID for the course you want to update: ").strip()
        if not course_id:
            print("Course ID cannot be empty")
            return
        
        new_grade = input("Enter the new grade: ").strip()
        if not new_grade.isdigit():
            print("Grade must be a number")
            return
        
        new_grade = int(new_grade)
        course = self.find_course_by_id(course_id)
        if course:
            self.grades[course_id] = new_grade
            print(f"Grade updated to {new_grade} for course {course_id}")
        else:
            print(f"Course with ID {course_id} not found")

    def print_grades(self):
        if not self.grades:
            print("No grades recorded")
            return
        for key, grade in self.grades.items():
            print(f"{key} - {grade}")   

    def get_gpa(self):
        if not self.grades:
            print("No grades recorded")
            return
        gpa = sum(self.grades.values()) / len(self.grades)
        print(f"Your GPA: {gpa:.2f}")
    
    def print_all_courses(self):
        if not self.courses_enrolled:
            print("No courses enrolled")
            return
        for course in self.courses_enrolled:
            print(course.course_name)

    def find_course_by_id(self, course_id: str) -> Optional['Course']:
        for course in self.courses_enrolled:
            if course.course_id == course_id:
                return course
        return None

    def get_course_input(self) -> Optional['Course']:
        course_name = input("Enter course name: ").strip()
        if not self.is_valid_course_name(course_name):
            print("Course name is invalid")
            return None
        
        course_id = input("Enter course ID: ").strip()
        if not self.is_valid_course_id(course_id):
            print("Course ID is invalid")
            return None
        
        instructor = input("Enter instructor's name: ").strip()
        if not self.is_valid_instructor(instructor):
            print("Instructor name is invalid")
            return None

        self.save_course_to_file(course_id, course_name, instructor)
        return Course(course_id, course_name, instructor)

    @staticmethod
    def is_valid_course_name(name: str) -> bool:
        return bool(re.fullmatch(r"^[a-z\s]+$", name, re.IGNORECASE))

    @staticmethod
    def is_valid_course_id(course_id: str) -> bool:
        return bool(re.fullmatch(r"^[a-z0-9/\s]+$", course_id, re.IGNORECASE))

    @staticmethod
    def is_valid_instructor(instructor: str) -> bool:
        return bool(re.fullmatch(r"^[a-z\s]+$", instructor, re.IGNORECASE))

    @staticmethod
    def save_course_to_file(course_id: str, course_name: str, instructor: str):
        file_exists = os.path.isfile("courses.csv")
        with open("courses.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["course_id", "course_name", "instructor"])
            if not file_exists:
                writer.writeheader()   
            writer.writerow({"course_id": course_id, "course_name": course_name, "instructor": instructor})

    @classmethod
    def get_student() -> Student:
        while True:
            student_name = input("Enter your full name: ").strip()
            if not cls.is_valid_name(student_name):
                print("Name is invalid!")
                continue
            
            student_email = input("Enter email: ").strip()
            if not cls.is_valid_email(student_email):
                print("E-mail is invalid!")
                continue
            
            student_id = input("Enter your student ID: ").strip()
            if not cls.is_valid_student_id(student_id):
                print("ID is invalid")
                continue
            
            student_age = input("Enter your age: ").strip()
            if not student_age.isdigit():
                print("Age must be a number")
                continue
            
            student_gender = input("Enter your gender: ").strip()
            if not cls.is_valid_gender(student_gender):
                print("Gender is invalid!")
                continue
    
            return Student(student_id, student_name, int(student_age), student_gender, student_email)

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return bool(re.fullmatch(r"^[a-zA-Z\s]+$", name))

    @staticmethod
    def is_valid_email(email: str) -> bool:
        return bool(re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|edu|net)$", email, re.IGNORECASE))

    @staticmethod
    def is_valid_student_id(student_id: str) -> bool:
        return bool(re.fullmatch(r"^[a-zA-Z0-9/\s]+$", student_id))
  
    @staticmethod
    def is_valid_gender(gender: str) -> bool:
        return gender.lower() in VALID_GENDERS
        
class Course:
    def __init__(self, course_id: str, course_name: str, instructor: str): 
        self.course_id = course_id 
        self.course_name = course_name 
        self.instructor = instructor 

    def __repr__(self) -> str:
        return f"Course(id={self.course_id}, name={self.course_name}, instructor={self.instructor})"



def show_menu() -> int:
    print("-----Choose from the list below!-----")
    print("1. Enroll in a course")
    print("2. Remove a course")
    print("3. Add a grade")
    print("4. Update a grade")
    print("5. View all enrolled courses")
    print("6. Get GPA")
    print("7. View all grades")
    print("8. Exit the app")
    print("--------------------------------------")
    try:
        choice = int(input("Choose from 1 - 8: "))
        if 1 <= choice <= 8:
            return choice
        else:
            print("Invalid choice! Choose from 1 - 8.")
            return 0
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 8.")
        return 0

def run_app(student_object: Student):
    while True:
        choice = show_menu()
        if choice == 8:
            print("You exited the app")
            break
        elif choice == 1:
            student_object.add_course()
        elif choice == 2:
            student_object.remove_course()
        elif choice == 3:
            student_object.add_grade()
        elif choice == 4:
            student_object.update_grade()
        elif choice == 5:
            student_object.print_all_courses()
        elif choice == 6:
            student_object.get_gpa()
        elif choice == 7:
            student_object.print_grades()
        else:
            print("Wrong choice! Choose from 1 - 8.")

if __name__ == "__main__":
    main()
