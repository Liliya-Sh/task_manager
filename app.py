import json
from typing import Optional

from model_task import Task


class ManagerTasks:
    """Менеджер задач"""

    def __init__(self, filename='task.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Открыть файл и загрузить задачи, как объекты Task"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return [Task(**task_data) for task_data in data.get("tasks", [])]
        except FileNotFoundError:
            print("Файл task.json не найден.")
            return []

    def save_to_file(self):
        """Сохраняем данные в файл task.json"""
        tasks_data = [task.__dict__ for task in self.tasks]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump({"tasks": tasks_data}, f, ensure_ascii=False, indent=2)

    def all_tasks(self) -> str:
        """Просмотреть список всех задач"""
        if not self.tasks:
            return "Список задач пуст."
        return '\n'.join(str(task) for task in self.tasks)

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """Находит задачу по ID"""
        return next((task for task in self.tasks if task.id == task_id), None)

    def search_task(self, criterion: int, meaning: str) -> str:
        """Поиск задачи по категориям, статусу или по ключевым словам"""
        result = []
        meaning_lower = meaning.lower()

        for task in self.tasks:
            if criterion == 1 and task.category.lower() == meaning_lower:
                result.append(str(task))
            elif criterion == 2 and task.status.lower() == meaning_lower:
                result.append(str(task))
            elif criterion == 3:
                if meaning_lower in task.title.lower() or meaning_lower in task.description.lower():
                    result.append(str(task))

        return '\n'.join(result) if result else "Задачи с такими данными нет"

    def add_task(self, title: str, description: str, category: str, due_date: str, prioriti: str) -> str:
        """Добавить новую задачу"""
        for task in self.tasks:
            if task.title == title:
                return 'Такая задача уже есть в списке'

        task_id = max((task.id for task in self.tasks), default=0) + 1
        new_task = Task(task_id, title, description, category, due_date, prioriti)
        self.tasks.append(new_task)
        self.save_to_file()
        return str(new_task)

    def change_status(self, task_id: int, status_task: str) -> str:
        """Меняем статус задачи на 'выполнена' или 'не выполнена'"""
        task = self.find_task_by_id(task_id)
        if task:
            task.status = status_task
            self.save_to_file()
            return f'У задачи id:{task_id}, статус:{status_task}'
        return f'Задача с ID {task_id} не найдена.'

    def edit_task(self, task_id, title=None, description=None, category=None, due_date=None, prioriti=None,
                  status=None):
        """Редактировать задачу,поиск по ID"""
        task_to_edit = self.find_task_by_id(task_id)
        if task_to_edit is None:
            return f"Задача с ID {task_id} не найдена."

        if title is not None:
            task_to_edit.title = title
        if description is not None:
            task_to_edit.description = description
        if category is not None:
            task_to_edit.category = category
        if due_date is not None:
            task_to_edit.due_date = due_date
        if prioriti is not None:
            task_to_edit.prioriti = prioriti
        if status is not None:
            task_to_edit.status = status

        self.save_to_file()
        return str(task_to_edit)

    def delete_task(self, task_id: int) -> str:
        """Удалить задачу по ID"""
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_to_file()
            return f'Задача с ID {task_id} была удалена.'
        return f'Задача с ID {task_id} не найдена.'
