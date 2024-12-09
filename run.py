from console_interfase import ConsoleInterface
from services import TaskService


if __name__ == "__main__":
    task_service = TaskService()
    console_interface = ConsoleInterface(task_service)
    console_interface.menu_app()
