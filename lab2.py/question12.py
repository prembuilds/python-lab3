def get_students():
    count = int(input("How many students? "))
    records = {}
    for i in range(count):
        student_name = input(f"Enter name of student {i + 1}: ")
        scores = []
        for j in range(3):
            score = int(input(f"Enter mark for subject {j + 1}: "))
            scores.append(score)
        records[student_name] = scores
    return records

def show_averages(records):
    avg_scores = {}
    print("\nAverage Marks for Each Student:")
    for student, marks in records.items():
        average = sum(marks) / len(marks)
        avg_scores[student] = average
        print(f"{student}: {average:.2f}")
    return avg_scores

def get_topper(avg_scores):
    highest = max(avg_scores, key=avg_scores.get)
    print(f"\nTopper: {highest} with average {avg_scores[highest]:.2f}")

def change_marks(records):
    name_to_update = input("\nWhose marks do you want to update? ")
    if name_to_update in records:
        new_scores = []
        for j in range(3):
            score = int(input(f"Enter new mark for subject {j + 1}: "))
            new_scores.append(score)
        records[name_to_update] = new_scores
        print(f"Updated marks for {name_to_update}.")
    else:
        print("No student found with that name.")

data = get_students()
averages = show_averages(data)
get_topper(averages)
change_marks(data)
averages = show_averages(data)
get_topper(averages)
