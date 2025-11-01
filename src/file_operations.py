import os
import pathlib
import shutil
from logger import er_logger


def read_file(active_path, object) -> None:
    """Выводит содержимое текстового файла

    Args:
        active_path (Path): Текущий путь
        object (str): Файл, который будет прочитан

    Raises:
        PermissionError: Недостаточно прав доступа для выполнения команды
        ValueError: "Невозможно прочитать этот тип объекта"
    """
    if "\\" not in object:
        if os.path.isfile(active_path / object) and pathlib.Path(active_path / object).suffix == ".txt":
            if os.access(active_path, os.R_OK):
                new_path = active_path / object
                with open(new_path, "r") as file:
                    for line in file:
                        print(line.strip())
            else:
                er_logger.error("Not enough rules")
                raise PermissionError(
                    "Недостаточно прав доступа для выполнения команды")
        else:
            er_logger.error("Can not read this object type")
            raise ValueError("Невозможно прочитать этот тип объекта")
    else:
        if os.path.isfile(object) and pathlib.Path(object).suffix == ".txt":
            if os.access(object, os.R_OK):
                object = pathlib.Path(object)
                with open(object, "r") as file:
                    for line in file:
                        print(line.strip())
            else:
                er_logger.error("Not enough rules")
                raise PermissionError(
                    "Недостаточно прав доступа для выполнения команды")
        else:
            er_logger.error("Can not read this object type")
            raise ValueError("Невозможно прочитать этот тип объекта")


