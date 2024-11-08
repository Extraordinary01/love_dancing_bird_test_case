import json
from pathlib import Path
from dance_class import DanceClass


if __name__ == '__main__':
    save_path = Path("dance_school_data.txt")

    with save_path.open('w') as f:

        json.dump({}, f)

    class_count = 0
    while True:
        class_count += 1
        class_name = input("Please provide a new class name, you may pass empty string, then we'll set class name for "
                           "you! If you want to stop adding new classes, then enter 0\n")

        if class_name.strip() == "0":
            break
        elif class_name.strip() == "":
            class_name = f"Class № {class_count}"

        try:
            room_capacity = int(input("Please provide room capacity of this class!\n"))
        except TypeError:
            print("You should pass a number for setting room capacity! Create class from beginning!\n\n")
            continue

        try:
            available_days = list(map(int, input("Please provide days of week, when class will be attend. "
                                                 "Divide the days by spaces! Notice: 0 - is Sunday.\n").split(" ")))
        except Exception:
            print("Days passed wrong. Starting from beginning!\n\n")
            continue

        DanceClass(class_id=class_count, class_name=class_name, room_capacity=room_capacity,
                   available_days=available_days, data_save_path=save_path)

        print("New class successfully added to database!\n")

    print("You'll finish the setup of Dance school classes. Remember, if you'll run this script again, all provided "
          "data before will be erased!")
