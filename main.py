import logging
from school.student import register as rg
from school.teacher import employ as em
from school.record import registry as rt

logger = logging.getLogger(__name__)
# defining constant variable
SCHOOL = "XYZ School"

if __name__ == "__main__":
    # STUDENT 1
    print("Student 1\n=========")
    logger.info("Registering student S1 details")
    student_details = {"name": "Anu", "age": 12}
    s1 = rg.register_student(student_details)

    logger.info("Updating student registry")
    rt.update_registry(student_details, "STUDENT")

    # changing class variable directly using class name
    rg.Student.school_name = SCHOOL

    # STUDENT 2
    print("Student 2\n=========")
    logger.info("Registering student S2 details")
    student_details = {"name": "Jancy", "age": 13}
    s2 = rg.register_student(student_details)

    logger.info("Updating student registry")
    rt.update_registry(student_details, "STUDENT")

    # TEACHER 1
    print("Teacher 1\n=========")
    logger.info("Registering teacher T1 details")
    teacher_details = {"name": "Mariam", "age": 40}
    t1 = em.register_teacher(teacher_details)

    logger.info("Updating teacher registry")
    rt.update_registry(teacher_details, "TEACHER")

    # calling class method via instance variable
    t1.change_school(new_school=SCHOOL)

    # TEACHER 2
    print("Teacher 2\n=========")
    logger.info("Registering teacher T2 details")
    teacher_details = {"name": "Hannah", "age": 32}
    t2 = em.register_teacher(teacher_details)

    logger.info("Updating teacher registry")
    rt.update_registry(teacher_details, "TEACHER")