def copy(active_path, object, path) -> None:
    """Копирование файла в текущую\\новую директорию

    Args:
        active_path (Path): Текущий путь
        object (str): Копируемый файл
        path (str): Путь к файлу (отн\\абс)

    Raises:
        FileNotFoundError: Не существует директория
        FileNotFoundError: Не существует файл  или недостаточно прав доступа
    """
    if "\\" not in object and "\\" in path:
        object_path = active_path / object
        if os.path.exists(object_path) and os.path.isfile(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(path) and os.path.isdir(path):
                shutil.copy(object_path, path)
                print("Копирование завершено")
            else:
                er_logger.error(f"Не существует директория {path}")
                raise FileNotFoundError(f"Не существует директория {path}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует файл {object} или недостаточно прав доступа")
    elif "\\" not in object and "\\" not in path:
        object_path = active_path / object
        new_path = active_path / path
        if os.path.exists(object_path) and os.path.isfile(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.copy(object_path, new_path)
                print("Копирование завершено")
            else:
                er_logger.error(f"{new_path} is not a directory")
                raise FileNotFoundError(f"Не существует директория {new_path}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует файл {object} или недостаточно прав доступа")
    elif "\\" in object and "\\" not in path:
        new_path = active_path / path
        if os.path.exists(object) and os.path.isfile(object) and os.access(object, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.copy(object, new_path)
                print("Копирование завершено")
            else:
                er_logger.error(f"{new_path} is not a directory")
                raise FileNotFoundError(f"Не существует директория {new_path}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует файл {object} или недостаточно прав доступа")
    elif "\\" in object and "\\" in path:
        if os.path.exists(object) and os.path.isfile(object) and os.access(object, os.X_OK):
            if os.path.exists(path) and os.path.isdir(path):
                shutil.copy(object, path)
                print("Копирование завершено")
            else:
                er_logger.error(f"{path} is not a directory")
                raise FileNotFoundError(f"Не существует директория {path}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует файл {object} или недостаточно прав доступа")


def copy_tree(active_path, object, path) -> None:
    """Копирование каталога рекурсивно в текущую\\новую директорию

    Args:
        active_path (Path): Текущий путь
        object (str): Копируемый файл
        path (str): Путь к файлу (отн\\абс)

    Raises:
        FileNotFoundError: Не существует директория
        FileNotFoundError: Не существует файл  или недостаточно прав доступа
    """
    if "\\" not in object and "\\" in path:
        object_path = active_path / object
        if os.path.exists(object_path) and os.path.isdir(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(path) and os.path.isdir(path):
                shutil.copytree(object_path, pathlib.Path(
                    path) / object, copy_function=shutil.copy2)
                print("Копирование завершено")
            else:
                er_logger.error(f"{path} is not a directory")
                raise FileNotFoundError(f"Не существует директория {path}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует файл {object} или недостаточно прав доступа")
    elif "\\" not in object and "\\" not in path:
        object_path = active_path / object
        new_path = active_path / path
        if os.path.exists(object_path) and os.path.isdir(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.copytree(object_path, pathlib.Path(
                    new_path) / object, copy_function=shutil.copy2)
                print("Копирование завершено")
            else:
                er_logger.error(f"{new_path} is not a directory")
                raise FileNotFoundError(f"Не существует директория {new_path}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует файл {object} или недостаточно прав доступа")
    elif "\\" in object and "\\" not in path:
        new_path = active_path / path
        if os.path.exists(object) and os.path.isdir(object) and os.access(object, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.copytree(object, pathlib.Path(
                    new_path) / pathlib.Path(object).name, copy_function=shutil.copy2)
                print("Копирование завершено")
            else:
                er_logger.error(f"{new_path} is not a directory")
                raise FileNotFoundError(f"Не существует директория {new_path}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует файл {object} или недостаточно прав доступа")
    elif "\\" in object and "\\" in path:
        if os.path.exists(object) and os.path.isdir(object) and os.access(object, os.X_OK):
            if os.path.exists(path) and os.path.isdir(path):
                shutil.copytree(object, pathlib.Path(
                    path) / pathlib.Path(object).name, copy_function=shutil.copy2)
                print("Копирование завершено")
            else:
                er_logger.error(f"{path} is not a directory")
                raise FileNotFoundError(f"Не существует директория {path}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует файл {object} или недостаточно прав доступа")


def move(active_path, object, target) -> None:
    """Перемещение объекта в новую директорию

    Args:
        active_path (Path): Текущий путь
        object (str): Перемещаемый объект
        target (str): Куда переместить объект (отн\\абс)

    Raises:
        FileNotFoundError: Не существует директория
        FileNotFoundError: Не существует объект или недостаточно прав доступа
    """
    object_path = active_path / object
    if "\\" not in object and "\\" in target:
        if os.path.exists(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(target) and os.path.isdir(target):
                shutil.move(object_path, pathlib.Path(target) / object)
                print("Перемещение завершено")
            else:
                er_logger.error(f"{target} is not a directory")
                raise FileNotFoundError(f"Не существует директория {target}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует объект {object} или недостаточно прав доступа")
    elif "\\" not in object and "\\" not in target:
        new_path = active_path / target
        if os.path.exists(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.move(object_path, new_path / object)
                print("Перемещение завершено")
            else:
                er_logger.error(f"{new_path} is not a directory")
                raise FileNotFoundError(f"Не существует директория {new_path}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует объект {object} или недостаточно прав доступа")
    elif "\\" in object and "\\" not in target:
        new_path = active_path / target
        if os.path.exists(object) and os.access(object, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.move(object, pathlib.Path(
                    new_path) / pathlib.Path(object).name)
                print("Перемещение завершено")
            else:
                er_logger.error(f"{new_path} is not a directory")
                raise FileNotFoundError(f"Не существует директория {new_path}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует файл {object} или недостаточно прав доступа")
    elif "\\" in object and "\\" in target:
        if os.path.exists(object) and os.access(object, os.X_OK):
            if os.path.exists(target) and os.path.isdir(target):
                shutil.move(object, pathlib.Path(
                    target) / pathlib.Path(object).name)
                print("Перемещение завершено")
            else:
                er_logger.error(f"{target} is not a directory")
                raise FileNotFoundError(f"Не существует директория {target}")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует файл {object} или недостаточно прав доступа")


def remove(active_path, object) -> None:
    """Удаление объекта в .trash (с возможностью восстановления)

    Args:
        active_path (Path): Текущий путь
        object (str): Удаляемый объект

    Raises:
        FileNotFoundError: Не существует объект
        PermissionError: Удаление отменено или недостаточно прав доступа
    """
    trash_dir = active_path / ".trash"
    if not trash_dir.exists():
        trash_dir.mkdir()

    if "\\" in object:
        conf = input("Для подтверждения введите y/n: ")
        if conf == "y" and os.access(object, os.X_OK):
            if os.path.exists(object) and os.path.isfile(object):
                file_name = pathlib.Path(object).name
                trash_destination = trash_dir / file_name
                counter = 1
                while trash_destination.exists():
                    name_parts = pathlib.Path(
                        object).stem, pathlib.Path(object).suffix
                    trash_destination = trash_dir / \
                        f"{name_parts[0]}_{counter}{name_parts[1]}"
                    counter += 1
                shutil.move(object, str(trash_destination))
                print(f"Объект перемещен в .trash: {file_name}")
            else:
                er_logger.error(f"{object} does not exist")
                raise FileNotFoundError(f"Не существует объект {object}")
        else:
            er_logger.error("Deleting canceled or not enough rules")
            raise PermissionError(
                "Удаление отменено или недостаточно прав доступа")
    else:
        conf = input("Для подтверждения введите y/n: ")
        object_path = active_path / object
        if conf == "y" and os.access(object_path, os.X_OK):
            if os.path.exists(object_path) and os.path.isfile(object_path):
                trash_destination = trash_dir / object
                counter = 1
                while trash_destination.exists():
                    name_parts = pathlib.Path(
                        object).stem, pathlib.Path(object).suffix
                    trash_destination = trash_dir / \
                        f"{name_parts[0]}_{counter}{name_parts[1]}"
                    counter += 1
                shutil.move(str(object_path), str(trash_destination))
                print(f"Файл перемещен в .trash: {object}")
            else:
                er_logger.error(f"{object_path} does not exist")
                raise FileNotFoundError(f"Не существует файл {object_path}")
        else:
            er_logger.error("Deleting canceled or not enough rules")
            raise PermissionError(
                "Удаление отменено или недостаточно прав доступа")


def remove_tree(active_path, object) -> None:
    """Рекурсивное удаление каталога в .trash (с возможностью восстановления)

    Args:
        active_path (Path): _Текущий путь
        object (str): Перемещаемый объект

    Raises:
        FileNotFoundError: Не существует файл
        ValueError: Нельзя удалить родительский каталог
        ValueError: Нельзя удалить корневой каталог
        PermissionError: Удаление отменено или недостаточно прав доступа
    """
    trash_dir = active_path / ".trash"
    if not trash_dir.exists():
        trash_dir.mkdir()
    if "\\" in object:
        conf = input("Для подтверждения введите y/n: ")
        if conf == "y" and os.access(object, os.X_OK):
            if object != str(pathlib.Path.home()):
                if pathlib.Path(object).name not in str(active_path):
                    if os.path.exists(object) and os.path.isdir(object):
                        dir_name = pathlib.Path(object).name
                        trash_destination = trash_dir / dir_name
                        counter = 1
                        while trash_destination.exists():
                            trash_destination = trash_dir / \
                                f"{dir_name}_{counter}"
                            counter += 1
                        shutil.move(object, str(trash_destination))
                        print(f"Каталог перемещен в .trash: {dir_name}")
                    else:
                        er_logger.error(f"{object} does not exist")
                        raise FileNotFoundError(f"Не существует файл {object}")
                else:
                    er_logger.error("Can not delete parent directory")
                    raise ValueError("Нельзя удалить родительский каталог")
            else:
                er_logger.error("Can not delete home directory")
                raise ValueError("Нельзя удалить домашний каталог")
        else:
            er_logger.error("Deleting canceled or not enough rules")
            raise PermissionError(
                "Удаление отменено или недостаточно прав доступа")
    else:
        conf = input("Для подтверждения введите y/n: ")
        object_path = active_path / object
        if conf == "y" and os.access(object_path, os.X_OK):
            if object_path != pathlib.Path.home():
                if object not in str(active_path):
                    if os.path.exists(object_path) and os.path.isdir(object_path):
                        trash_destination = trash_dir / object
                        counter = 1
                        while trash_destination.exists():
                            trash_destination = trash_dir / \
                                f"{object}_{counter}"
                            counter += 1
                        shutil.move(str(object_path), str(trash_destination))
                        print(f"Каталог перемещен в .trash: {object}")
                    else:
                        er_logger.error(f"{object_path} does not exist")
                        raise FileNotFoundError(
                            f"Не существует файл {object_path}")
                else:
                    er_logger.error("Can not delete parent directory")
                    raise ValueError("Нельзя удалить родительский каталог")
            else:
                er_logger.error("Can not delete home directory")
                raise ValueError("Нельзя удалить домашний каталог")
        else:
            er_logger.error("Deleting canceled or not enough rules")
            raise PermissionError(
                "Удаление отменено или недостаточно прав доступа")
