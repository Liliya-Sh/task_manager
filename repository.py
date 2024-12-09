import json

from models import Task


class TaskRepository:
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
