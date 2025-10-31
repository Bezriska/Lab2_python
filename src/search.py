import os
import pathlib
import re
from logger import er_logger


def grep(pattern, object, flag1=None, flag2=None) -> None:
    """Выполняет поиск\\рекурсивный поиск внутри текстовых файлов по шаблону пользователя

    Args:
        pattern (str): Шаблон поиска
        object (str): объект, где производится поиск
        flag1 (str, optional): флаг -r (рекурсивный поиск по подкаталогам). По умолчанию принимает None.
        flag2 (str, optional): флаг -i (поиск без учеа регистра). По умолчанию принимает None.

    Raises:
        FileNotFoundError: расширение не .txt
        FileNotFoundError: не является директорией
        PermissionError: Недостаточно прав доступа
        FileNotFoundError: объект не существует
    """
    if os.path.exists(object):
        if os.access(object, os.X_OK):
            object_path = pathlib.Path(object)
            if flag1 == None and flag2 == None:
                regex = re.compile(pattern)
                if pathlib.Path(object_path).suffix == ".txt":
                    with open(object_path, "r", encoding="utf-8", errors="replace") as f:
                        for line_num, line in enumerate(f, 1):
                            if regex.search(line):
                                print(
                                    f"Имя файла: {str(object_path)}\nНомер строки: {line_num}\nСтрока: {line.rstrip()}\n")
                else:
                    er_logger.error(f"{str(object_path)} is not a .txt")
                    raise FileNotFoundError(
                        f"{str(object_path)} расширение не .txt")
            elif flag1 == None and flag2 == "-i":
                regex = re.compile(pattern, re.IGNORECASE)
                if pathlib.Path(object_path).suffix == ".txt":
                    with open(object_path, "r", encoding="utf-8", errors="replace") as f:
                        for line_num, line in enumerate(f, 1):
                            if regex.search(line):
                                print(
                                    f"Имя файла: {str(object_path)}\nНомер строки: {line_num}\nСтрока: {line.rstrip()}\n")
                else:
                    er_logger.error(f"{str(object_path)} is not a .txt")
                    raise FileNotFoundError(
                        f"{str(object_path)} расширение не .txt")
            elif flag1 == "-r" and flag2 == None:
                if os.path.isdir(object_path):
                    regex = re.compile(pattern)
                    files = collect_files(object_path)
                    for path in files:
                        with open(path, "r", encoding="utf-8", errors="replace") as f:
                            for line_num, line in enumerate(f, 1):
                                if regex.search(line):
                                    print(
                                        f"Имя файла: {str(path)}\nНомер строки: {line_num}\nСтрока: {line.rstrip()}\n")
                else:
                    er_logger.error(f"{object_path} is not a directory")
                    raise FileNotFoundError(
                        f"{object_path} не является директорией")
            elif flag1 == "-r" and flag2 == "-i":
                if os.path.isdir(object_path):
                    regex = re.compile(pattern, re.IGNORECASE)
                    files = collect_files(object_path)
                    for path in files:
                        with open(path, "r", encoding="utf-8", errors="replace") as f:
                            for line_num, line in enumerate(f, 1):
                                if regex.search(line):
                                    print(
                                        f"Имя файла: {str(path)}\nНомер строки: {line_num}\nСтрока: {line.rstrip()}\n")
                else:
                    er_logger.error(f"{object_path} is not a directory")
                    raise FileNotFoundError(
                        f"{object_path} не является директорией")
        else:
            er_logger.error("Not enough rules")
            raise PermissionError("Недостаточно прав доступа")
    else:
        er_logger.error(f"{object} does not exist")
        raise FileNotFoundError(f"{object} не существует")


def collect_files(target) -> list:
    """Рекурсивно собирает файлы типа .txt из каталога и подкаталогов в список

    Args:
        target (str): Каталог для сбора

    Returns:
        list: список файлов
    """
    files = []
    target_path = pathlib.Path(target)
    for obj in target_path.rglob("*.txt"):
        files.append(obj)
    return files
