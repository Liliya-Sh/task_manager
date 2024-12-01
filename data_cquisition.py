from datetime import datetime


class ReceivedData:
    """Данные, которые вводит пользователь"""

    @staticmethod
    def _get_input(prompt: str, min_length: int, max_length: int) -> str:
        """Запрашивает ввод и проверяет его длину."""
        while True:
            user_input = input(prompt).strip()
            if len(user_input) < min_length or len(user_input) > max_length:
                print(f'Ввод некорректен. Пожалуйста, введите значение от {min_length} до {max_length} символов.')
            else:
                return user_input

    def get_title(self) -> str:
        """Запрашивает название задачи."""
        return self._get_input("Введите название задачи: ", 2, 70)

    def get_description(self) -> str:
        """Запрашивает описание задачи."""
        return self._get_input("Введите описание задачи: ", 2, 250)

    def get_category(self) -> str:
        """Запрашивает категорию задачи."""
        return self._get_input("Введите категорию задачи: ", 2, 25)

    def get_word(self) -> str:
        """Запрашивает ключевое слово."""
        return self._get_input("Введите ключевое слово: ", 2, 10)

    @staticmethod
    def get_due_date() -> str:
        """Запрашивает срок выполнения задачи."""
        while True:
            due_date_str = input("Введите срок(дату) выполнения задачи в формате YYYY-MM-DD: ")
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                return str(due_date)
            except ValueError:
                print('Введен неверный формат срока выполнения задачи. Пожалуйста, введите в формате YYYY-MM-DD.')

    @staticmethod
    def get_id() -> int:
        """Запрашивает ID и проверяет его корректность."""
        while True:
            try:
                task_id = int(input("Введите ID задачи: "))
                return task_id
            except ValueError:
                print('Введен неверный формат ID. Пожалуйста, введите целое число.')

    @staticmethod
    def get_priority():
        """Запрашивает приоритет задачи и проверяет его корректность."""
        while True:
            try:
                priority = int(input("Укажите какой приоритет присвоить задаче(низкий - 1, средний - 2, высокий - 3):"))
                if priority == 1:
                    priority_task = 'низкий'
                    return priority_task
                elif priority == 2:
                    priority_task = 'средний'
                    return priority_task
                elif priority == 3:
                    priority_task = 'высокий'
                    return priority_task
                else:
                    print('Пожалуйста, укажите 1, 2 или 3.')
            except ValueError:
                print('Введен неверный формат приоритета. Укажите 1, 2 или 3.')

    @staticmethod
    def get_status():
        """Запрашивает статус задачи и проверяет его корректность."""
        while True:
            try:
                status = int(input("Укажите какой статус присвоить задаче(не выполнена - 1, выполнена - 2):"))
                if status == 1:
                    status_book = 'не выполнена'
                    return status_book
                elif status == 2:
                    status_book = 'выполнена'
                    return status_book
                else:
                    print('Пожалуйста, укажите 1 или 2.')

            except ValueError:
                print('Введен неверный формат ID. Укажите 1 или 2.')

    @staticmethod
    def get_criterion() -> int:
        """Запрашивает критерий поиска задачи."""
        while True:
            try:
                criterion = int(input("Введите критерий поиска (категориям - 1, статусу - 2, ключевым словам - 3): "))
                if criterion in (1, 2, 3):
                    return criterion
                else:
                    print('Пожалуйста, укажите 1, 2 или 3.')
            except ValueError:
                print('Введен неверный формат критерия. Укажите 1, 2 или 3.')
