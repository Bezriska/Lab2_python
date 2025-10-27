import os
import pathlib
from datetime import datetime
import shutil
from shutil import make_archive
import stat
from logger import er_logger
import zlib


def if_ls(active_path) -> list:
    output = "\n".join(os.listdir(active_path))
    return output


def if_ls_l(active_path) -> list:
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


def chdir_down(active_path, user_input):
    if "\\" not in user_input:
        if os.access(active_path, os.X_OK):
            output = pathlib.Path(active_path).joinpath(user_input)
        else:
            # Рэйзим ошибку
            print("Недостаточно прав доступа для выполнения команды")
            er_logger.error(
                "Not enough rules")
    else:
        if os.access(user_input, os.X_OK):
            output = pathlib.Path(user_input)
        else:
            # Рэйзим ошибку
            print("Недостаточно прав доступа для выполнения команды")
            er_logger.error(
                "Not enough rules")
    return output


def chdir_up(active_path):
    if os.access(active_path, os.X_OK):
        output = pathlib.Path(active_path).parents[0]
        return output
    else:
        # Рэйзим ошибку
        print("Недостаточно прав доступа для выполнения команды")
        er_logger.error(
            "Недостаточно прав доступа для выоплнения этой команды")


def home_dir():
    if os.access(pathlib.Path.home(), os.X_OK):
        output = pathlib.Path.home()
        return output
    else:
        # Рэйзим ошибку
        print("Недостаточно прав доступа для выполнения команды")
        er_logger.error(
            "Недостаточно прав доступа для выоплнения этой команды")


def read_file(active_path, object):
    if "\\" not in object:
        if os.path.isfile(active_path / object) and pathlib.Path(active_path / object).suffix == ".txt":
            if os.access(active_path, os.R_OK):
                new_path = active_path / object
                with open(new_path, "r") as file:
                    for line in file:
                        print(line.strip())
            else:
                # Рэйзим ошибку
                print("Недостаточно прав доступа для выполнения команды")
                er_logger.error(
                    "Недостаточно прав доступа для выоплнения этой команды")
        else:
            # Рэйзим ошибку
            print("Невозможно прочитать этот тип объекта")
            er_logger.error(
                "Can not read this object type")
    else:
        if os.path.isfile(object) and pathlib.Path(object).suffix == ".txt":
            if os.access(object, os.R_OK):
                object = pathlib.Path(object)
                with open(object, "r") as file:
                    for line in file:
                        print(line.strip())
            else:
                # Рэйзим ошибку
                print("Недостаточно прав доступа для выполнения команды")
                er_logger.error(
                    "Недостаточно прав доступа для выоплнения этой команды")
        else:
            # Рэйзим ошибку
            print("Невозможно прочитать этот тип объекта")
            er_logger.error(
                "Can not read this object type")


