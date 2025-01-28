from .element_processor import ElementProcessor
from logger import Logger

class RenderedPageBreakProcessor(ElementProcessor):

    def __init__(self):
        self.logger = Logger()
        # pass

    def process(self, element):
        self.logger.logn("> process pagebreak")
        return "\\clearpage\n\\newpage"


