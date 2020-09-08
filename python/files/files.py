import inspect
import os
# KEYS=[python current file]


def current_file() -> str:
    """
    Return the absolute file of the script calling this function
    e.g
       /tmp/my.py calls current_file()  will return /tmp/my.py
    see: https://stackoverflow.com/questions/13699283/how-to-get-the-callers-filename-method-name-in-python
    """
    frame = inspect.stack()[1]
    filename = frame[0].f_code.co_filename

    return os.path.abspath(filename)
