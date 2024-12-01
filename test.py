import unittest


from app import ManagerTasks


class TestTasksManager(unittest.TestCase):
    """Тесты на для проверки работы функций"""

    def setUp(self) -> None:
        self.manager_task = ManagerTasks()

    def tearDown(self):
        pass

    def test_add_task(self):
        """Тестируем функцию add_task(добавляем новую задачу)"""
        new_task = ('\nID: 3'
                    '\nНазвание: День рождение'
                    '\nОписание: Поздравить подругу'
                    '\nКатегория: Личное'
                    '\nСрок: 2024-11-05'
                    '\nПриоритет: Средний'
                    '\nСтатус: Не выполнена'
                    )

        actual_result = ManagerTasks().add_task('День рождение', 'Поздравить подругу', 'Личное',
                                                '2024-11-05', 'Средний')
        self.assertEqual(actual_result, new_task)

    def test_search_task_category(self):
        """Тестируем функцию search_task(поиск задачи по категориям)"""
        task = ('\nID: 3'
                '\nНазвание: День рождение'
                '\nОписание: Поздравить подругу'
                '\nКатегория: Личное'
                '\nСрок: 2024-11-05'
                '\nПриоритет: Средний'
                '\nСтатус: Не выполнена')

        actual_result = self.manager_task.search_task(1, 'личное')
        self.assertEqual(actual_result, task)

    def test_search_book_status(self):
        """Тестируем функцию search_task(поиск задачи по статусу)"""
        task = ('\nID: 1'
                '\nНазвание: Изучить основы FastAPI'
                '\nОписание: Пройти документацию по FastAPI и создать простой проект'
                '\nКатегория: Обучение'
                '\nСрок: 2024-11-30'
                '\nПриоритет: Высокий'
                '\nСтатус: Не выполнена\n'
                '\nID: 3'
                '\nНазвание: День рождение'
                '\nОписание: Поздравить подругу'
                '\nКатегория: Личное'
                '\nСрок: 2024-11-05'
                '\nПриоритет: Средний'
                '\nСтатус: Не выполнена')

        actual_result = self.manager_task.search_task(2, 'не выполнена')
        self.assertEqual(actual_result, task)

    def test_search_book_word(self):
        """Тестируем функцию search_task(поиск задачи по ключевому слову)"""
        task = ('\nID: 1'
                '\nНазвание: Изучить основы FastAPI'
                '\nОписание: Пройти документацию по FastAPI и создать простой проект'
                '\nКатегория: Обучение'
                '\nСрок: 2024-11-30'
                '\nПриоритет: Высокий'
                '\nСтатус: Не выполнена')

        actual_result = self.manager_task.search_task(3, 'FastAPI')
        self.assertEqual(actual_result, task)

    def test_delete_task(self):
        """Тестируем функцию delete_task(удаляет задачу по ID)"""
        del_task = 'Задача с ID 2 была удалена.'

        actual_result = ManagerTasks().delete_task(2)
        self.assertEqual(actual_result, del_task)


if __name__ == '__main__':
    unittest.main()
