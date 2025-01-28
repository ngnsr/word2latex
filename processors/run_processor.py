import logger
from .element_processor import ElementProcessor
from .text_processor import TextProcessor
from .drawing_processor import DrawingProcessor
from .rendered_page_break_processor import RenderedPageBreakProcessor

from logger import Logger

from docx.drawing import Drawing
from docx.text.pagebreak import RenderedPageBreak

class RunProcessor(ElementProcessor):

    def __init__(self):
        self.textProcessor = TextProcessor()
        self.drawingProcessor = DrawingProcessor()
        self.renderedPageBreakProcessor = RenderedPageBreakProcessor()
        self.logger = Logger()

    def process(self, element):
        # self.logger.logn("> process run")

        run = element
        result = []
        for strDrawingPageBreak in run.iter_inner_content():
            if isinstance(strDrawingPageBreak, str):
                # TODO: is it even work
                font_name = run.font.name
                font_size = run.font.size
                is_bold = run.bold
                is_italic = run.italic
                text = run.text

                out = self.textProcessor.process(text)
                if is_bold:
                    # self.logger.logn("!!!!!!!!!!!!!!!!!bold")
                    out = f"\\textbf{{{out}}}"
                if is_italic:
                    # self.logger.logn("!!!!!!!!!!!!!!!!!italic")
                    out = f"\\textit{{{out}}}"
                if font_name:
                    pass
                    # self.logger.logn(f"!!!!!!!!!!!!!!!!!font_name {font_name}")
                    # latex_text = f"{{\\fontfamily{{{font_name}}}\\selectfont {latex_text}}}"

                # Call TextProcessor
                result.append(out)

            elif isinstance(strDrawingPageBreak, Drawing):
                # Call DrawingProcessor
                out = self.drawingProcessor.process(strDrawingPageBreak)
                result.append(out)
            elif isinstance(strDrawingPageBreak, RenderedPageBreak):
                # Call RenderedPageBreakProcessor
                out = self.renderedPageBreakProcessor.process(strDrawingPageBreak)
                result.append(out)

        return "\n".join(result)
