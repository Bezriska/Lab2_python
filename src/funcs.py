import os
import pathlib
from datetime import datetime, timezone
import shutil


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
                        str(os.stat(pathlib.Path(path)).st_mode)]
            output.append(lst_file)
        else:
            lst_lib = [pathlib.Path(path).name, "папка"]
            output.append(lst_lib)
    return output


def chdir_down(active_path, user_input):
    new_object = list(map(str, user_input.split()))
    output = pathlib.Path(active_path).joinpath(new_object[1])
    return output


def chdir_up(active_path):
    output = pathlib.Path(active_path).parents[0]
    return output


def home_dir():
    output = pathlib.Path.home()
    return output


def read_file(active_path, object):

    new_path = active_path / object
    with open(new_path, "r") as file:
        for line in file:
            print(line.strip())


def copy(active_path, object, path):
    object_path = active_path / object
    if "\\" in path:
        if os.path.exists(object_path) and os.path.isfile(object_path):
            if os.path.exists(path) and os.path.isdir(path):
                shutil.copy(object_path, path)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {path}")
        else:
            print(f"Не существует файл {object}")
    else:
        new_path = active_path / path
        if os.path.exists(object_path) and os.path.isfile(object_path):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.copy(object_path, new_path)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {new_path}")
        else:
            print(f"Не существует файл {object}")


def copy_tree(active_path, object, target):
    object_path = active_path / object
    if "\\" in target:
        if os.path.exists(object_path) and os.path.isdir(object_path):
            if os.path.exists(target) and os.path.isdir(target):
                shutil.copytree(object_path, pathlib.Path(
                    target) / pathlib.Path(object), copy_function=shutil.copy2)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {target}")
        else:
            print(f"Не существует файл {object}")
    else:
        new_path = active_path / target
        if os.path.exists(object_path) and os.path.isdir(object_path):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.copytree(object_path, new_path / object,
                                copy_function=shutil.copy2)
                print("Копирование завершено")
            else:
                print(f"Не существует директория {new_path}")
        else:
            print(f"Не существует файл {object}")


def move(active_path, object, target):
    object_path = active_path / object
    if "\\" in target:
        if os.path.exists(object_path):
            if os.path.exists(target) and os.path.isdir(target):
                shutil.move(object_path, pathlib.Path(
                    target) / pathlib.Path(object))
                print("Перемещение завершено")
            else:
                print(f"Не существует директория {target}")
        else:
            print(f"Не существует файл {object}")
    else:
        new_path = active_path / target
        if os.path.exists(object_path):
            if os.path.exists(new_path) and os.path.isdir(new_path):
                shutil.move(object_path, new_path / object)
                print("Перемещение завершено")
            else:
                print(f"Не существует директория {new_path}")
        else:
            print(f"Не существует файл {object}")


def remove(active_path, object):
    if "\\" in object:
        conf = input("Для подтверждения введите y/n: ")
        if conf == "y":
            if os.path.exists(object) and os.path.isfile(object):
                os.remove(object)
                print("Файл удален")
            else:
                print(f"Не существует файл {object_path}")
        else:
            print("Удаление отменено")
    else:
        conf = input("Для подтверждения введите y/n: ")
        if conf == "y":
            object_path = active_path / object
            if os.path.exists(object_path) and os.path.isfile(object_path):
                os.remove(object_path)
                print("Файл удален")
            else:
                print(f"Не существует файл {object_path}")
        else:
            print("Удаление отменено")


def remove_tree(active_path, object):
    if "\\" in object:
        conf = input("Для подтверждения введите y/n: ")
        if conf == "y":
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
            print("Удаление отменено")
    else:
        conf = input("Для подтверждения введите y/n: ")
        if conf == "y":
            object_path = active_path / object
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
            print("Удаление отменено")
