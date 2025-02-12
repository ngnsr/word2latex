from docx import Document
from docx.text.paragraph import Paragraph
from .element_processor import ElementProcessor
from .hyperlink_processor import HyperlinkProcessor
from .run_processor import RunProcessor
from logger import Logger
from docx.text.run import Run
import threading
from lxml import etree

class ListProcessor(ElementProcessor):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ListProcessor, cls).__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.logger = Logger()
            self.stack = []
            self._initialized = True
            self.hyperlinkProcessor = HyperlinkProcessor()
            self.runProcessor = RunProcessor()

    # paragraphs should contain list items
    def process(self, paragraphs, doc):
        self.logger.logn("> Processing list")
        result = []

        for paragraph in paragraphs:
            list_info = self.is_list(paragraph, doc)

            if list_info:
                num_id, level, is_numbered = list_info

                while (self.stack and self.stack[-1][0] > level) or (self.stack.__len__() >= 2 and self.stack[-2][2] == num_id):
                    result.append(f"\\end{{{self.stack.pop()[1]}}}")

                if not self.stack or (self.stack and self.stack[-1][0] < level or self.stack[-1][2] != num_id):
                    list_type = "enumerate" if is_numbered else "itemize"
                    result.append(f"\\begin{{{list_type}}}")
                    self.stack.append((level, list_type, num_id))

                # TODO: hypenetion
                result.append(f"\\item {self.processInner(paragraph)}")


        while self.stack:
            result.append(f"\\end{{{self.stack.pop()[1]}}}")

        return "\n".join(result) + "\n"

    def processInner(self, paragraph):
        out = ''
        for runHyperlink in paragraph.iter_inner_content():
            if isinstance(runHyperlink, Run):
                # Call RunProcessor
                r = self.runProcessor.process(runHyperlink)
                if r != '': # ignore blank runs
                    out = out + "\n" + r

            else: # is Hyperlink
                # Call HyperlinkProcessor
                r = self.hyperlinkProcessor.process(runHyperlink)
                out = out + "\n" + r
        return out

    @staticmethod
    def is_list(paragraph: Paragraph, doc: Document):
        if paragraph._element.pPr is None or paragraph._element.pPr.numPr is None:
            return None

        num_id = paragraph._element.pPr.numPr.numId.val 
        level = paragraph._element.pPr.numPr.ilvl.val
        numbering = doc.part.numbering_part.numbering_definitions._numbering

        # https://docs.python.org/3/library/xml.etree.elementtree.html
        # check (Numbering.xml) first numFmt attrib of abstractNum with abstractNumId == num_id  - from paragraph (which is list) attrib
        fmt = ''
        firstAbstractNum = numbering.find(f"{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}abstractNum/[@{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}abstractNumId='{num_id}']")
        if firstAbstractNum:
            firstLvl = firstAbstractNum.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}lvl")
            if firstLvl:
                numFmt = firstLvl.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}numFmt") 
                fmt = numFmt.attrib['{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val']
                # level is indentation level from 0 to 8, 0 is first level (\t●)
                return num_id, level, fmt == "decimal"

        # why a u here bruh
        return None

