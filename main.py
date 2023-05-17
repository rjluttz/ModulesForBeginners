import logging
from school.student import register as rg
from school.teacher import employ as em
from school.record import registry as rt

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Registering student details")
    student_details = {"name": "Anu", "age": 12}
    s1 = rg.register_student(student_details)

    logger.info("Updating student registry")
    rt.update_registry(student_details, "STUDENT")

    logger.info("Registering teacher details")
    teacher_details = {"name": "Mariam", "age": 40}
    t1 = em.register_teacher(teacher_details)

    logger.info("Updating teacher registry")
    rt.update_registry(teacher_details, "TEACHER")
