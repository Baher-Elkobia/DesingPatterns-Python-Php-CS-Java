import os


class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        """__new__ method will be called when an object is created, __new__ is called before __init__,
        Instance can be created inside __new__ method either by using super function or
        by directly calling __new__ method over object
        """
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, file_name='log.txt'):
        """__init__ method will be called to initialize the object"""
        self.file_name = os.path.join(os.getcwd(), file_name)

    def _log(self, level, msg):
        """Write a message to the file"""

        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")

    def critical(self, msg):
        self._log("CRITICAL", msg)

    def error(self, msg):
        self._log("ERROR", msg)

    def warn(self, msg):
        self._log("WARN", msg)

    def info(self, msg):
        self._log("INFO", msg)

    def debug(self, msg):
        self._log("DEBUG", msg)
