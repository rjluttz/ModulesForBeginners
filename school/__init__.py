import logging.config

"""
- __init__ is executed automatically when package school is imported
- While executing main.py, imports are taking place from that directory
- Hence, we can specify "logging.conf" instead of "../logging.conf"
"""
logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger()
