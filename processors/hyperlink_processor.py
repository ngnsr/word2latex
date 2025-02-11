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
        hyperlink = element
        # print("#################",hyperlink.address)
        # check bookmarks
        # if hyperlink.fragment != None:
            # self.logger.logn(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$ {hyperlink.fragment}")
        # if hyperlink.url != None:
        #     self.logger.logn(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$ {hyperlink.url}")
        # if hyperlink.address != None:
        #     self.logger.logn(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$ {hyperlink.address}")

        for run in hyperlink.runs:
            # Maybe call RunProcessor
            for c in run.iter_inner_content():
                if isinstance(c, str):
                    pass
                    # print("str")
                    # self.logger.logn(f"!!!!!!!!!!!!!!!!!!! {c}")
                elif isinstance(c, Drawing):
                    pass
                    # print("drawing")
                    # self.logger.logn(f"!!!!!!!!!!!!!!!!!!! {c}")
                elif isinstance(c, RenderedPageBreak):
                    pass
                    # print("page break")
                    # self.logger.logn("c")
                    # print(run)
        return f'\\href{{{hyperlink.text}}}{{{hyperlink.text}}}'
        # return f'\\hyperref[{hyperlink.text}]{{{hyperlink.text}}}'
