from docx.drawing import Drawing
from docx.text.hyperlink import Hyperlink
from docx.text.pagebreak import RenderedPageBreak

from logger import Logger
from .element_processor import ElementProcessor

class HyperlinkProcessor(ElementProcessor):

    def __init__(self):
        self.logger = Logger()

    def process(self, element: Hyperlink):
        self.logger.logn("> process hyperlink")
        return f'\\href{{{element.text}}}{{{element.text}}}'
