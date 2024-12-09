from services import TaskService


class ConsoleInterface:
    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def menu_app(self):
        """Выбрать действие"""
        while True:
            try:
                print("\nМеню:")
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
                    self.edit_status()
                elif choice == 6:
                    self.delete_task()
                elif choice == 7:
                    print("Закрыть программу.")
                    exit()

            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите номер действия от 1 до 7.")

    def view_tasks(self) -> None:
        """Просмотреть список всех задач"""
        print(self.task_service.all_tasks())

    def search_task(self) -> None:
        """Поиск задачи"""
        while True:
            try:
                meaning = input("Введите категорию, статусу или ключевое слово: ")
                found_tasks = self.task_service.search_task(meaning)
                print(found_tasks)
                break

            except ValueError:
                print('Введен неверный формат данных.')

    def add_task(self) -> None:
        """Добавить новую задачу"""
        while True:
            try:
                title = input("Введите название задачи: ")
                description = input("Введите описание задачи: ")
                category = input("Введите категорию задачи: ")
                due_date = input("Введите срок(дату) выполнения задачи в формате YYYY-MM-DD: ")
                priority = input("Укажите какой приоритет присвоить задаче: ")
                result = self.task_service.add_task(title.capitalize(),
                                                    description.capitalize(),
                                                    category.capitalize(),
                                                    due_date,
                                                    priority.capitalize())
                print("Задача добавлена:", result)
                break

            except ValueError as e:
                print(f"Ошибка: {e}. Пожалуйста, попробуйте снова.")

    def edit_task(self) -> None:
        """Редактировать задачу, по ID"""
        try:
            task_id = int(input("Введите ID задачи: "))
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            category = input("Введите категорию задачи: ")
            due_date = input("Введите срок(дату) выполнения задачи в формате YYYY-MM-DD: ")
            priority = input("Укажите какой приоритет присвоить задаче: ")
            edited_task = self.task_service.edit_task(task_id, title.capitalize(),
                                                      description.capitalize(),
                                                      category.capitalize(),
                                                      due_date,
                                                      priority.capitalize())
            print(edited_task)
        except ValueError:
            print("Некорректный ввод данных.")

    def edit_status(self) -> None:
        """Меняет статус задачи."""
        try:
            task_id = int(input("Введите ID задачи: "))
            status = input("Укажите какой статус присвоить задаче(не выполнена, выполнена):")
            if status in ["не выполнена", "выполнена"]:
                print(self.task_service.change_status(task_id, status.capitalize()))
            else:
                print('Пожалуйста, укажите не выполнена или выполнена.')

        except ValueError:
            print('Введен неверный формат ID.')

    def delete_task(self) -> None:
        """Удалить задачу, по ID"""
        try:
            task_id = int(input("Введите ID задачи: "))
            print(self.task_service.delete_task(task_id))
        except ValueError:
            print("Некорректный ввод ID.")
