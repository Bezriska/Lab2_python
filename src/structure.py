import os
import pathlib
from funcs import (if_ls, if_ls_l, chdir_down,
                    chdir_up, home_dir, read_file,
                    copy, copy_tree, move, remove,
                    remove_tree)

def structure():
    stop_word = "stop"
    active_path = pathlib.Path(r"C:\Users\TatyanaPC\Documents\Test_for_lab2")
    while True:
        print( "\n", active_path)
        user_input = input("Введите команду: ")
        if user_input != stop_word:
            if user_input == "ls" and os.path.exists(active_path) and os.path.isdir(active_path):
                print(if_ls(active_path))
            elif user_input == "ls" and (os.path.exists(active_path) == False) and (os.path.isdir(active_path) == False):
                #Рэйзим ошибку
                #Для теста просто принт
                print("Такой путь не существует, либо текущий объект не является папкой")
            elif user_input == "ls -l" and os.path.exists(active_path) and os.path.isdir(active_path):
                for sublist in if_ls_l(pathlib.Path(active_path)):
                    print(" ".join(map(str, sublist)))
            elif user_input == "ls -l" and (os.path.exists(active_path) == False) and (os.path.isdir(active_path) == False):
                #Рэйзим ошибку
                #Для теста просто принт
                print("Такой путь не существует, либо текущий объект не является папкой")
            elif "cd" == list(map(str, user_input.split()))[0]:
                parts = user_input.split()
                if len(parts) == 2:
                    if parts[1] == "..":
                        if os.path.exists(active_path.parents[0]):
                            active_path = chdir_up(active_path)
                        else:
                            #Рэйзим ошибку
                            print("отсутствует родительская директория")
                    
                    elif parts[1] == "~":
                        if os.path.exists(home_dir()):
                            active_path = home_dir()
                        else:
                            #Рэйзим ошибку
                            print("Отсутствует домашний каталог")

                    else:
                        if parts[1] in os.listdir(active_path):
                            new_path = chdir_down(active_path, user_input)
                            if os.path.isdir(new_path):
                                active_path = new_path
                            else:
                                #Рэйзим ошибку
                                print(f"'{parts[1]}' не является директорией")
                        else:
                            #Рэйзим ошибку
                            print(f"Отсутствует директория с именем {parts[1]}")
                else:
                    #Рэйзим ошибку
                    print("Неправильный формат команды cd. Используйте: cd <имя_директории> или cd ..")
            elif "cat" == list(map(str, user_input.split()))[0]:
                parts = user_input.split()
                if len(parts) == 2:
                    if os.path.exists(pathlib.Path(active_path) / parts[1]):
                        if pathlib.Path(active_path / parts[1]).is_file() and pathlib.Path(active_path / parts[1]).suffix == ".txt":
                            read_file(active_path, parts[1])
                        else:
                            #Рэйзим ошибку
                            print("Чтение файла с таким расширением не поддерживается")
                    else:
                        #Рэйзим ошибку
                        print("Отсутствует файл с таким именем")
                else:
                    #Рэйзим ошибку
                    print("Неправильный формат команды cat. Используйте: cat <имя_файла>")
            elif "cp" == list(map(str, user_input.split()))[0]:
                parts = user_input.split()
                if len(parts) == 3:
                    copy(active_path, parts[1], parts[2])
                elif len(parts) == 4 and parts[3] == "-r":
                    copy_tree(active_path, parts[1], parts[2])
                else:
                    #Рэйзим ошибку
                    print("Неправильный формат команды cp. Используйте: cp <имя_файла> <новая_директория>" \
                    "\nДля копирования каталога используйте: cp <имя_каталога> <новая_директория> -r")
            elif "mv" == list(map(str, user_input.split()))[0]:
                parts = user_input.split()
                if len(parts) == 3:
                    move(active_path, parts[1], parts[2])
                else:
                    #Рэйзим ошибку
                    print("Неправильный формат команды mv. Используйте: mv <имя_файла> <директория_перемещения>")
            elif "rm" == list(map(str, user_input.split()))[0]:
                parts = user_input.split()
                if len(parts) == 2:
                    remove(active_path, parts[1])
                elif len(parts) == 3 and parts[2] == "-r":
                    remove_tree(active_path, parts[1])
                else:
                    #Рэйзим ошибку
                    print("Неправильный формат команды rm. Используйте: rm <имя_файла>\n" \
                    "Для удаления каталога используйте: rm <имя_каталога> -r")

        
        else:
            print("Завершение программы")
            break

