import logging

# Logger (Singleton)
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._setup()
        return cls._instance

    def _setup(self):
        self.logs = []
        logging.basicConfig(level=logging.INFO)

    def log(self, message):
        self.logs.append(message)
        logging.info(message)

    def logn(self, message):
        self.logs.append(message + '\n')
        logging.info(message)

    def err(self, error):
        self.logs.append(error)
        logging.error(error)

    def errn(self, error):
        self.logs.append(error + '\n')
        logging.error(error)

