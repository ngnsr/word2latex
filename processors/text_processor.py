from .element_processor import ElementProcessor
from logger import Logger
# from pylatexenc.latexencode import unicode_to_latex
from utils import unicode_to_latex

class TextProcessor(ElementProcessor):
    def __init__(self):
        self.logger = Logger()


    def process(self, element):
        # self.logger.logn("> process str")
        # errors ???
        # styles:
        # {\fontfamily{lmss}\selectfont Текст у шрифті без засічок.}
        # return element
        return unicode_to_latex(element)
        # return unicode_to_latex(element, non_ascii_only=True)
