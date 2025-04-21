from .element_processor import ElementProcessor
from logger import Logger
from utils import unicode_to_latex

class TextProcessor(ElementProcessor):
    def __init__(self):
        self.logger = Logger()


    def process(self, element):
        self.logger.logn(f"> process str {element}")
        return unicode_to_latex(element)
