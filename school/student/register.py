import logging
logger = logging.getLogger(__name__)


class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Profile :\nName - {self.name}\nAge - {self.age}")

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school


def register_student(student_details: dict):
    s = Student(**student_details)
    logger.debug(f"Successfully added student details")
    s.display()
    return s
