"""
Utility Helpers
===============
A collection of standalone helper functions for data validation 
and string manipulation.
"""

import re

def validate_iso_date(date_string):
    """
    Validates if a string follows the ISO 8601 YYYY-MM-DD format.

    :param date_string: The string to be checked.
    :return: True if format is valid, False otherwise.
    :rtype: bool
    """
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    return bool(re.match(pattern, date_string))

def format_task_output(task):
    """
    Formats a task's information for console or text-file reporting.

    :param task: Task instance to format.
    :return: A multi-line string with task details.
    """
    line = "-" * 30
    return (
        f"{line}\n"
        f"ID: {task.task_id}\n"
        f"TITLE: {task.title}\n"
        f"PRIORITY: {task.priority}\n"
        f"STATUS: {task.status}\n"
        f"{line}"
    )