#!/usr/bin/env python3
"""
Simple Python Application
A basic task management application with file persistence
"""

import json
import os
from datetime import datetime


class TaskManager:
    """Manages tasks with file persistence"""

    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file"""
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

    def add_task(self, title, description=''):
        """Add a new task"""
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.now().isoformat(),
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
            print(f"{status} [{task['id']}] {task['title']}")
            if task['description']:
                print(f"    {task['description']}")

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
    print("WELCOME TO TASK MANAGER")
    print("=" * 60)

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
            title = input("Enter task title: ").strip()
            description = input("Enter description (optional): ").strip()
            task = manager.add_task(title, description)
            print(f"Task added: {task['title']}")

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
