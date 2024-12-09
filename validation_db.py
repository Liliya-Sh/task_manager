from datetime import datetime


def is_valid_due_date(due_date_str) -> str:
    """Проверяет, срок выполнения задачи."""
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        return str(due_date)
    except ValueError:
        print('Введен неверный формат срока выполнения задачи. Пожалуйста, введите в формате YYYY-MM-DD.')


def is_valid_get_priority(priority) -> str :
    """Проверяет,что приоритет задачи указан верно"""
    try:
        if priority.lower() in ["низкий", "средний", "высокий"]:
            return priority
        else:
            return 'Пожалуйста, укажите: низкий, средний, высокий'
    except ValueError:
        print('Введен неверный формат приоритета.')
