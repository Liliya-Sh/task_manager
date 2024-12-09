from dataclasses import dataclass


@dataclass
class Task:
    """Модель Задачи"""
    id: int
    title: str
    description: str
    category: str
    due_date: str
    priority: str
    status: str = 'Не выполнена'

    def __str__(self):
        return (f"\nID: {self.id}\nНазвание: {self.title}\nОписание: {self.description}"
                f"\nКатегория: {self.category}\nСрок: {self.due_date}\nПриоритет: {self.priority}"
                f"\nСтатус: {self.status}")
