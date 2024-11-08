import json
from dataclasses import dataclass, field
from typing import List, Dict
from pathlib import Path

from student import Student, StudentType


@dataclass
class DanceClass:
    class_id: int
    class_name: str
    room_capacity: int
    available_days: List[int]
    data_save_path: Path
    students: Dict[StudentType, List] = field(default_factory=lambda: {StudentType.LEADER: [],
                                                                       StudentType.FOLLOWER: []})

    def __post_init__(self):
        self.save_data()

    def add_student(self, student: Student) -> bool:
        leaders = len(self.students[StudentType.LEADER])
        followers = len(self.students[StudentType.FOLLOWER])
        if student.student_type == StudentType.LEADER:
            leaders += 1
        else:
            followers += 1
        if abs(leaders - followers) > 2:
            print('Sorry, you can\'t be attend to this class, it will cause disbalance of leaders and followers amount')
            return False
        if self.room_capacity >= leaders + followers:
            self.students[student.student_type].append(student)
            self.save_data()
            return True
        else:
            print("Sorry, no places left\n")
            return False

    def save_data(self):
        """Saving and updating class info in the local store

        Serializing into JSON format DanceClass and Student classes.
        """
        with self.data_save_path.open('r') as f:
            data = json.load(f)

        data[self.class_id] = {
            "class_id": self.class_id,
            "class_name": self.class_name,
            "room_capacity": self.room_capacity,
            "available_days": self.available_days,
            "students": {},
        }
        for student_type, students_per_type in self.students.items():
            students = [student.serialize() for student in students_per_type]
            data[self.class_id]["students"][student_type.value] = students

        with self.data_save_path.open('w') as f:
            json.dump(data, f)

    @classmethod
    def init_from_data(cls, class_data, data_save_path: Path):
        """Getting class instance from local store."""
        students = {}
        for student_type, raw_students in class_data["students"].items():
            students[StudentType(int(student_type))] = [Student.deserialize(raw_data) for raw_data in raw_students]
        return cls(
            class_id=class_data["class_id"],
            class_name=class_data["class_name"],
            room_capacity=class_data["room_capacity"],
            available_days=class_data["available_days"],
            students=students,
            data_save_path=data_save_path
        )
