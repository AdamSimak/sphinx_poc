"""
Task Data Models
================
This module defines the core Task entity used across the application.
It handles unique identification, state transitions, and priority validation.
"""

import uuid
from datetime import datetime

class Task:
    """
    Represents a single unit of work in the system.
    
    This class ensures that every task has a unique ID and tracks 
    its lifecycle from creation to completion.
    """

    # Allowed priority levels for validation
    PRIORITIES = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}

    def __init__(self, title, description="", priority="MEDIUM", due_date=None):
        """
        Initialize a new Task instance.

        :param title: A short summary of the task.
        :type title: str
        :param description: Detailed explanation of the work required.
        :type description: str
        :param priority: Importance level (LOW, MEDIUM, HIGH, CRITICAL).
        :type priority: str
        :param due_date: Optional deadline in YYYY-MM-DD format.
        :type due_date: str, optional
        :raises ValueError: If the provided priority is not in the allowed list.
        """
        if priority.upper() not in self.PRIORITIES:
            raise ValueError(f"Priority must be one of {self.PRIORITIES}")

        self.task_id = str(uuid.uuid4())[:8]
        self.title = title
        self.description = description
        self.priority = priority.upper()
        self.due_date = due_date
        self.created_at = datetime.now().isoformat()
        self.completed_at = None
        self.status = "OPEN"

    def mark_completed(self):
        """
        Transitions the task to the COMPLETED state.
        
        Records the current timestamp to 'completed_at' and updates the status.
        
        .. note:: 
           A completed task cannot be reopened in the current version.
        """
        self.status = "COMPLETED"
        self.completed_at = datetime.now().isoformat()

    def is_overdue(self):
        """
        Checks if the task is past its due date.

        :return: True if current date is past due_date, False otherwise.
        :rtype: bool
        """
        if not self.due_date or self.status == "COMPLETED":
            return False
        
        current_date = datetime.now().strftime("%Y-%m-%d")
        return self.due_date < current_date

    def __repr__(self):
        return f"<Task {self.task_id} | {self.title} | {self.status}>"