"""Tests for course module"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from course import Course, CourseManager


def test_course_creation():
    """Test creating a course"""
    course = Course("C001", "Test Course", "A test course", 3)
    assert course.course_id == "C001"
    assert course.name == "Test Course"
    assert course.description == "A test course"
    assert course.credits == 3


def test_course_to_dict():
    """Test course to dictionary conversion"""
    course = Course("C001", "Test Course", "A test course", 3)
    course_dict = course.to_dict()
    assert course_dict['course_id'] == "C001"
    assert course_dict['name'] == "Test Course"
    assert course_dict['credits'] == 3


def test_add_course():
    """Test adding a course to manager"""
    manager = CourseManager()
    course = Course("C001", "Test Course", "A test course", 3)
    
    assert manager.add_course(course) == True
    assert manager.add_course(course) == False  # Duplicate


def test_get_course():
    """Test getting a course"""
    manager = CourseManager()
    course = Course("C001", "Test Course", "A test course", 3)
    manager.add_course(course)
    
    retrieved = manager.get_course("C001")
    assert retrieved is not None
    assert retrieved.name == "Test Course"
    
    assert manager.get_course("C999") is None


def test_update_course():
    """Test updating a course"""
    manager = CourseManager()
    course = Course("C001", "Test Course", "A test course", 3)
    manager.add_course(course)
    
    assert manager.update_course("C001", name="Updated Course") == True
    updated = manager.get_course("C001")
    assert updated.name == "Updated Course"
    
    assert manager.update_course("C999", name="Test") == False


def test_delete_course():
    """Test deleting a course"""
    manager = CourseManager()
    course = Course("C001", "Test Course", "A test course", 3)
    manager.add_course(course)
    
    assert manager.delete_course("C001") == True
    assert manager.get_course("C001") is None
    assert manager.delete_course("C001") == False


def test_list_courses():
    """Test listing all courses"""
    manager = CourseManager()
    course1 = Course("C001", "Course 1", "Description 1", 3)
    course2 = Course("C002", "Course 2", "Description 2", 4)
    
    manager.add_course(course1)
    manager.add_course(course2)
    
    courses = manager.list_courses()
    assert len(courses) == 2


if __name__ == "__main__":
    test_course_creation()
    test_course_to_dict()
    test_add_course()
    test_get_course()
    test_update_course()
    test_delete_course()
    test_list_courses()
    print("All course tests passed!")
