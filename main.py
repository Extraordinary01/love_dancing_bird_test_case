import json
from pathlib import Path

from dance_class import DanceClass
from student import Student


DAYS_OF_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


if __name__ == '__main__':
    data_path = Path("dance_school_data.txt")
    with data_path.open('r') as f:
        data = json.load(f)

    print('This is available dance school classes:\n\n')
    for class_id, class_info in data.items():
        print(f'''
    This is class: {class_info["class_name"]}. Class id is {class_id}. Available days of week to attend: 
    {", ".join(DAYS_OF_WEEK[day] for day in class_info["available_days"])}.\n\n
                ''')

    while True:
        student_name = input("Please provide student name or 0 for closing application\n")
        if student_name.strip() == "0":
            break

        try:
            student_type = int(input("Please set student type from these 2 options:\n1) Leader\n2) Follower\n"))
            new_student = Student(name=student_name, student_type=student_type)
        except Exception:
            print("Wrong student type provided. Starting from beginning!\n\n")
            continue

        while True:
            selected_class_id = input("Please type class_id of class, which you want to attend!\n")

            selected_class_data = data.get(selected_class_id)
            if not selected_class_data:
                print(f"Class with class_id: {selected_class_id} doesn't exist! Please type class_id correctly!\n\n")
                continue

            selected_class = DanceClass.init_from_data(selected_class_data, data_path)
            is_attended = selected_class.add_student(new_student)

            if not is_attended:
                try_again = input("Maybe you want to attend another class? Type yes or no\n")

                if try_again == "no":
                    break
            else:
                with data_path.open('r') as f:
                    data = json.load(f)
                print("Student successfully attended to the class!\n\n")
                break

    print("Application closed")
