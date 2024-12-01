from app import ManagerTasks
from data_cquisition import ReceivedData


class AppTasksManager:
    """Приложение менеджер задач"""

    def __init__(self):
        self.task_manager = ManagerTasks()
        self.received_data = ReceivedData()

    def select_action(self):
        """Выбрать действие"""
        while True:
            try:
                print("\nВыберите действие:")
                print("1. Просмотреть список задач")
                print("2. Поиск задачи по категориям,по статутсу или по ключевым словам")
                print("3. Добавить задачу")
                print("4. Редактировать задачу")
                print("5. Поменять статус задачи")
                print("6. Удалить задачу")
                print("7. Закрыть программу")
                choice = int(input("Введите номер действия (1/2/3/4/5/6/7): "))

                if choice == 1:
                    self.view_tasks()
                elif choice == 2:
                    self.search_task()
                elif choice == 3:
                    self.add_task()
                elif choice == 4:
                    self.edit_task()
                elif choice == 5:
                    self.change_status()
                elif choice == 6:
                    self.delete_task()
                elif choice == 7:
                    self.exit_program()

            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите номер действия от 1 до 7.")

    def view_tasks(self):
        """Просмотр списка задач"""
        print(self.task_manager.all_tasks())

    def search_task(self):
        """Поиск задачи по ID"""
        criterion = self.received_data.get_criterion()
        if criterion == 1:
            meaning = self.received_data.get_category()
        elif criterion == 2:
            meaning = self.received_data.get_status()
        elif criterion == 3:
            meaning = self.received_data.get_word()
        print(self.task_manager.search_task(criterion, meaning))

    def add_task(self):
        """Добавить новую задачу"""
        title = self.received_data.get_title()
        description = self.received_data.get_description()
        category = self.received_data.get_category()
        due_date = self.received_data.get_due_date()
        priority = self.received_data.get_priority()
        result = self.task_manager.add_task(title, description, category, due_date, priority)
        print("Задача добавлена:", result)

    def edit_task(self):
        """Редактировать задачу, по ID"""
        id_task = self.received_data.get_id()
        title = self.received_data.get_title()
        description = self.received_data.get_description()
        category = self.received_data.get_category()
        due_date = self.received_data.get_due_date()
        priority = self.received_data.get_priority()
        print(self.task_manager.edit_task(id_task, title, description, category, due_date, priority))

    def change_status(self):
        """Изменить статус задачи, по ID"""
        id_task = self.received_data.get_id()
        status_task = self.received_data.get_status()
        print(self.task_manager.change_status(id_task, status_task))

    def delete_task(self):
        """Удалить задачу, по ID"""
        id_task = self.received_data.get_id()
        print(self.task_manager.delete_task(id_task))

    @staticmethod
    def exit_program():
        """Закрыть программу"""
        print("Закрыть программу.")
        exit()


if __name__ == '__main__':
    manager = AppTasksManager()
    manager.select_action()
