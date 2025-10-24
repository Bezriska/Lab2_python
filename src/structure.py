import os
import pathlib
from logger import (logger, er_logger)
from funcs import (if_ls, if_ls_l, chdir_down,
                   chdir_up, home_dir, read_file,
                   copy, copy_tree, move, remove,
                   remove_tree)
from str_formatter import str_formatter


def structure():
    stop_word = "stop"
    active_path = pathlib.Path(r"C:\Users\TatyanaPC\Documents\Test_for_lab2")
    logger.debug(f"Start programm, default path: {str(active_path)}")
    while True:
        print("\n", active_path)
        user_input = input("Введите команду: ")
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
                                # Рэйзим ошибку
                                print("Неправильный формат команды ls. Используйте: для отн. пути ls, для подробного вывода ls -l\n"
                                      "Для абс. пути испльзуйте: ls <путь>, для подробного вывода ls <путь> -l")
                                er_logger.error("Incorrect format of the ls command. Use: ls for relative paths, and ls -l for detailed output\n"
                                                "For absolute paths, use: ls <path>, and ls <path> -l for detailed output")
                        else:
                            # Рэйзим ошибку
                            print(
                                "Текущая директория не существует или не является папкой")
                            er_logger.error(
                                "Current path is not exist or is not a directory")
                    else:
                        if os.path.exists(parts[1]) and os.path.isdir(parts[1]):
                            if len(parts) == 2 and "\\" in parts[1]:
                                print(if_ls(parts[1]))
                            elif len(parts) == 3 and "\\" in parts[1] and "-l" == parts[2]:
                                for sublist in if_ls_l(pathlib.Path(parts[1])):
                                    print(" ".join(map(str, sublist)))
                            else:
                                # Рэйзим ошибку
                                print("Неправильный формат команды ls. Используйте: для отн. пути ls, для подробного вывода ls -l\n"
                                      "Для абс. пути испльзуйте: ls <путь>, для подробного вывода ls <путь> -l")
                                er_logger.error("Incorrect format of the ls command. Use: ls for relative paths, and ls -l for detailed output\n"
                                                "For absolute paths, use: ls <path>, and ls <path> -l for detailed output")
                        else:
                            # Рэйзим ошибку
                            print(
                                f"Путь {parts[1]} не существет или ведет не к папке")
                            er_logger.error(
                                f"Path {parts[1]} is not exist or does not lead to directory")

            # if user_input == "ls" and os.path.exists(active_path) and os.path.isdir(active_path):
            #     print(if_ls(active_path))
            # elif user_input == "ls" and (os.path.exists(active_path) == False) and (os.path.isdir(active_path) == False):
            #     #Рэйзим ошибку
            #     #Для теста просто принт
            #     print("Такой путь не существует, либо текущий объект не является папкой")
            #     er_logger.error("This path does not exist, or the current object is not a folder")
            # elif user_input == "ls -l" and os.path.exists(active_path) and os.path.isdir(active_path):
            #     for sublist in if_ls_l(pathlib.Path(active_path)):
            #         print(" ".join(map(str, sublist)))
            # elif user_input == "ls -l" and (os.path.exists(active_path) == False) and (os.path.isdir(active_path) == False):
            #     #Рэйзим ошибку
            #     #Для теста просто принт
            #     print("Такой путь не существует, либо текущий объект не является папкой")
            #     er_logger.error("This path does not exist, or the current object is not a folder")
            elif "cd" == parts[0]:
                if len(parts) == 2:
                    if parts[1] == "..":
                        if os.path.exists(active_path.parents[0]):
                            active_path = chdir_up(active_path)
                        else:
                            # Рэйзим ошибку
                            print("Отсутствует родительская директория")
                            er_logger.error("The parent directory is missing")

                    elif parts[1] == "~":
                        if os.path.exists(home_dir()):
                            active_path = home_dir()
                        else:
                            # Рэйзим ошибку
                            print("Отсутствует домашний каталог")
                            er_logger.error("The home directory is missing")
                    else:
                        if parts[1] in os.listdir(active_path):
                            new_path = chdir_down(active_path, parts[1])
                            if os.path.isdir(new_path):
                                active_path = new_path
                            else:
                                # Рэйзим ошибку
                                print(f"{parts[1]} не является директорией")
                                er_logger.error(
                                    f"{parts[1]} is not a directory")
                        else:
                            # Рэйзим ошибку
                            print(
                                f"Отсутствует директория с именем {parts[1]}")
                            er_logger.error(
                                f"Missing directory with name: {parts[1]}")
                else:
                    # Рэйзим ошибку
                    print(
                        "Неправильный формат команды cd. Используйте: cd <имя_директории> или cd ..")
                    er_logger.error(
                        "Incorrect format of the command cd. Use: cd <directory_name> or cd ..")
            elif "cat" == parts[0]:
                if len(parts) == 2:
                    if os.path.exists(pathlib.Path(active_path) / parts[1]):
                        if pathlib.Path(active_path / parts[1]).is_file() and pathlib.Path(active_path / parts[1]).suffix == ".txt":
                            read_file(active_path, parts[1])
                        else:
                            # Рэйзим ошибку
                            print(
                                "Чтение файла с таким расширением не поддерживается")
                            er_logger.error(
                                "Reading a file with this extension is not supported.")
                    else:
                        # Рэйзим ошибку
                        print(f"Отсутствует файл с именем: {parts[1]}")
                        er_logger.error(f"Missing file with name: {parts[1]}")
                else:
                    # Рэйзим ошибку
                    print(
                        "Неправильный формат команды cat. Используйте: cat <имя_файла>")
                    er_logger.error(
                        "Incorrect format of the command cat. Use: cat <file_name>")
            elif "cp" == parts[0]:
                if len(parts) == 3:
                    copy(active_path, parts[1], parts[2])
                elif len(parts) == 4 and parts[3] == "-r":
                    copy_tree(active_path, parts[1], parts[2])
                else:
                    # Рэйзим ошибку
                    print("Неправильный формат команды cp. Используйте: cp <имя_файла> <новая_директория>"
                          "\nДля копирования каталога используйте: cp <имя_каталога> <новая_директория> -r")
                    er_logger.error("Incorrect format of the command cp. Use: cp <file_name> <new_directory>\n"
                                    "To copy a directory, use: cp <directory_name> <new_directory> -r")
            elif "mv" == parts[0]:
                if len(parts) == 3:
                    move(active_path, parts[1], parts[2])
                else:
                    # Рэйзим ошибку
                    print(
                        "Неправильный формат команды mv. Используйте: mv <имя_файла> <директория_перемещения>")
                    er_logger.error(
                        "Incorrect format of the command mv. Use: mv <file_name> <new_directory>")
            elif "rm" == parts[0]:
                if len(parts) == 2:
                    remove(active_path, parts[1])
                elif len(parts) == 3 and parts[2] == "-r":
                    remove_tree(active_path, parts[1])
                else:
                    # Рэйзим ошибку
                    print("Неправильный формат команды rm. Используйте: rm <имя_файла>\n"
                          "Для удаления каталога используйте: rm <имя_каталога> -r")
                    er_logger.error("Incorrect format of the command rm. Use: rm <file_name>\n"
                                    "To remove a directory, use: rm <directory_name> -r")

        else:
            print("Завершение программы")
            break
