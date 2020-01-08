import os
import logging
from logging import FileHandler, Formatter
"""
    The logger made as indipendent module for ease of use and readability
"""
def file_handler(location):
    cwd = os.getcwd()
    file_handler1 = FileHandler(location)
    file_handler1.setLevel(logging.INFO)
    log_format = Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        )
    file_handler1.setFormatter(log_format)
    return file_handler1