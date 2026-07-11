"""
Student Management System
A comprehensive system for managing student records, grades, and courses.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class Student:
    """Represents a student with personal and academic information."""
    
    def __init__(self, student_id: str, name: str, email: str, major: str):
        """Initialize a student with basic information."""
        self.student_id = student_id
        self.name = name
        self.email = email
        self.major = major
        self.courses = []
        self.grades = {}
        self.enrollment_date = datetime.now()
    
    def enroll_course(self, course_id: str) -> None:
        """Enroll student in a course."""
        if course_id not in self.courses:
            self.courses.append(course_id)
    
    def add_grade(self, course_id: str, grade: float) -> None:
        """Add or update grade for a course."""
        if 0 <= grade <= 100:
            self.grades[course_id] = grade
        else:
            raise ValueError("Grade must be between 0 and 100")
    
    def get_gpa(self) -> float:
        """Calculate GPA based on grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    
    def to_dict(self) -> Dict:
        """Convert student to dictionary."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'email': self.email,
            'major': self.major,
            'courses': self.courses,
            'grades': self.grades,
            'gpa': self.get_gpa()
        }


class Course:
    """Represents an academic course."""
    
    def __init__(self, course_id: str, name: str, instructor: str, credits: int):
        """Initialize a course with basic information."""
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
        self.credits = credits
        self.students = []
        self.description = ""
        self.schedule = ""
    
    def add_student(self, student_id: str) -> None:
        """Add a student to the course."""
        if student_id not in self.students:
            self.students.append(student_id)
    
    def remove_student(self, student_id: str) -> None:
        """Remove a student from the course."""
        if student_id in self.students:
            self.students.remove(student_id)
    
    def get_student_count(self) -> int:
        """Return the number of students in the course."""
        return len(self.students)
    
    def to_dict(self) -> Dict:
        """Convert course to dictionary."""
        return {
            'course_id': self.course_id,
            'name': self.name,
            'instructor': self.instructor,
            'credits': self.credits,
            'students': self.students,
            'description': self.description,
            'schedule': self.schedule
        }


class University:
    """Manages students and courses for a university."""
    
    def __init__(self, name: str):
        """Initialize university with a name."""
        self.name = name
        self.students: Dict[str, Student] = {}
        self.courses: Dict[str, Course] = {}
    
    def add_student(self, student: Student) -> bool:
        """Add a new student to the university."""
        if student.student_id not in self.students:
            self.students[student.student_id] = student
            return True
        return False
    
    def add_course(self, course: Course) -> bool:
        """Add a new course to the university."""
        if course.course_id not in self.courses:
            self.courses[course.course_id] = course
            return True
        return False
    
    def enroll_student(self, student_id: str, course_id: str) -> bool:
        """Enroll a student in a course."""
        if student_id in self.students and course_id in self.courses:
            self.students[student_id].enroll_course(course_id)
            self.courses[course_id].add_student(student_id)
            return True
        return False
    
    def assign_grade(self, student_id: str, course_id: str, grade: float) -> bool:
        """Assign a grade to a student for a course."""
        if student_id in self.students:
            try:
                self.students[student_id].add_grade(course_id, grade)
                return True
            except ValueError:
                return False
        return False
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """Retrieve a student by ID."""
        return self.students.get(student_id)
    
    def get_course(self, course_id: str) -> Optional[Course]:
        """Retrieve a course by ID."""
        return self.courses.get(course_id)
    
    def get_all_students(self) -> List[Student]:
        """Get all students in the university."""
        return list(self.students.values())
    
    def get_all_courses(self) -> List[Course]:
        """Get all courses in the university."""
        return list(self.courses.values())
    
    def get_top_students(self, n: int = 5) -> List[Student]:
        """Get top N students by GPA."""
        sorted_students = sorted(self.students.values(), 
                                key=lambda s: s.get_gpa(), 
                                reverse=True)
        return sorted_students[:n]
    
    def get_course_statistics(self, course_id: str) -> Dict:
        """Get statistics for a course."""
        course = self.get_course(course_id)
        if not course:
            return {}
        
        grades = []
        for student_id in course.students:
            student = self.get_student(student_id)
            if student and course_id in student.grades:
                grades.append(student.grades[course_id])
        
        if not grades:
            return {'course_id': course_id, 'student_count': 0}
        
        return {
            'course_id': course_id,
            'course_name': course.name,
            'student_count': len(grades),
            'average_grade': sum(grades) / len(grades),
            'highest_grade': max(grades),
            'lowest_grade': min(grades)
        }


class UniversityManager:
    """Manager class for handling university data persistence and operations."""
    
    def __init__(self, data_file: str = "university_data.json"):
        """Initialize the manager with a data file."""
        self.data_file = data_file
        self.university = None
    
    def create_university(self, name: str) -> University:
        """Create a new university."""
        self.university = University(name)
        return self.university
    
    def save_data(self) -> bool:
        """Save university data to file."""
        if not self.university:
            return False
        
        data = {
            'name': self.university.name,
            'students': [s.to_dict() for s in self.university.get_all_students()],
            'courses': [c.to_dict() for c in self.university.get_all_courses()]
        }
        
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2, default=str)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self) -> bool:
        """Load university data from file."""
        if not os.path.exists(self.data_file):
            return False
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            
            self.university = University(data['name'])
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False


def main():
    """Main function to demonstrate the university system."""
    
    # Create university
    manager = UniversityManager()
    uni = manager.create_university("Tech University")
    
    # Add some students
    students_data = [
        ("S001", "Alice Johnson", "alice@tech.edu", "Computer Science"),
        ("S002", "Bob Smith", "bob@tech.edu", "Mathematics"),
        ("S003", "Carol White", "carol@tech.edu", "Computer Science"),
        ("S004", "David Brown", "david@tech.edu", "Physics"),
        ("S005", "Emma Davis", "emma@tech.edu", "Computer Science"),
    ]
    
    for sid, name, email, major in students_data:
        student = Student(sid, name, email, major)
        uni.add_student(student)
    
    # Add some courses
    courses_data = [
        ("C001", "Introduction to Python", "Dr. Smith", 3),
        ("C002", "Data Structures", "Dr. Johnson", 4),
        ("C003", "Web Development", "Dr. Williams", 3),
        ("C004", "Database Design", "Dr. Brown", 4),
    ]
    
    for cid, name, instructor, credits in courses_data:
        course = Course(cid, name, instructor, credits)
        uni.add_course(course)
    
    # Enroll students in courses
    enrollments = [
        ("S001", "C001"), ("S001", "C002"), ("S001", "C003"),
        ("S002", "C001"), ("S002", "C004"),
        ("S003", "C001"), ("S003", "C002"), ("S003", "C003"), ("S003", "C004"),
        ("S004", "C002"), ("S004", "C004"),
        ("S005", "C001"), ("S005", "C003"),
    ]
    
    for student_id, course_id in enrollments:
        uni.enroll_student(student_id, course_id)
    
    # Assign grades
    grades = [
        ("S001", "C001", 95), ("S001", "C002", 88), ("S001", "C003", 92),
        ("S002", "C001", 78), ("S002", "C004", 85),
        ("S003", "C001", 98), ("S003", "C002", 95), ("S003", "C003", 96), ("S003", "C004", 94),
        ("S004", "C002", 82), ("S004", "C004", 80),
        ("S005", "C001", 85), ("S005", "C003", 89),
    ]
    
    for student_id, course_id, grade in grades:
        uni.assign_grade(student_id, course_id, grade)
    
    # Display results
    print(f"\n{'='*60}")
    print(f"{uni.name} Management System")
    print(f"{'='*60}\n")
    
    print("Top 3 Students by GPA:")
    print("-" * 60)
    for i, student in enumerate(uni.get_top_students(3), 1):
        print(f"{i}. {student.name} - GPA: {student.get_gpa():.2f}")
    
    print(f"\n{'='*60}")
    print("Course Statistics:")
    print(f"{'='*60}")
    for course in uni.get_all_courses():
        stats = uni.get_course_statistics(course.course_id)
        if stats.get('student_count', 0) > 0:
            print(f"\n{stats['course_name']} ({stats['course_id']})")
            print(f"  Students: {stats['student_count']}")
            print(f"  Average Grade: {stats['average_grade']:.2f}")
            print(f"  Highest Grade: {stats['highest_grade']}")
            print(f"  Lowest Grade: {stats['lowest_grade']}")
    
    print(f"\n{'='*60}")
    print("Student Details:")
    print(f"{'='*60}")
    for student in uni.get_all_students():
        print(f"\n{student.name} ({student.student_id})")
        print(f"  Major: {student.major}")
        print(f"  Email: {student.email}")
        print(f"  GPA: {student.get_gpa():.2f}")
        print(f"  Courses: {len(student.courses)}")
    
    # Save data
    manager.save_data()
    print(f"\n{'='*60}")
    print("Data saved successfully!")


if __name__ == "__main__":
    main()
