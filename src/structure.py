import os
import pathlib
from logger import (logger, er_logger)
from funcs import (if_ls, if_ls_l, chdir_down,
                   chdir_up, home_dir, read_file,
                   copy, copy_tree, move, remove,
                   remove_tree, zip_archive, zip_unarchive,
                   tar_archive, tar_unarchive, grep)
from str_formatter import str_formatter


def structure():
    stop_word = "stop"
    active_path = pathlib.Path(r"C:\Users\TatyanaPC\Documents\Test_for_lab2")
    logger.debug(f"Start programm, default path: {str(active_path)}")
    while True:
        try:
            print("\n", active_path)
            user_input = input("Введите команду: ")
            print("\n")
            logger.debug(f"Current directory: {active_path}")
            logger.debug(f"{user_input}")
            if user_input != stop_word:
                parts = str_formatter(user_input)
                if "ls" == parts[0]:
                    if user_input == "ls":
                        print(if_ls(active_path))
                    else:
                        if "\\" not in parts[1]:
                            if os.path.exists(active_path) and os.path.isdir(active_path):
                                if len(parts) == 2 and parts[1] == "-l":
                                    for sublist in if_ls_l(active_path):
                                        print(" ".join(map(str, sublist)))
                                else:
                                    er_logger.error("Incorrect format of the ls command. Use: ls for relative paths, and ls -l for detailed output\n"
                                                    "For absolute paths, use: ls <path>, and ls <path> -l for detailed output")
                                    raise ValueError("Неправильный формат команды ls. Используйте: для отн. пути ls, для подробного вывода ls -l\n"
                                                     "Для абс. пути испльзуйте: ls <путь>, для подробного вывода ls <путь> -l")

                            else:
                                er_logger.error(
                                    "Current path is not exist or is not a directory")
                                raise FileNotFoundError(
                                    "Текущая директория не существует или не является папкой")

                        else:
                            if os.path.exists(parts[1]) and os.path.isdir(parts[1]):
                                if len(parts) == 2 and "\\" in parts[1]:
                                    print(if_ls(parts[1]))
                                elif len(parts) == 3 and "\\" in parts[1] and "-l" == parts[2]:
                                    for sublist in if_ls_l(pathlib.Path(parts[1])):
                                        print(" ".join(map(str, sublist)))
                                else:
                                    er_logger.error("Incorrect format of the ls command. Use: ls for relative paths, and ls -l for detailed output\n"
                                                    "For absolute paths, use: ls <path>, and ls <path> -l for detailed output")
                                    raise ValueError("Неправильный формат команды ls. Используйте: для отн. пути ls, для подробного вывода ls -l\n"
                                                     "Для абс. пути испльзуйте: ls <путь>, для подробного вывода ls <путь> -l")
                            else:
                                er_logger.error(
                                    f"Path {parts[1]} is not exist or does not lead to directory")
                                raise FileNotFoundError(
                                    f"Путь {parts[1]} не существет или ведет не к папке")
                elif "cd" == parts[0]:
                    if len(parts) == 2:
                        if parts[1] == "..":
                            if os.path.exists(active_path.parents[0]):
                                active_path = chdir_up(active_path)
                            else:
                                er_logger.error(
                                    "The parent directory is missing")
                                raise FileNotFoundError(
                                    "Отсутствует родительская директория")
                        elif parts[1] == "~":
                            if os.path.exists(home_dir()):
                                active_path = home_dir()
                            else:
                                er_logger.error(
                                    "The home directory is missing")
                                raise FileNotFoundError(
                                    "Отсутствует домашний каталог")
                        elif parts[1] == "-d":
                            active_path = active_path.anchor
                        else:
                            if "\\" not in parts[1]:
                                if parts[1] in os.listdir(active_path):
                                    new_path = chdir_down(
                                        active_path, parts[1])
                                    if os.path.isdir(new_path):
                                        active_path = new_path
                                    else:
                                        er_logger.error(
                                            f"{parts[1]} is not a directory")
                                        raise FileNotFoundError(
                                            f"{parts[1]} не является директорией")
                                else:
                                    er_logger.error(
                                        f"Missing directory with name: {parts[1]}")
                                    raise FileNotFoundError(
                                        f"Отсутствует директория с именем {parts[1]}")
                            else:
                                if pathlib.Path(parts[1]).name in os.listdir(pathlib.Path(parts[1]).parents[0]) and os.path.isdir(parts[1]):
                                    active_path = pathlib.Path(parts[1])
                                else:
                                    er_logger.error(
                                        f"Missing directory with name: {parts[1]}. To go to disk directory, enter: cd -d")
                                    raise FileNotFoundError(
                                        f"Отсутствует директория с именем {parts[1]}. Для перехода в каталог диска введите: cd -d")

                    else:
                        er_logger.error(
                            "Incorrect format of the command cd. Use: cd <directory_name> or cd ..")
                        raise ValueError(
                            "Неправильный формат команды cd. Используйте: cd <имя_директории> или cd ..")
                elif "cat" == parts[0]:
                    if len(parts) == 2:
                        if "\\" not in user_input:
                            if os.path.exists(pathlib.Path(active_path) / parts[1]):
                                if pathlib.Path(active_path / parts[1]).is_file() and pathlib.Path(active_path / parts[1]).suffix == ".txt":
                                    read_file(active_path, parts[1])
                                else:
                                    er_logger.error(
                                        "Reading a file with this extension is not supported.")
                                    raise ValueError(
                                        "Чтение файла с таким расширением не поддерживается")
                            else:
                                er_logger.error(
                                    f"Missing file with name: {parts[1]}")
                                raise FileNotFoundError(
                                    f"Missing file with name: {parts[1]}")
                        else:
                            if os.path.exists(parts[1]):
                                read_file(active_path, parts[1])
                            else:
                                er_logger.error(
                                    f"Missing file with name: {parts[1]}")
                                raise FileNotFoundError(
                                    f"Отсутствует файл с именем: {parts[1]}")
                    else:
                        er_logger.error(
                            "Incorrect format of the command cat. Use: cat <file_name>")
                        raise ValueError(
                            "Неправильный формат команды cat. Используйте: cat <имя_файла>")
                elif "cp" == parts[0]:
                    if len(parts) == 3:
                        copy(active_path, parts[1], parts[2])
                    elif len(parts) == 4 and parts[3] == "-r":
                        copy_tree(active_path, parts[1], parts[2])
                    else:
                        er_logger.error("Incorrect format of the command cp. Use: cp <file_name> <new_directory>\n"
                                        "To copy a directory, use: cp <directory_name> <new_directory> -r")
                        raise ValueError("Неправильный формат команды cp. Используйте: cp <имя_файла> <новая_директория>"
                                         "\nДля копирования каталога используйте: cp <имя_каталога> <новая_директория> -r")
                elif "mv" == parts[0]:
                    if len(parts) == 3:
                        move(active_path, parts[1], parts[2])
                    else:
                        er_logger.error(
                            "Incorrect format of the command mv. Use: mv <file_name> <new_directory>")
                        raise ValueError(
                            "Неправильный формат команды mv. Используйте: mv <имя_файла> <директория_перемещения>")
                elif "rm" == parts[0]:
                    if len(parts) == 2:
                        remove(active_path, parts[1])
                    elif len(parts) == 3 and parts[2] == "-r":
                        remove_tree(active_path, parts[1])
                    else:
                        print("Неправильный формат команды rm. Используйте: rm <имя_файла>\n"
                              "Для удаления каталога используйте: rm <имя_каталога> -r")
                        er_logger.error("Incorrect format of the command rm. Use: rm <file_name>\n"
                                        "To remove a directory, use: rm <directory_name> -r")
                        raise ValueError("Неправильный формат команды rm. Используйте: rm <имя_файла>\n"
                                         "Для удаления каталога используйте: rm <имя_каталога> -r")

                elif "zip" == parts[0]:
                    if len(parts) == 3:
                        zip_archive(active_path, parts[1], parts[2])
                    else:
                        er_logger.error(
                            "Incorrect format of the command zip. Use: zip <directory_name> <archive_name>")
                        raise ValueError(
                            "Неправильный формат команды zip. Используйте: zip <имя_директории> <название архива>")
                elif "unzip" == parts[0]:
                    if len(parts) == 2:
                        zip_unarchive(active_path, parts[1])
                    else:
                        er_logger.error(
                            "Incorrect format of the command unzip. Use: unzip <archive_name>")
                        raise ValueError(
                            "Неправильный формат команды unzip. Используйте: unzip <название архива>")
                elif "tar" == parts[0]:
                    if len(parts) == 3:
                        tar_archive(active_path, parts[1], parts[2])
                    else:
                        er_logger.error(
                            "Incorrect format of the command zip. Use: zip <directory_name> <archive_name>")
                        raise ValueError(
                            "Неправильный формат команды zip. Используйте: zip <имя_директории> <название архива>")
                elif "untar" == parts[0]:
                    if len(parts) == 2:
                        tar_unarchive(active_path, parts[1])
                    else:
                        er_logger.error(
                            "Incorrect format of the command unzip. Use: unzip <archive_name>")
                        raise ValueError(
                            "Неправильный формат команды unzip. Используйте: unzip <название архива>")

                elif "grep" == parts[0]:
                    if len(parts) == 3:
                        grep(parts[1], parts[2])
                    elif len(parts) == 4:
                        if parts[3] == "-i":
                            grep(parts[1], parts[2], None, parts[3])
                        elif parts[3] == "-r":
                            grep(parts[1], parts[2], parts[3], None)
                        else:
                            er_logger.error(
                                "Incorrect flag. Avalible flags: <-r>, <-i>")
                            raise ValueError(
                                "Неверный флаг. Доступные флаги: <-r>, <-i>")
                    elif len(parts) == 5:
                        grep(parts[1], parts[2], parts[3], parts[4])
                    else:
                        er_logger.error(
                            "??")
                        raise ValueError(
                            "??")
                else:
                    er_logger.error("Incorrect command")
                    raise ValueError("Такой команды не существует")

            else:
                print("Завершение программы")
                break
        except ValueError as v:
            print(v)
        except FileNotFoundError as f:
            print(f)
        except PermissionError as p:
            print(p)
