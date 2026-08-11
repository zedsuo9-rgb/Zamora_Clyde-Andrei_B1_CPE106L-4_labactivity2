def main():
   
    student_records = {}

    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add Student Record (Create)")
        print("2. View Student Record (Read)")
        print("3. Update Student Record (Update)")
        print("4. Display All Students (Display)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\n--- Add New Student ---")
            student_id = input("Enter Student ID (e.g., 2023-001): ")
            
            name = input("Enter Student Name: ")
            
            courses_input = input("Enter enrolled courses (comma-separated, e.g., Math, Science): ")
            courses_list = [course.strip() for course in courses_input.split(',')]
            
            grades_input = input("Enter grades for Prelim, Midterm, and Finals (comma-separated, e.g., 85, 90, 88): ")
            try:
                grades_tuple = tuple(float(g.strip()) for g in grades_input.split(','))
            except ValueError:
                print("Invalid grades format. Defaulting to (0.0, 0.0, 0.0)")
                grades_tuple = (0.0, 0.0, 0.0)

            student_records[student_id] = {
                "name": name,
                "courses": courses_list,
                "grades": grades_tuple
            }
            print("Student added successfully!")

        elif choice == '2':
            print("\n--- View Student ---")
            student_id = input("Enter Student ID to search: ")
            
            if student_id in student_records:
                record = student_records[student_id]
                print(f"\nRecord for ID: {student_id}")
                print(f"Name: {record['name']}")
                print(f"Courses: {', '.join(record['courses'])}")
                print(f"Grades (Prelim, Midterm, Finals): {record['grades']}")
            else:
                print("Error: Student record not found.")

        elif choice == '3':
            print("\n--- Update Student ---")
            student_id = input("Enter Student ID to update: ")
            
            if student_id in student_records:
                print("Note: Leave a field blank and press Enter to keep the current value.")
                
                current_name = student_records[student_id]['name']
                new_name = input(f"Enter new Name ({current_name}): ")
                
                current_courses = ", ".join(student_records[student_id]['courses'])
                new_courses = input(f"Enter new courses ({current_courses}): ")
                
                current_grades = ", ".join(map(str, student_records[student_id]['grades']))
                new_grades = input(f"Enter new grades ({current_grades}): ")

                if new_name.strip():
                    student_records[student_id]['name'] = new_name.strip()
                
                if new_courses.strip():
                    student_records[student_id]['courses'] = [c.strip() for c in new_courses.split(',')]
                
                if new_grades.strip():
                    try:
                        student_records[student_id]['grades'] = tuple(float(g.strip()) for g in new_grades.split(','))
                    except ValueError:
                        print("Invalid grades format. Grades remain unchanged.")
                
                print("Student record updated successfully!")
            else:
                print("Error: Student record not found.")

        elif choice == '4':
            print("\n--- All Student Records ---")
            if not student_records:
                print("No student records found in the database.")
            else:
                for s_id, data in student_records.items():
                    print(f"ID: {s_id} | Name: {data['name']} | Courses: {data['courses']} | Grades: {data['grades']}")

        elif choice == '5':
            print("Exiting the Student Record Management System. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()