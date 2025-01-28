from docx.text.paragraph import Paragraph

from docx.text.paragraph import Paragraph
from docx.text.run import Run

from .element_processor import ElementProcessor
from .hyperlink_processor import HyperlinkProcessor
from .run_processor import RunProcessor
from logger import Logger

class ParagraphProcessor(ElementProcessor):

    def __init__(self):
        self.hyperlinkProcessor = HyperlinkProcessor()
        self.runProcessor = RunProcessor()
        self.logger = Logger()

    def process(self, element: Paragraph):
        self.logger.logn('> process paragraph')
        paragraph = element
        res = []
        for runHyperlink in paragraph.iter_inner_content():
            if isinstance(runHyperlink, Run):
                # Call RunProcessor
                out = self.runProcessor.process(runHyperlink)
                res.append(out)

            else: # is Hyperlink
                # Call HyperlinkProcessor
                out = self.hyperlinkProcessor.process(runHyperlink)
                res.append(out)
                # do smth with that
        res.append("\\newline")
        return "\n".join(res)
