"""
Task Management Engine
======================
The engine module provides the high-level API for managing tasks, 
including bulk operations, filtering, and reporting.
"""

class TaskManager:
    """
    Main controller class for task operations.
    
    Acts as a container for tasks and provides methods for analysis 
    and batch processing.
    """

    def __init__(self, manager_name="General"):
        """
        :param manager_name: Name of the project or department.
        """
        self.manager_name = manager_name
        self.tasks = []

    def add_task(self, task_instance):
        """
        Registers a new task in the manager's inventory.

        :param task_instance: An instance of the Task class.
        :type task_instance: src.models.task.Task
        """
        self.tasks.append(task_instance)

    def get_tasks_by_priority(self, priority):
        """
        Filters the internal list for tasks matching a specific priority.

        :param priority: The priority level to filter by (e.g., 'CRITICAL').
        :return: List of filtered Task objects.
        :rtype: list
        """
        return [t for t in self.tasks if t.priority == priority.upper()]

    def get_summary_report(self):
        """
        Generates a dictionary report of current task statistics.

        :return: Summary containing total, completed, and open task counts.
        :rtype: dict
        """
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.status == "COMPLETED"])
        return {
            "manager": self.manager_name,
            "total_tasks": total,
            "completed_tasks": completed,
            "open_tasks": total - completed,
            "success_rate": round(completed / total, 2) if total > 0 else 0.0
        }

    def clear_completed(self):
        """
        Removes all completed tasks from the active inventory.
        
        .. warning:: 
           This operation deletes data from memory. Ensure reports are saved first.
        """
        self.tasks = [t for t in self.tasks if t.status != "COMPLETED"]