import pathlib


def write_in_history(command, old_hs) -> list:
    """Запись команды в историю

    Args:
        command (str): Команда
        old_hs (list): Предыдущая история команд

    Returns:
        list: Обновленная история команд
    """
    if old_hs == ['']:
        old_hs = []
    old_hs.append(command)
    if len(old_hs) > 5:
        old_hs = old_hs[-5:]
    with open(".history", "w", encoding='utf-8') as file:
        history_string = "|".join(old_hs)
        file.write(history_string)
    return old_hs


def history(amount_com=None) -> None:
    """Отображение истории команд

    Args:
        amount_com (int, optional): количество команд для отображения. По умолчанию принимает None.
    """
    history_path = pathlib.Path(".history")

    if history_path.is_file():
        with open(history_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if content:
                # Разделяем команды по символу |
                commands = content.split("|")

                if amount_com == None:
                    for i, cmd in enumerate(commands):
                        print(f"{i + 1}: {cmd}")
                else:
                    if amount_com > len(commands):
                        amount_com = len(commands)
                    start_index = len(commands) - amount_com
                    for i in range(start_index, len(commands)):
                        print(f"{i + 1}: {commands[i]}")
            else:
                print("История команд пуста")
    else:
        print("История команд отсутствует")
