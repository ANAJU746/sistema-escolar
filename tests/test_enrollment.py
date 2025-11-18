"""Tests for enrollment module"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from student import Student, StudentManager
from course import Course, CourseManager
from enrollment import Enrollment, EnrollmentManager


def test_enrollment_creation():
    """Test creating an enrollment"""
    enrollment = Enrollment("E001", "S001", "C001")
    assert enrollment.enrollment_id == "E001"
    assert enrollment.student_id == "S001"
    assert enrollment.course_id == "C001"
    assert enrollment.status == "active"
    assert enrollment.grade is None


def test_enrollment_set_grade():
    """Test setting a grade"""
    enrollment = Enrollment("E001", "S001", "C001")
    
    assert enrollment.set_grade(85.5) == True
    assert enrollment.grade == 85.5
    
    assert enrollment.set_grade(150) == False  # Invalid grade
    assert enrollment.set_grade(-10) == False  # Invalid grade


def test_enrollment_to_dict():
    """Test enrollment to dictionary conversion"""
    enrollment = Enrollment("E001", "S001", "C001")
    enrollment.set_grade(90)
    
    enrollment_dict = enrollment.to_dict()
    assert enrollment_dict['enrollment_id'] == "E001"
    assert enrollment_dict['student_id'] == "S001"
    assert enrollment_dict['course_id'] == "C001"
    assert enrollment_dict['grade'] == 90


def test_enroll_student():
    """Test enrolling a student in a course"""
    student_manager = StudentManager()
    course_manager = CourseManager()
    enrollment_manager = EnrollmentManager(student_manager, course_manager)
    
    # Add student and course
    student = Student("S001", "Test Student", "test@email.com", "2005-01-01")
    course = Course("C001", "Test Course", "A test course", 3)
    student_manager.add_student(student)
    course_manager.add_course(course)
    
    # Enroll student
    enrollment = Enrollment("E001", "S001", "C001")
    assert enrollment_manager.enroll_student(enrollment) == True
    
    # Try duplicate enrollment
    enrollment2 = Enrollment("E001", "S001", "C001")
    assert enrollment_manager.enroll_student(enrollment2) == False
    
    # Try enrolling with non-existent student
    enrollment3 = Enrollment("E002", "S999", "C001")
    assert enrollment_manager.enroll_student(enrollment3) == False


def test_get_enrollment():
    """Test getting an enrollment"""
    student_manager = StudentManager()
    course_manager = CourseManager()
    enrollment_manager = EnrollmentManager(student_manager, course_manager)
    
    student = Student("S001", "Test Student", "test@email.com", "2005-01-01")
    course = Course("C001", "Test Course", "A test course", 3)
    student_manager.add_student(student)
    course_manager.add_course(course)
    
    enrollment = Enrollment("E001", "S001", "C001")
    enrollment_manager.enroll_student(enrollment)
    
    retrieved = enrollment_manager.get_enrollment("E001")
    assert retrieved is not None
    assert retrieved.student_id == "S001"
    
    assert enrollment_manager.get_enrollment("E999") is None


def test_get_student_enrollments():
    """Test getting all enrollments for a student"""
    student_manager = StudentManager()
    course_manager = CourseManager()
    enrollment_manager = EnrollmentManager(student_manager, course_manager)
    
    student = Student("S001", "Test Student", "test@email.com", "2005-01-01")
    course1 = Course("C001", "Course 1", "Description 1", 3)
    course2 = Course("C002", "Course 2", "Description 2", 4)
    student_manager.add_student(student)
    course_manager.add_course(course1)
    course_manager.add_course(course2)
    
    enrollment1 = Enrollment("E001", "S001", "C001")
    enrollment2 = Enrollment("E002", "S001", "C002")
    enrollment_manager.enroll_student(enrollment1)
    enrollment_manager.enroll_student(enrollment2)
    
    enrollments = enrollment_manager.get_student_enrollments("S001")
    assert len(enrollments) == 2


def test_set_grade():
    """Test setting grade through enrollment manager"""
    student_manager = StudentManager()
    course_manager = CourseManager()
    enrollment_manager = EnrollmentManager(student_manager, course_manager)
    
    student = Student("S001", "Test Student", "test@email.com", "2005-01-01")
    course = Course("C001", "Test Course", "A test course", 3)
    student_manager.add_student(student)
    course_manager.add_course(course)
    
    enrollment = Enrollment("E001", "S001", "C001")
    enrollment_manager.enroll_student(enrollment)
    
    assert enrollment_manager.set_grade("E001", 95.0) == True
    retrieved = enrollment_manager.get_enrollment("E001")
    assert retrieved.grade == 95.0
    
    assert enrollment_manager.set_grade("E999", 95.0) == False


def test_drop_enrollment():
    """Test dropping an enrollment"""
    student_manager = StudentManager()
    course_manager = CourseManager()
    enrollment_manager = EnrollmentManager(student_manager, course_manager)
    
    student = Student("S001", "Test Student", "test@email.com", "2005-01-01")
    course = Course("C001", "Test Course", "A test course", 3)
    student_manager.add_student(student)
    course_manager.add_course(course)
    
    enrollment = Enrollment("E001", "S001", "C001")
    enrollment_manager.enroll_student(enrollment)
    
    assert enrollment_manager.drop_enrollment("E001") == True
    retrieved = enrollment_manager.get_enrollment("E001")
    assert retrieved.status == "dropped"


if __name__ == "__main__":
    test_enrollment_creation()
    test_enrollment_set_grade()
    test_enrollment_to_dict()
    test_enroll_student()
    test_get_enrollment()
    test_get_student_enrollments()
    test_set_grade()
    test_drop_enrollment()
    print("All enrollment tests passed!")
