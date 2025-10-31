import os
import pathlib
import shutil
from logger import er_logger


def zip_archive(active_path, object, ar_name) -> None:
    """Архивирует каталог в формате zip

    Args:
        active_path (Path): Текущий путь
        object (str): Архивируемый объект
        ar_name (str): Имя архива

    Raises:
        FileNotFoundError: Не существует директория или нехватает прав доступа
    """
    if "\\" in object:
        if os.path.exists(object) and os.access(object, os.X_OK) and os.path.isdir(object):
            shutil.make_archive(str(pathlib.Path(object).parents[0] / ar_name),
                                "zip", root_dir=str(pathlib.Path(object)))
            print("Архивирование завершено")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует директория {object} или нехватает прав доступа")
    else:
        object_path = active_path / object
        if os.path.exists(object_path) and os.access(object_path, os.X_OK) and os.path.isdir(object_path):
            shutil.make_archive(str(active_path / ar_name),
                                "zip", root_dir=str(object_path))
            print("Архивирование завершено")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует директория {object} или нехватает прав доступа")


def zip_unarchive(active_path, object) -> None:
    """Разархивирует каталог из формата zip

    Args:
        active_path (Path): Текущий путь
        object (str): Разархивируемый объект

    Raises:
        FileNotFoundError: Не существует директория или нехватает прав доступа
    """
    if "\\" in object:
        if os.path.exists(object) and os.access(object, os.X_OK) and pathlib.Path(object).suffix == ".zip":
            shutil.unpack_archive(
                object, pathlib.Path(object).parents[0], "zip")
            print("Извлечение завершено")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует архив {object} или нехватает прав доступа")
    else:
        object_path = active_path / object
        if os.path.exists(object_path) and os.access(object_path, os.X_OK) and pathlib.Path(object_path).suffix == ".zip":
            shutil.unpack_archive(object_path, active_path, "zip")
            print("Извлечение завершено")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует архив {object} или нехватает прав доступа")


def tar_archive(active_path, object, ar_name) -> None:
    """Архивирует каталог в формате tar

    Args:
        active_path (Path): Текущий путь
        object (str): Архивируемый объект
        ar_name (str): Имя архива

    Raises:
        FileNotFoundError: Не существует директория или нехватает прав доступа
    """
    if "\\" in object:
        if os.path.exists(object) and os.access(object, os.X_OK) and os.path.isdir(object):
            shutil.make_archive(str(pathlib.Path(object).parents[0] / ar_name),
                                "tar", root_dir=str(pathlib.Path(object)))
            print("Архивирование завершено")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует директория {object} или нехватает прав доступа")
    else:
        object_path = active_path / object
        if os.path.exists(object_path) and os.access(object_path, os.X_OK) and os.path.isdir(object_path):
            shutil.make_archive(str(active_path / ar_name),
                                "tar", root_dir=str(object_path))
            print("Архивирование завершено")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует директория {object} или нехватает прав доступа")


def tar_unarchive(active_path, object) -> None:
    """Разархивирует каталог из формата tar

    Args:
        active_path (Path): Текущий путь
        object (str): Разархивируемый объект

    Raises:
        FileNotFoundError: Не существует директория или нехватает прав доступа
    """
    if "\\" in object:
        if os.path.exists(object) and os.access(object, os.X_OK) and pathlib.Path(object).suffix == ".tar":
            shutil.unpack_archive(
                object, pathlib.Path(object).parents[0], "tar")
            print("Извлечение завершено")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует архив {object} или нехватает прав доступа")
    else:
        object_path = active_path / object
        if os.path.exists(object_path) and os.access(object_path, os.X_OK) and pathlib.Path(object_path).suffix == ".tar":
            shutil.unpack_archive(object_path, active_path, "tar")
            print("Извлечение завершено")
        else:
            er_logger.error(f"{object} does not exist or not enough rules")
            raise FileNotFoundError(
                f"Не существует архив {object} или нехватает прав доступа")
