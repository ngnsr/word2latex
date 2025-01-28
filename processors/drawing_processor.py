from .element_processor import ElementProcessor
from logger import Logger

from docx.drawing import Drawing
class DrawingProcessor(ElementProcessor):
    def __init__(self):
        self.logger = Logger()

    # make sure that images copied to output/img directory
    def process(self, element: Drawing):
        # self.logger.logn("> process drawing")

        nsmap = {
            "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
            "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
            "pic": "http://schemas.openxmlformats.org/drawingml/2006/picture",
        }
        doc_pr = element._element.find(".//wp:docPr", namespaces=nsmap)
        image_name = ""
        if doc_pr is not None:
            image_name = doc_pr.attrib.get("name")
            if image_name is None:
                self.logger.errn("Can't find image name when processing Drawing xml")
                exit(-1)
        else:
            self.logger.errn("Can't find image name when processing Drawing xml")
            exit(-1)
        
        return f"\\includegraphics[width=0.9\\linewidth]{{img/{image_name}}}"
