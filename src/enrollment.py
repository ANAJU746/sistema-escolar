"""Enrollment management module"""

from typing import Optional
from datetime import datetime


class Enrollment:
    """Represents a student's enrollment in a course"""
    
    def __init__(self, enrollment_id: str, student_id: str, course_id: str):
        """
        Initialize a new enrollment
        
        Args:
            enrollment_id: Unique enrollment identifier
            student_id: ID of the enrolled student
            course_id: ID of the course
        """
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = datetime.now().strftime("%Y-%m-%d")
        self.grade = None
        self.status = "active"  # active, completed, dropped
    
    def __str__(self):
        return f"Enrollment({self.enrollment_id}, Student: {self.student_id}, Course: {self.course_id})"
    
    def __repr__(self):
        return f"Enrollment(enrollment_id={self.enrollment_id!r}, student_id={self.student_id!r}, course_id={self.course_id!r})"
    
    def set_grade(self, grade: float):
        """Set the grade for this enrollment"""
        if 0 <= grade <= 100:
            self.grade = grade
            return True
        return False
    
    def to_dict(self):
        """Convert enrollment to dictionary"""
        return {
            'enrollment_id': self.enrollment_id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'enrollment_date': self.enrollment_date,
            'grade': self.grade,
            'status': self.status
        }


class EnrollmentManager:
    """Manages enrollment records"""
    
    def __init__(self, student_manager, course_manager):
        """
        Initialize enrollment manager
        
        Args:
            student_manager: StudentManager instance
            course_manager: CourseManager instance
        """
        self.enrollments = {}
        self.student_manager = student_manager
        self.course_manager = course_manager
    
    def enroll_student(self, enrollment: Enrollment) -> bool:
        """
        Enroll a student in a course
        
        Args:
            enrollment: Enrollment object
            
        Returns:
            True if enrollment was successful, False otherwise
        """
        # Verify student and course exist
        student = self.student_manager.get_student(enrollment.student_id)
        course = self.course_manager.get_course(enrollment.course_id)
        
        if not student or not course:
            return False
        
        if enrollment.enrollment_id in self.enrollments:
            return False
        
        self.enrollments[enrollment.enrollment_id] = enrollment
        return True
    
    def get_enrollment(self, enrollment_id: str) -> Optional[Enrollment]:
        """
        Get an enrollment by ID
        
        Args:
            enrollment_id: The enrollment's ID
            
        Returns:
            Enrollment object if found, None otherwise
        """
        return self.enrollments.get(enrollment_id)
    
    def get_student_enrollments(self, student_id: str):
        """Get all enrollments for a student"""
        return [e for e in self.enrollments.values() if e.student_id == student_id]
    
    def get_course_enrollments(self, course_id: str):
        """Get all enrollments for a course"""
        return [e for e in self.enrollments.values() if e.course_id == course_id]
    
    def update_enrollment_status(self, enrollment_id: str, status: str) -> bool:
        """
        Update enrollment status
        
        Args:
            enrollment_id: The enrollment's ID
            status: New status (active, completed, dropped)
            
        Returns:
            True if updated, False if not found
        """
        enrollment = self.enrollments.get(enrollment_id)
        if not enrollment:
            return False
        
        if status in ["active", "completed", "dropped"]:
            enrollment.status = status
            return True
        return False
    
    def set_grade(self, enrollment_id: str, grade: float) -> bool:
        """
        Set grade for an enrollment
        
        Args:
            enrollment_id: The enrollment's ID
            grade: Grade value (0-100)
            
        Returns:
            True if grade was set, False otherwise
        """
        enrollment = self.enrollments.get(enrollment_id)
        if not enrollment:
            return False
        
        return enrollment.set_grade(grade)
    
    def drop_enrollment(self, enrollment_id: str) -> bool:
        """
        Drop an enrollment (mark as dropped)
        
        Args:
            enrollment_id: The enrollment's ID
            
        Returns:
            True if dropped, False if not found
        """
        return self.update_enrollment_status(enrollment_id, "dropped")
