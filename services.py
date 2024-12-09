from typing import Optional

from validation_db import is_valid_due_date, is_valid_get_priority
from models import Task
from repository import TaskRepository


class TaskService:
    def __init__(self):
        self.repository = TaskRepository()
        self.tasks = self.repository.tasks

    def all_tasks(self) -> str:
        """Просмотреть список всех задач"""
        if not self.tasks:
            return "Список задач пуст."
        return '\n'.join(str(task) for task in self.tasks)

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """Находит задачу по ID"""
        return next((task for task in self.tasks if task.id == task_id), None)

    def search_task(self, meaning: str) -> str:
        """Поиск задачи по категориям, статусу или по ключевым словам"""
        result = []
        meaning_lower = meaning.lower()

        for task in self.tasks:
            if (meaning_lower in task.title.lower() or
                    meaning_lower in task.description.lower() or
                    meaning_lower in task.category.lower() or
                    meaning_lower in task.status.lower()):
                result.append(str(task))

        return '\n'.join(result) if result else "Задачи с такими данными нет"

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str) -> str:
        """Добавить новую задачу"""
        for task in self.tasks:
            if task.title == title:
                return 'Такая задача уже есть в списке'

        task_id = max((task.id for task in self.tasks), default=0) + 1
        valid_due_date = is_valid_due_date(due_date)
        valid_priority = is_valid_get_priority(priority)
        new_task = Task(task_id, title, description, category, valid_due_date, valid_priority)
        self.tasks.append(new_task)
        self.repository.save_to_file()
        return str(new_task)

    def change_status(self, task_id: int, status_task: str) -> str:
        """Меняем статус задачи на 'выполнена' или 'не выполнена'"""
        task = self.find_task_by_id(task_id)
        if task:
            task.status = status_task
            self.repository.save_to_file()
            return f'У задачи id:{task_id}, статус:{status_task}'
        return f'Задача с ID {task_id} не найдена.'

    def edit_task(self, task_id, title=None, description=None, category=None, due_date=None, priority=None,
                  status=None):
        """Редактировать задачу,поиск по ID"""
        task_to_edit = self.find_task_by_id(task_id)
        if task_to_edit is None:
            return f"Задача с ID {task_id} не найдена."

        if title is not None and title.strip() != "":
            task_to_edit.title = title
        if description is not None and description.strip() != "":
            task_to_edit.description = description
        if category is not None and category.strip() != "":
            task_to_edit.category = category
        if due_date is not None and is_valid_due_date(due_date) and due_date.strip() != "":
            task_to_edit.due_date = due_date
        if priority is not None and is_valid_get_priority(priority) and priority.strip() != "":
            task_to_edit.priority = priority
        if status is not None and status.strip() != "":
            task_to_edit.status = status

        self.repository.save_to_file()
        return str(task_to_edit)

    def delete_task(self, task_id: int) -> str:
        """Удалить задачу по ID"""
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.repository.save_to_file()
            return f'Задача с ID {task_id} была удалена.'
        return f'Задача с ID {task_id} не найдена.'
