import os
import pathlib
from datetime import datetime
import stat
from logger import er_logger


def if_ls(active_path) -> list:
    """Показывает список объектов в директории

    Args:
        active_path (Path): Текущий путь

    Returns:
        list: Список объектов в директории
    """
    output = "\n".join(os.listdir(active_path))
    return output


def if_ls_l(active_path) -> list:
    """Показывает список объектов с подробными данными в директории

    Args:
        active_path (Path): Текущий путь

    Returns:
        list: Список объектов с данными в директории
    """
    output = []
    for object in os.listdir(active_path):
        path = active_path / object
        if pathlib.Path(path).is_file():
            lst_file = [pathlib.Path(path).name,
                        str(os.stat(pathlib.Path(path)).st_size) + " байт",
                        datetime.fromtimestamp(
                            os.stat(pathlib.Path(path)).st_ctime).strftime("%d.%m.%Y"),
                        str(stat.filemode(os.stat(pathlib.Path(path)).st_mode))]
            output.append(lst_file)
        else:
            lst_lib = [pathlib.Path(path).name, "папка"]
            output.append(lst_lib)
    return output


def chdir_down(active_path, user_input) -> pathlib.Path:
    """Смена директории на ввод пользователя

    Args:
        active_path (Path): Текущий путь
        user_input (list): Ввод пользователя, разбитый на токены.

    Raises:
        PermissionError: Недостаточно прав доступа для выполнения команды

    Returns:
        Path: Новый путь
    """
    if "\\" not in user_input:
        if os.access(active_path, os.X_OK):
            output = pathlib.Path(active_path).joinpath(user_input)
        else:
            er_logger.error("Not enough rules")
            raise PermissionError(
                "Недостаточно прав доступа для выполнения команды")
    else:
        if os.access(user_input, os.X_OK):
            output = pathlib.Path(user_input)
        else:
            er_logger.error("Not enough rules")
            raise PermissionError(
                "Недостаточно прав доступа для выполнения команды")
    return output


def chdir_up(active_path) -> pathlib.Path:
    """Переход в родительскую директорию от текущей

    Args:
        active_path (Path): Текущий путь

    Raises:
        PermissionError: Недостаточно прав доступа для выполнения команды

    Returns:
        Path: Новый путь
    """
    if os.access(active_path, os.X_OK):
        output = pathlib.Path(active_path).parents[0]
        return output
    else:
        er_logger.error("Not enough rules")
        raise PermissionError(
            "Недостаточно прав доступа для выполнения команды")


def home_dir() -> pathlib.Path:
    """Переходит в домашнюю директорию

    Raises:
        PermissionError: Недостаточно прав доступа для выполнения команды

    Returns:
        Path: Новый путь
    """
    if os.access(pathlib.Path.home(), os.X_OK):
        output = pathlib.Path.home()
        return output
    else:
        er_logger.error("Not enough rules")
        raise PermissionError(
            "Недостаточно прав доступа для выполнения команды")
