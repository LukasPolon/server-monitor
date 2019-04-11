""" Module with various helpers and constant variables."""

import os
import sys

from datetime import datetime


PATH_DIR_SRC = os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))
PATH_DIR_PROJECT = os.path.abspath(os.path.join(PATH_DIR_SRC, '..'))


def get_current_datetime():
    """ Read current date and time and parse it accordingly:
        "2019-04-11 18:28:35"

        Returns:
            current_date(str): date and time in string format
    """
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return current_time
