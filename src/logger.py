import logging

def setup_logger():
    logger = logging.getLogger("Shell_logger")
    logger.setLevel(logging.DEBUG)

    file_handler_info = logging.FileHandler("shell.log")
    file_handler_info.setLevel(logging.DEBUG)

    formatter = logging.Formatter(fmt = "[%(asctime)s] %(levelname)s: %(message)s", datefmt = "%Y-%m-%d %H:%M:%S")
    file_handler_info.setFormatter(formatter)

    logger.addHandler(file_handler_info)

    return logger

logger = setup_logger()

def setup_er_logger():
    er_logger = logging.getLogger("Shell_er_logger")
    er_logger.setLevel(logging.ERROR)

    file_handler_errors = logging.FileHandler("shell.log")
    file_handler_errors.setLevel(logging.ERROR)

    formatter = logging.Formatter(fmt = "[%(asctime)s] %(levelname)s: %(message)s", datefmt = "%Y-%m-%d %H:%M:%S")
    file_handler_errors.setFormatter(formatter)

    er_logger.addHandler(file_handler_errors)

    return er_logger

er_logger = setup_er_logger()