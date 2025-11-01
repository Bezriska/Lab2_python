from str_formatter import str_formatter
import pathlib
import shutil
from logger import er_logger


def undo(active_path) -> None:
    """Отменяет последнюю выполненную команду из списка: cp, mv, rm

    Args:
        active_path (Path): Текущая активная директория

    Raises:
        FileNotFoundError: Файл истории не найден
        ValueError: Последняя команда не поддерживается для отмены или история пуста
    """
    try:
        with open(".history", "r", encoding='utf-8') as file:
            history_line = file.readline().strip()
            if not history_line:
                er_logger.error("History is empty")
                raise ValueError("История команд пуста")
            history = history_line.split("|")
        if not history or len(history) == 0:
            er_logger.error("No commands to undo")
            raise ValueError("Нет команд для отмены")
        last_com = history[-1].strip()
        if not last_com:
            er_logger.error("Last command is empty")
            raise ValueError("Последняя команда пуста")
        parts = str_formatter(last_com)
        command = parts[0]
        if command == "mv" and len(parts) >= 3:
            undo_mv(parts, active_path, history)
        elif command == "cp" and len(parts) >= 3:
            undo_cp(parts, active_path, history)
        elif command == "rm" and len(parts) >= 2:
            undo_rm(parts, active_path, history)
        else:
            er_logger.error(
                f"Command {command} is not supported for undo or has incorrect format")
            raise ValueError(
                f"Команда {command} не поддерживается для отмены или имеет неправильный формат")
    except FileNotFoundError as e:
        if "История" in str(e) or "History" in str(e):
            raise e
        er_logger.error("History file not found")
        raise FileNotFoundError("Файл истории не найден")
    except Exception as e:
        er_logger.error(f"Error during undo: {str(e)}")
        raise ValueError(f"Ошибка при отмене команды: {str(e)}")


def update_history(history) -> None:
    """Обновляет файл истории после удаления команды

    Args:
        history (list): Список команд истории
    """
    with open(".history", "w", encoding='utf-8') as file:
        if history:
            file.write("|".join(history))
        else:
            file.write("")


def undo_mv(parts, active_path, history) -> None:
    """Отменяет команду mv - возвращает объект в исходное место

    Args:
        parts (list): Части команды [mv, source, target]
        active_path (Path): Текущая активная директория
        history (list): Список команд истории

    Raises:
        FileNotFoundError: Файл не найден или целевая директория не существует
    """
    original_source = parts[1]
    original_target = parts[2]
    file_name = pathlib.Path(original_source).name
    if "\\" in original_target:
        current_location = pathlib.Path(original_target) / file_name
    else:
        current_location = active_path / original_target / file_name
    if "\\" in original_source:
        return_to_dir = pathlib.Path(original_source).parent
    else:
        return_to_dir = active_path
    if current_location.exists():
        destination = return_to_dir / file_name
        if return_to_dir.exists() and return_to_dir.is_dir():
            shutil.move(str(current_location), str(destination))
            print(
                f"Команда mv отменена: {file_name} возвращен из {current_location.parent} в {return_to_dir}")
            del history[-1]
            update_history(history)
        else:
            raise FileNotFoundError(
                f"Целевая директория для возврата не существует: {return_to_dir}")
    else:
        raise FileNotFoundError(
            f"Файл не найден в ожидаемом месте: {current_location}")


def undo_cp(parts, active_path, history) -> None:
    """Отменяет команду cp - удаляет скопированный файл/каталог

    Args:
        parts (list): Части команды [cp, source, target]
        active_path (Path): Текущая активная директория
        history (list): Список команд истории

    Raises:
        FileNotFoundError: Скопированный объект не найден
        ValueError: Ошибка при удалении скопированного объекта
    """
    original_source = parts[1]
    original_target = parts[2]
    item_name = pathlib.Path(original_source).name
    if "\\" in original_target:
        copied_location = pathlib.Path(original_target) / item_name
    else:
        copied_location = active_path / original_target / item_name
    if copied_location.exists():
        try:
            if copied_location.is_file():
                copied_location.unlink()
                print(
                    f"Команда cp отменена: удален скопированный файл {copied_location}")
            elif copied_location.is_dir():
                shutil.rmtree(copied_location)
                print(
                    f"Команда cp отменена: удален скопированный каталог {copied_location}")

            del history[-1]
            update_history(history)
        except Exception as e:
            raise ValueError(
                f"Ошибка при удалении скопированного объекта: {e}")
    else:
        raise FileNotFoundError(
            f"Скопированный объект не найден: {copied_location}")


def undo_rm(parts, active_path, history) -> None:
    """Отменяет команду rm - восстанавливает из временного каталога .trash

    Args:
        parts (list): Части команды [rm, deleted_item]
        active_path (Path): Текущая активная директория
        history (list): Список команд истории

    Raises:
        FileNotFoundError: Объект не найден в .trash
        ValueError: Ошибка при восстановлении из .trash
    """
    deleted_item = parts[1]
    item_name = pathlib.Path(deleted_item).name
    trash_dir = active_path / ".trash"
    trash_location = trash_dir / item_name
    if trash_location.exists():
        try:
            if "\\" in deleted_item:
                restore_to = pathlib.Path(deleted_item)
            else:
                restore_to = active_path / deleted_item

            shutil.move(str(trash_location), str(restore_to))
            print(
                f"Команда rm отменена: {item_name} восстановлен из .trash в {restore_to.parent}")

            del history[-1]
            update_history(history)
        except Exception as e:
            raise ValueError(f"Ошибка при восстановлении из .trash: {e}")
    else:
        raise FileNotFoundError(
            f"Объект не найден в .trash: {trash_location}. Возможно, .trash была очищена или объект удален навсегда.")
