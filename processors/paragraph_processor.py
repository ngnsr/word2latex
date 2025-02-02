from types import NoneType
from docx.text.paragraph import Paragraph

from docx.text.paragraph import Paragraph
from docx.text.run import Run

from .element_processor import ElementProcessor
from .hyperlink_processor import HyperlinkProcessor
from .run_processor import RunProcessor
from .rendered_page_break_processor import RenderedPageBreakProcessor
from logger import Logger

class ParagraphProcessor(ElementProcessor):

    def __init__(self):
        self.hyperlinkProcessor = HyperlinkProcessor()
        self.runProcessor = RunProcessor()
        self.renderedPageBreakProcessor = RenderedPageBreakProcessor()
        self.logger = Logger()

    def process(self, element: Paragraph):
        # self.logger.logn('> process paragraph')
        paragraph = element
        res = []

        # if have Heading*/subtitle return 
        if paragraph != None and paragraph.style != None and paragraph.style.name != None and paragraph.text != '':
            name = paragraph.style.name
            text = paragraph.text
            if name.startswith("Heading"):
                text = f"\\section{{{text}}}"
            elif name.startswith("Subtitle"):
                text = f"\\subsection{{{text}}}"

            return f"{text}"

        for runHyperlink in paragraph.iter_inner_content():
            if isinstance(runHyperlink, Run):
                # Call RunProcessor
                out = self.runProcessor.process(runHyperlink)
                if out != '': # ignore blank runs
                    res.append(out)

            else: # is Hyperlink
                # Call HyperlinkProcessor
                out = self.hyperlinkProcessor.process(runHyperlink)
                res.append(out)
                # do smth with that

        # res.append("\\n\\n")

        if self.has_page_break(paragraph):
            # Call RenderedPageBreakProcessor
            out = self.renderedPageBreakProcessor.process(paragraph)
            res.append(out)


        return "\n".join(res)

    def has_page_break(self, paragraph: Paragraph) -> bool:
        xml_content = paragraph._element
        for br in xml_content.findall(".//w:br", namespaces=xml_content.nsmap):
            if br.get("{%s}type" % xml_content.nsmap["w"]) == "page":
                return True
        return False