def copy(active_path, object, path):
    if "\\" not in object and "\\" in path:
        object_path = active_path / object
        if os.path.exists(object_path) and os.path.isfile(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(path) and os.path.isdir(path):
                shutil.copy(object_path, path)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {path}")
                er_logger.error(f"Не существует директория {path}")
        else:
            print(f"Не существует файл {object} или недостаточно прав доступа")
            er_logger.error(
                f"Не существует файл {object} или недостаточно прав доступа")
    elif "\\" not in object and "\\" not in path:
        object_path = active_path / object
        new_path = active_path / path
        if os.path.exists(object_path) and os.path.isfile(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.copy(object_path, new_path)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {new_path}")
                er_logger.error(f"{new_path} is not a directory")
        else:
            print(f"Не существует файл {object} или недостаточно прав доступа")
            er_logger.error(
                f"Не существует файл {object} или недостаточно прав доступа")
    elif "\\" in object and "\\" not in path:
        new_path = active_path / path
        if os.path.exists(object) and os.path.isfile(object) and os.access(object, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.copy(object, new_path)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {new_path}")
                er_logger.error(f"{new_path} is not a directory")
        else:
            print(f"Не существует файл {object} или недостаточно прав доступа")
            er_logger.error(
                f"{object} does not exist or not enough rules")
    elif "\\" in object and "\\" in path:
        if os.path.exists(object) and os.path.isfile(object) and os.access(object, os.X_OK):
            if os.path.exists(path) and os.path.isdir(path):
                shutil.copy(object, path)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {path}")
                er_logger.error(f"{path} is not a directory")
        else:
            print(f"Не существует файл {object} или недостаточно прав доступа")
            er_logger.error(
                f"{object} does not exist or not enough rules")


def copy_tree(active_path, object, path):
    if "\\" not in object and "\\" in path:
        object_path = active_path / object
        if os.path.exists(object_path) and os.path.isdir(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(path) and os.path.isdir(path):
                shutil.copytree(object_path, pathlib.Path(
                    path) / object, copy_function=shutil.copy2)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {path}")
                er_logger.error(f"Не существует директория {path}")
        else:
            print(f"Не существует файл {object} или недостаточно прав доступа")
            er_logger.error(
                f"Не существует файл {object} или недостаточно прав доступа")
    elif "\\" not in object and "\\" not in path:
        object_path = active_path / object
        new_path = active_path / path
        if os.path.exists(object_path) and os.path.isdir(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.copytree(object_path, pathlib.Path(new_path) / object,
                                copy_function=shutil.copy2)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {new_path}")
                er_logger.error(f"{new_path} is not a directory")
        else:
            print(f"Не существует файл {object} или недостаточно прав доступа")
            er_logger.error(
                f"Не существует файл {object} или недостаточно прав доступа")
    elif "\\" in object and "\\" not in path:
        new_path = active_path / path
        if os.path.exists(object) and os.path.isdir(object) and os.access(object, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.copytree(object, pathlib.Path(
                    new_path) / pathlib.Path(object).name, copy_function=shutil.copy2)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {new_path}")
                er_logger.error(f"{new_path} is not a directory")
        else:
            print(f"Не существует файл {object} или недостаточно прав доступа")
            er_logger.error(
                f"{object} does not exist or not enough rules")
    elif "\\" in object and "\\" in path:
        if os.path.exists(object) and os.path.isdir(object) and os.access(object, os.X_OK):
            if os.path.exists(path) and os.path.isdir(path):
                shutil.copytree(object, pathlib.Path(
                    path) / pathlib.Path(object).name, copy_function=shutil.copy2)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {path}")
                er_logger.error(f"{path} is not a directory")
        else:
            print(f"Не существует файл {object} или недостаточно прав доступа")
            er_logger.error(
                f"{object} does not exist or not enough rules")


def move(active_path, object, target):
    object_path = active_path / object
    if "\\" not in object and "\\" in target:
        if os.path.exists(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(target) and os.path.isdir(target):
                shutil.move(object_path, pathlib.Path(
                    target) / object)
                print("Перемещение завершено")
            else:
                print(f"Не существует директория {target}")
                er_logger.error(f"Не существует директория {target}")
        else:
            print(
                f"Не существует объект {object} или недостаточно прав доступа")
            er_logger.error(
                f"Не существует объект {object} или недостаточно прав доступа")
    elif "\\" not in object and "\\" not in target:
        new_path = active_path / target
        if os.path.exists(object_path) and os.access(object_path, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.move(object_path, new_path / object)
                print("Перемещение завершено")
            else:
                print(f"Не существует директория {new_path}")
                er_logger.error(f"Не существует директория {new_path}")
        else:
            print(
                f"Не существует объект {object} или недостаточно прав доступа")
            er_logger.error(
                f"Не существует объект {object} или недостаточно прав доступа")
    elif "\\" in object and "\\" not in target:
        new_path = active_path / target
        if os.path.exists(object) and os.access(object, os.X_OK):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.move(object, pathlib.Path(
                    new_path) / pathlib.Path(object).name)
                print("Перемещение завершено")
            else:
                print(f"Не существует директория {new_path}")
                er_logger.error(f"{new_path} is not a directory")
        else:
            print(f"Не существует файл {object} или недостаточно прав доступа")
            er_logger.error(
                f"{object} does not exist or not enough rules")
    elif "\\" in object and "\\" in target:
        if os.path.exists(object) and os.access(object, os.X_OK):
            if os.path.exists(target) and os.path.isdir(target):
                shutil.move(object, pathlib.Path(
                    target) / pathlib.Path(object).name)
                print("Перемещение завершено")
            else:
                print(f"Не существует директория {target}")
                er_logger.error(f"{target} is not a directory")
        else:
            print(f"Не существует файл {object} или недостаточно прав доступа")
            er_logger.error(
                f"{object} does not exist or not enough rules")


def remove(active_path, object):
    if "\\" in object:
        conf = input("Для подтверждения введите y/n: ")
        if conf == "y" and os.access(object, os.X_OK):
            if os.path.exists(object) and os.path.isfile(object):
                os.remove(object)
                print("Объект удален")
            else:
                print(f"Не существует объект {object_path}")
        else:
            print("Удаление отменено или недостаточно прав доступа")
    else:
        conf = input("Для подтверждения введите y/n: ")
        object_path = active_path / object
        if conf == "y" and os.access(object_path, os.X_OK):
            if os.path.exists(object_path) and os.path.isfile(object_path):
                os.remove(object_path)
                print("Файл удален")
            else:
                print(f"Не существует файл {object_path}")
        else:
            print("Удаление отменено или недостаточно прав доступа")


def remove_tree(active_path, object):
    if "\\" in object:
        conf = input("Для подтверждения введите y/n: ")
        if conf == "y" and os.access(object, os.X_OK):
            if object != pathlib.Path.home():
                if pathlib.Path(object).name not in str(active_path):
                    if os.path.exists(object) and os.path.isdir(object):
                        shutil.rmtree(object)
                        print("Файл удален")
                    else:
                        # Рэйзим ошибку
                        print(f"Не существует файл {object_path}")
                else:
                    # Рэйзим ошибку
                    print("Нельзя удалить родительский каталог")
            else:
                # Рэйзим ошибку
                print("Нельзя удалить корневой каталог")
        else:
            print("Удаление отменено или недостаточно прав доступа")
    else:
        conf = input("Для подтверждения введите y/n: ")
        object_path = active_path / object
        if conf == "y" and os.access(object_path, os.X_OK):
            if object_path != pathlib.Path.home():
                if object not in str(active_path):
                    if os.path.exists(object_path) and os.path.isdir(object_path):
                        shutil.rmtree(object_path)
                        print("Файл удален")
                    else:
                        # Рэйзим ошибку
                        print(f"Не существует файл {object_path}")
                else:
                    # Рэйзим ошибку
                    print("Нельзя удалить родительский каталог")
            else:
                # Рэйзим ошибку
                print("Нельзя удалить корневой каталог")
        else:
            print("Удаление отменено или недостаточно прав доступа")


def zip_archive(active_path, object, ar_name):
    if "\\" in object:
        if os.path.exists(object) and os.access(object, os.X_OK) and os.path.isdir(object):
            make_archive(ar_name, "zip", root_dir=str(object))
            print("Архивирование завершено")
        else:
            # Рэйзим ошибку
            print(
                f"Не существует директория {object} или нехватает прав доступа")
            er_logger.error(f"{object} does not exist or not enough rules")
    else:
        object_path = active_path / object
        if os.path.exists(object_path) and os.access(object_path, os.X_OK) and os.path.isdir(object_path):
            make_archive(ar_name, "zip", root_dir=str(object_path))
            print("Архивирование завершено")
        else:
            # Рэйзим ошибку
            print(
                f"Не существует директория {object} или нехватает прав доступа")
            er_logger.error(f"{object} does not exist or not enough rules")
