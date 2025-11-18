"""Main application entry point for Sistema Escolar"""

from student import StudentManager, Student
from course import CourseManager, Course
from enrollment import EnrollmentManager, Enrollment


def print_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("SISTEMA ESCOLAR - School Management System")
    print("="*50)
    print("1. Student Management")
    print("2. Course Management")
    print("3. Enrollment Management")
    print("4. Exit")
    print("="*50)


def student_menu(student_manager):
    """Handle student management operations"""
    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. List Students")
        print("3. View Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back to Main Menu")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == "1":
            student_id = input("Student ID: ").strip()
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            birth_date = input("Birth Date (YYYY-MM-DD): ").strip()
            
            student = Student(student_id, name, email, birth_date)
            if student_manager.add_student(student):
                print(f"✓ Student {name} added successfully!")
            else:
                print(f"✗ Student ID {student_id} already exists!")
        
        elif choice == "2":
            students = student_manager.list_students()
            if students:
                print(f"\nTotal Students: {len(students)}")
                for student in students:
                    print(f"  - {student}")
            else:
                print("No students found.")
        
        elif choice == "3":
            student_id = input("Student ID: ").strip()
            student = student_manager.get_student(student_id)
            if student:
                print(f"\nStudent Details:")
                print(f"  ID: {student.student_id}")
                print(f"  Name: {student.name}")
                print(f"  Email: {student.email}")
                print(f"  Birth Date: {student.birth_date}")
            else:
                print(f"✗ Student not found!")
        
        elif choice == "4":
            student_id = input("Student ID: ").strip()
            if student_manager.get_student(student_id):
                name = input("New Name (leave empty to skip): ").strip()
                email = input("New Email (leave empty to skip): ").strip()
                
                updates = {}
                if name:
                    updates['name'] = name
                if email:
                    updates['email'] = email
                
                if updates:
                    student_manager.update_student(student_id, **updates)
                    print("✓ Student updated successfully!")
                else:
                    print("No updates provided.")
            else:
                print(f"✗ Student not found!")
        
        elif choice == "5":
            student_id = input("Student ID: ").strip()
            if student_manager.delete_student(student_id):
                print("✓ Student deleted successfully!")
            else:
                print(f"✗ Student not found!")
        
        elif choice == "6":
            break


def course_menu(course_manager):
    """Handle course management operations"""
    while True:
        print("\n--- Course Management ---")
        print("1. Add Course")
        print("2. List Courses")
        print("3. View Course")
        print("4. Update Course")
        print("5. Delete Course")
        print("6. Back to Main Menu")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == "1":
            course_id = input("Course ID: ").strip()
            name = input("Course Name: ").strip()
            description = input("Description: ").strip()
            credits = int(input("Credits: ").strip())
            
            course = Course(course_id, name, description, credits)
            if course_manager.add_course(course):
                print(f"✓ Course {name} added successfully!")
            else:
                print(f"✗ Course ID {course_id} already exists!")
        
        elif choice == "2":
            courses = course_manager.list_courses()
            if courses:
                print(f"\nTotal Courses: {len(courses)}")
                for course in courses:
                    print(f"  - {course} ({course.credits} credits)")
            else:
                print("No courses found.")
        
        elif choice == "3":
            course_id = input("Course ID: ").strip()
            course = course_manager.get_course(course_id)
            if course:
                print(f"\nCourse Details:")
                print(f"  ID: {course.course_id}")
                print(f"  Name: {course.name}")
                print(f"  Description: {course.description}")
                print(f"  Credits: {course.credits}")
            else:
                print(f"✗ Course not found!")
        
        elif choice == "4":
            course_id = input("Course ID: ").strip()
            if course_manager.get_course(course_id):
                name = input("New Name (leave empty to skip): ").strip()
                description = input("New Description (leave empty to skip): ").strip()
                
                updates = {}
                if name:
                    updates['name'] = name
                if description:
                    updates['description'] = description
                
                if updates:
                    course_manager.update_course(course_id, **updates)
                    print("✓ Course updated successfully!")
                else:
                    print("No updates provided.")
            else:
                print(f"✗ Course not found!")
        
        elif choice == "5":
            course_id = input("Course ID: ").strip()
            if course_manager.delete_course(course_id):
                print("✓ Course deleted successfully!")
            else:
                print(f"✗ Course not found!")
        
        elif choice == "6":
            break


