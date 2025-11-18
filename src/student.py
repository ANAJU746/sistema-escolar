"""Student management module"""

from typing import Optional


class Student:
    """Represents a student in the school system"""
    
    def __init__(self, student_id: str, name: str, email: str, birth_date: str):
        """
        Initialize a new student
        
        Args:
            student_id: Unique student identifier
            name: Student's full name
            email: Student's email address
            birth_date: Student's birth date (YYYY-MM-DD)
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.birth_date = birth_date
        self.enrollments = []
    
    def __str__(self):
        return f"Student({self.student_id}, {self.name})"
    
    def __repr__(self):
        return f"Student(student_id={self.student_id!r}, name={self.name!r}, email={self.email!r})"
    
    def to_dict(self):
        """Convert student to dictionary"""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'email': self.email,
            'birth_date': self.birth_date
        }


class StudentManager:
    """Manages student records"""
    
    def __init__(self):
        self.students = {}
    
    def add_student(self, student: Student) -> bool:
        """
        Add a new student to the system
        
        Args:
            student: Student object to add
            
        Returns:
            True if student was added, False if student_id already exists
        """
        if student.student_id in self.students:
            return False
        self.students[student.student_id] = student
        return True
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """
        Get a student by ID
        
        Args:
            student_id: The student's ID
            
        Returns:
            Student object if found, None otherwise
        """
        return self.students.get(student_id)
    
    def update_student(self, student_id: str, **kwargs) -> bool:
        """
        Update student information
        
        Args:
            student_id: The student's ID
            **kwargs: Fields to update (name, email, birth_date)
            
        Returns:
            True if student was updated, False if not found
        """
        student = self.students.get(student_id)
        if not student:
            return False
        
        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)
        
        return True
    
    def delete_student(self, student_id: str) -> bool:
        """
        Delete a student from the system
        
        Args:
            student_id: The student's ID
            
        Returns:
            True if student was deleted, False if not found
        """
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False
    
    def list_students(self):
        """Return list of all students"""
        return list(self.students.values())
