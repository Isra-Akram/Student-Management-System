student_record = []
while True:
    x = "====Student Management System==="
    option_1 = "Add student"
    option_2 = "View Student"
    option_3 = "Search student"
    option_4 = "Update student"
    option_5 = "Delete student"
    option_6 = "Exit"
    print(x)

    print("1.", option_1)
    print("2.", option_2)
    print("3.", option_3)
    print("4.", option_4)
    print("5.", option_5)
    print("6.", option_6)

    choice = int(input("Enter your choice:"))


    ask = "yes"
    if choice == 1:
        print("Add Student selected")
        while ask == "yes":
            student_name = input("Enter your name: ")
            student_rollno = int(input("Enter your roll no: "))
            student_marks = int(input("Enter your marks: "))

            if student_marks >= 90:
                grade = "A+"
            elif student_marks >= 80 and student_marks < 90:
                grade = "A"
            elif student_marks >= 70 and student_marks < 80:
                grade = "B"
            elif student_marks >= 60 and student_marks < 70:
                grade = "C"
            elif student_marks >= 50 and student_marks < 60:
                grade = "D"
            else:
                grade = "Fail"

            student_information = {
                "name": student_name,
                "roll no": student_rollno,
                "marks": student_marks,
                "grade": grade,
    }

            student_record.append(student_information)
            print(student_record)

            ask = input("Do you want to add another student? ")

    elif choice==2:
        print("View Student selected")     

        print("\n===== Students =====")

        for result in student_record:
            print("Name:", result["name"])
            print("Roll No:", result["roll no"])
            print("Marks:", result["marks"])
            print("Grade:", result["grade"])
            print("-------------------")

    elif choice==3:
        print("Search Student selected")
        found = False
        search_roll = int(input("Enter roll no to search: "))
        for result2 in student_record:
            if result2["roll no"] == search_roll:
                print(result2)
                found = True
        if found == False:
            print("Not found")

    elif choice ==4:
        print("Update Student selected")
        update_roll = int(input("Enter roll no to update: "))
        for result3 in student_record:
            if result3["roll no"] == update_roll:
                new_marks = int(input("Enter new marks: "))
                result3["marks"] = new_marks
                if new_marks >= 90:
                    new_grade = "A+"
                elif new_marks >= 80:
                    new_grade = "A"
                elif new_marks >= 70:
                    new_grade = "B"
                elif new_marks >= 60:
                    new_grade = "C"
                elif new_marks >= 50:
                    new_grade = "D"
                else:
                    new_grade = "Fail"

                result3["grade"] = new_grade
                print(result3)
        print("Student updated successfully")

    elif choice == 5:
        print("Delete student selected")
        find = False
        delete_roll = int(input("Enter roll no to delete: "))
        for result4 in student_record:
            if result4["roll no"] == delete_roll:
                student_record.remove(result4)
                print("Student deleted successfully")
                find = True
        if find == False:
            print("Roll no is not found")

    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please choose 1-6.")






