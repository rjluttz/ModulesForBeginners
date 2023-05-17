import logging
logger = logging.getLogger(__name__)


def apply_details(personal_file, details, code):
    logging.info(f"Applying details to Registry")
    if code == "STUDENT":
        s = personal_file.register_student(details)
        logger.debug(f"Student : {s}")
    else:
        t = personal_file.register_teacher(details)
        logger.debug(f"Teacher : {t}")
