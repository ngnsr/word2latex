from .element_processor import ElementProcessor
from logger import Logger
class DrawingProcessor(ElementProcessor):
    def __init__(self):
        self.logger = Logger()
        self.imgCount = 0


    # make sure that images copied to output/img directory
    def process(self, element):
        self.logger.logn("> process drawing")
        res = f"\\includegraphics[width=0.9\\linewidth]{{img/img{self.imgCount}.png}}"
        # res = f"\\begin{{figure}}[h!]\\includegraphics[\\linewidth]{{img/img{self.imgCount}.png}}\\end{{figure}}"
        self.imgCount += 1
        return res
