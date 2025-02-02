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
        self.logger.logn("> process run")
        run = element
        result = []
        for strDrawingPageBreak in run.iter_inner_content():
            if isinstance(strDrawingPageBreak, str):
                font_name = run.font.name
                text = run.text

                # Call TextProcessor
                out = self.textProcessor.process(text)
                if run.bold:
                    out = f"\\textbf{{{out}}}"
                if run.italic:
                    out = f"\\textit{{{out}}}"
                if run.underline:
                    out = f"\\underline{{{out}}}"
                if run.font.name:
                    # ends up for every paragraph so ignore
                    # self.logger.logn(f"!!!!!!!!!!!!!!!!!font_name {font_name}")
                    # latex_text = f"{{\\fontfamily{{{font_name}}}\\selectfont {latex_text}}}"
                    pass

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