def enrollment_menu(enrollment_manager, student_manager, course_manager):
    """Handle enrollment management operations"""
    while True:
        print("\n--- Enrollment Management ---")
        print("1. Enroll Student")
        print("2. View Student Enrollments")
        print("3. View Course Enrollments")
        print("4. Set Grade")
        print("5. Drop Enrollment")
        print("6. Back to Main Menu")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == "1":
            enrollment_id = input("Enrollment ID: ").strip()
            student_id = input("Student ID: ").strip()
            course_id = input("Course ID: ").strip()
            
            enrollment = Enrollment(enrollment_id, student_id, course_id)
            if enrollment_manager.enroll_student(enrollment):
                student = student_manager.get_student(student_id)
                course = course_manager.get_course(course_id)
                print(f"✓ {student.name} enrolled in {course.name} successfully!")
            else:
                print(f"✗ Enrollment failed! Check if student and course exist.")
        
        elif choice == "2":
            student_id = input("Student ID: ").strip()
            enrollments = enrollment_manager.get_student_enrollments(student_id)
            if enrollments:
                print(f"\nEnrollments for Student {student_id}:")
                for enr in enrollments:
                    course = course_manager.get_course(enr.course_id)
                    grade_str = f"{enr.grade}" if enr.grade is not None else "N/A"
                    print(f"  - {course.name} | Grade: {grade_str} | Status: {enr.status}")
            else:
                print("No enrollments found.")
        
        elif choice == "3":
            course_id = input("Course ID: ").strip()
            enrollments = enrollment_manager.get_course_enrollments(course_id)
            if enrollments:
                print(f"\nEnrollments for Course {course_id}:")
                for enr in enrollments:
                    student = student_manager.get_student(enr.student_id)
                    grade_str = f"{enr.grade}" if enr.grade is not None else "N/A"
                    print(f"  - {student.name} | Grade: {grade_str} | Status: {enr.status}")
            else:
                print("No enrollments found.")
        
        elif choice == "4":
            enrollment_id = input("Enrollment ID: ").strip()
            grade = float(input("Grade (0-100): ").strip())
            if enrollment_manager.set_grade(enrollment_id, grade):
                print("✓ Grade set successfully!")
            else:
                print(f"✗ Failed to set grade! Check enrollment ID and grade range.")
        
        elif choice == "5":
            enrollment_id = input("Enrollment ID: ").strip()
            if enrollment_manager.drop_enrollment(enrollment_id):
                print("✓ Enrollment dropped successfully!")
            else:
                print(f"✗ Enrollment not found!")
        
        elif choice == "6":
            break


def main():
    """Main application loop"""
    # Initialize managers
    student_manager = StudentManager()
    course_manager = CourseManager()
    enrollment_manager = EnrollmentManager(student_manager, course_manager)
    
    # Add some sample data
    print("Initializing with sample data...")
    
    # Sample students
    student_manager.add_student(Student("S001", "Ana Silva", "ana@email.com", "2005-03-15"))
    student_manager.add_student(Student("S002", "João Santos", "joao@email.com", "2004-07-22"))
    
    # Sample courses
    course_manager.add_course(Course("C001", "Mathematics", "Basic mathematics course", 4))
    course_manager.add_course(Course("C002", "Portuguese", "Portuguese language and literature", 3))
    
    # Sample enrollments
    enrollment_manager.enroll_student(Enrollment("E001", "S001", "C001"))
    enrollment_manager.enroll_student(Enrollment("E002", "S002", "C002"))
    
    print("Sample data loaded!")
    
    # Main loop
    while True:
        print_menu()
        choice = input("\nEnter choice: ").strip()
        
        if choice == "1":
            student_menu(student_manager)
        elif choice == "2":
            course_menu(course_manager)
        elif choice == "3":
            enrollment_menu(enrollment_manager, student_manager, course_manager)
        elif choice == "4":
            print("\nThank you for using Sistema Escolar!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
