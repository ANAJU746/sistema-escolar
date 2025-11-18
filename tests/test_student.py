"""Tests for student module"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from student import Student, StudentManager


def test_student_creation():
    """Test creating a student"""
    student = Student("S001", "Test Student", "test@email.com", "2005-01-01")
    assert student.student_id == "S001"
    assert student.name == "Test Student"
    assert student.email == "test@email.com"
    assert student.birth_date == "2005-01-01"


def test_student_to_dict():
    """Test student to dictionary conversion"""
    student = Student("S001", "Test Student", "test@email.com", "2005-01-01")
    student_dict = student.to_dict()
    assert student_dict['student_id'] == "S001"
    assert student_dict['name'] == "Test Student"


def test_add_student():
    """Test adding a student to manager"""
    manager = StudentManager()
    student = Student("S001", "Test Student", "test@email.com", "2005-01-01")
    
    assert manager.add_student(student) == True
    assert manager.add_student(student) == False  # Duplicate


def test_get_student():
    """Test getting a student"""
    manager = StudentManager()
    student = Student("S001", "Test Student", "test@email.com", "2005-01-01")
    manager.add_student(student)
    
    retrieved = manager.get_student("S001")
    assert retrieved is not None
    assert retrieved.name == "Test Student"
    
    assert manager.get_student("S999") is None


def test_update_student():
    """Test updating a student"""
    manager = StudentManager()
    student = Student("S001", "Test Student", "test@email.com", "2005-01-01")
    manager.add_student(student)
    
    assert manager.update_student("S001", name="Updated Name") == True
    updated = manager.get_student("S001")
    assert updated.name == "Updated Name"
    
    assert manager.update_student("S999", name="Test") == False


def test_delete_student():
    """Test deleting a student"""
    manager = StudentManager()
    student = Student("S001", "Test Student", "test@email.com", "2005-01-01")
    manager.add_student(student)
    
    assert manager.delete_student("S001") == True
    assert manager.get_student("S001") is None
    assert manager.delete_student("S001") == False


def test_list_students():
    """Test listing all students"""
    manager = StudentManager()
    student1 = Student("S001", "Student 1", "s1@email.com", "2005-01-01")
    student2 = Student("S002", "Student 2", "s2@email.com", "2005-02-02")
    
    manager.add_student(student1)
    manager.add_student(student2)
    
    students = manager.list_students()
    assert len(students) == 2


if __name__ == "__main__":
    test_student_creation()
    test_student_to_dict()
    test_add_student()
    test_get_student()
    test_update_student()
    test_delete_student()
    test_list_students()
    print("All student tests passed!")
