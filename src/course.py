"""Course management module"""

from typing import Optional


class Course:
    """Represents a course in the school system"""
    
    def __init__(self, course_id: str, name: str, description: str, credits: int):
        """
        Initialize a new course
        
        Args:
            course_id: Unique course identifier
            name: Course name
            description: Course description
            credits: Number of credits
        """
        self.course_id = course_id
        self.name = name
        self.description = description
        self.credits = credits
    
    def __str__(self):
        return f"Course({self.course_id}, {self.name})"
    
    def __repr__(self):
        return f"Course(course_id={self.course_id!r}, name={self.name!r}, credits={self.credits})"
    
    def to_dict(self):
        """Convert course to dictionary"""
        return {
            'course_id': self.course_id,
            'name': self.name,
            'description': self.description,
            'credits': self.credits
        }


class CourseManager:
    """Manages course records"""
    
    def __init__(self):
        self.courses = {}
    
    def add_course(self, course: Course) -> bool:
        """
        Add a new course to the system
        
        Args:
            course: Course object to add
            
        Returns:
            True if course was added, False if course_id already exists
        """
        if course.course_id in self.courses:
            return False
        self.courses[course.course_id] = course
        return True
    
    def get_course(self, course_id: str) -> Optional[Course]:
        """
        Get a course by ID
        
        Args:
            course_id: The course's ID
            
        Returns:
            Course object if found, None otherwise
        """
        return self.courses.get(course_id)
    
    def update_course(self, course_id: str, **kwargs) -> bool:
        """
        Update course information
        
        Args:
            course_id: The course's ID
            **kwargs: Fields to update (name, description, credits)
            
        Returns:
            True if course was updated, False if not found
        """
        course = self.courses.get(course_id)
        if not course:
            return False
        
        for key, value in kwargs.items():
            if hasattr(course, key):
                setattr(course, key, value)
        
        return True
    
    def delete_course(self, course_id: str) -> bool:
        """
        Delete a course from the system
        
        Args:
            course_id: The course's ID
            
        Returns:
            True if course was deleted, False if not found
        """
        if course_id in self.courses:
            del self.courses[course_id]
            return True
        return False
    
    def list_courses(self):
        """Return list of all courses"""
        return list(self.courses.values())
