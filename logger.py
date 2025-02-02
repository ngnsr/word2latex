import logging
from threading import Lock

# Logger (Singleton)
class Logger:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._setup()
        return cls._instance

    def _setup(self):
        self.logs = []
        self.enabled = True
        self.logger = logging.getLogger("Logger")
        self.logger.setLevel(logging.INFO)

        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter("[%(levelname)s] %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def log(self, message):
        if self.enabled:
            self.logs.append(message)
            self.logger.info(message)

    def logn(self, message):
        if self.enabled:
            self.logs.append(message + '\n')
            self.logger.info(message)

    def err(self, error):
        if self.enabled:
            self.logs.append(error)
            self.logger.error(error)

    def errn(self, error):
        if self.enabled:
            self.logs.append(error + '\n')
            self.logger.error(error)

    def on(self):
        self.enabled = True

    def off(self):
        self.enabled = False
