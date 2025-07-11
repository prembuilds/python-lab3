records = {}

while True:
    print("\n===== STUDENT REPORT CARD SYSTEM =====")
    print("1. Add new student")
    print("2. Show all student reports")
    print("3. Show class topper(s)")
    print("4. Search student by roll number")
    print("5. Show students who failed")
    print("6. Edit student marks")
    print("7. Exit")
    option = int(input("Select an option (1-7): "))

    if option == 1:
        roll_no = input("Enter student roll number: ")
        if roll_no in records:
            print("A student with this roll number already exists.")
        else:
            student_name = input("Enter student name: ")
            subjects = ['Electronics', 'Circuits', 'Mathematics', 'Programming', 'Chemistry']
            marks_dict = {}
            for subject in subjects:
                score = int(input(f"Marks for {subject}: "))
                marks_dict[subject] = score
            records[roll_no] = {"Name": student_name, "Marks": marks_dict}
            print("Student added successfully.")

    elif option == 2:
        if not records:
            print("No student records to display.")
        else:
            print("\n=== All Student Reports ===")
            for roll_no, info in records.items():
                print(f"\nRoll No: {roll_no}")
                print(f"Name   : {info['Name']}")
                for sub, mark in info['Marks'].items():
                    print(f"  {sub}: {mark}")
                avg_mark = sum(info['Marks'].values()) / len(info['Marks'])
                print(f"  Average: {avg_mark:.2f}")

    elif option == 3:
        if not records:
            print("No records available to determine topper.")
        else:
            highest_avg = -1
            toppers = []
            for roll_no, info in records.items():
                avg = sum(info['Marks'].values()) / len(info['Marks'])
                if avg > highest_avg:
                    highest_avg = avg
                    toppers = [(roll_no, info['Name'], avg)]
                elif avg == highest_avg:
                    toppers.append((roll_no, info['Name'], avg))
            print("\n=== Topper(s) ===")
            for t in toppers:
                print(f"Roll No: {t[0]}, Name: {t[1]}, Average: {t[2]:.2f}")

    elif option == 4:
        find_roll = input("Enter roll number to search: ")
        if find_roll in records:
            info = records[find_roll]
            print(f"\nRoll No: {find_roll}")
            print(f"Name   : {info['Name']}")
            for sub, mark in info['Marks'].items():
                print(f"  {sub}: {mark}")
            avg_mark = sum(info['Marks'].values()) / len(info['Marks'])
            print(f"  Average: {avg_mark:.2f}")
        else:
            print("No student found with that roll number.")

    elif option == 5:
        failed_found = False
        print("\nStudents failing in any subject (score below 40):")
        for roll_no, info in records.items():
            failed_subjects = [sub for sub, mark in info['Marks'].items() if mark < 40]
            if failed_subjects:
                failed_found = True
                print(f"{info['Name']} (Roll No: {roll_no}) failed in: {', '.join(failed_subjects)}")
        if not failed_found:
            print("All students passed all subjects.")

    elif option == 6:
        edit_roll = input("Enter roll number to edit marks: ")
        if edit_roll in records:
            sub_name = input("Enter subject to update: ")
            if sub_name in records[edit_roll]['Marks']:
                updated_score = int(input("Enter new mark: "))
                records[edit_roll]['Marks'][sub_name] = updated_score
                print("Marks updated.")
            else:
                print("Invalid subject name.")
        else:
            print("No student found with that roll number.")

    elif option == 7:
        print("Exiting Report Card System. Goodbye!")
        break

    else:
        print("Invalid option. Please choose between 1 and 7.")
