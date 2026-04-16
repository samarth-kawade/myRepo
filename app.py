#!/usr/bin/env python3
"""
Task Manager Application
Syncs with TaskHub web application via JSON files
"""

import json
import os
from datetime import datetime


class TaskManager:
    """Manages tasks with file persistence (compatible with TaskHub web app)"""

    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file (compatible with web app format)"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []

    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, text, completed=False):
        """Add a new task (compatible with web app format)"""
        task = {
            'id': int(datetime.now().timestamp() * 1000),
            'text': text,
            'completed': completed,
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def list_tasks(self, show_completed=True):
        """List all tasks"""
        if not self.tasks:
            print("\nNo tasks found.")
            return

        print("\n" + "=" * 60)
        print("TASKS")
        print("=" * 60)

        for task in self.tasks:
            if not show_completed and task['completed']:
                continue

            status = "✓" if task['completed'] else "○"
            print(f"{status} [{task['id']}] {task['text']}")

    def complete_task(self, task_id):
        """Mark task as complete"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task {task_id} marked as complete!")
                return
        print(f"Task {task_id} not found.")

    def delete_task(self, task_id):
        """Delete a task"""
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        self.save_tasks()
        print(f"Task {task_id} deleted!")

    def get_stats(self):
        """Get task statistics"""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t['completed'])
        pending = total - completed
        return {'total': total, 'completed': completed, 'pending': pending}


def main():
    """Main application loop"""
    manager = TaskManager()

    print("\n" + "=" * 60)
    print("TASK MANAGER - Synced with TaskHub Web App")
    print("=" * 60)
    print(f"Data file: {manager.filename}")

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. View statistics")
        print("6. Exit")

        choice = input("\nSelect an option (1-6): ").strip()

        if choice == '1':
            text = input("Enter task: ").strip()
            if text:
                task = manager.add_task(text)
                print(f"✓ Task added: {task['text']}")
            else:
                print("Task cannot be empty.")

        elif choice == '2':
            manager.list_tasks()

        elif choice == '3':
            try:
                task_id = int(input("Enter task ID: ").strip())
                manager.complete_task(task_id)
            except ValueError:
                print("Invalid task ID.")

        elif choice == '4':
            try:
                task_id = int(input("Enter task ID: ").strip())
                manager.delete_task(task_id)
            except ValueError:
                print("Invalid task ID.")

        elif choice == '5':
            stats = manager.get_stats()
            print(f"\nTotal Tasks: {stats['total']}")
            print(f"Completed: {stats['completed']}")
            print(f"Pending: {stats['pending']}")

        elif choice == '6':
            print("\nGoodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()
