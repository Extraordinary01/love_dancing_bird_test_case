from enum import Enum


class StudentType(Enum):
    LEADER = 1
    FOLLOWER = 2


class Student:

    def __init__(self, name: str, student_type: int):
        self.name = name
        self.student_type = StudentType(student_type)

    def serialize(self) -> dict:
        """Converts student data for initialization into dict.

        We use this method for passing student data into file.
        """
        return {
            'name': self.name,
            'student_type': self.student_type.value
        }

    @classmethod
    def deserialize(cls, data: dict):
        return cls(
            name=data['name'],
            student_type=data['student_type']
        )
