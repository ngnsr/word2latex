from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

from document_builder import LatexDocumentBuilder
from logger import Logger
from processors import list_processor

from .paragraph_processor import ParagraphProcessor
from .table_processor import TableProcessor
from .list_processor import ListProcessor
from  utils import extract_images_from_docx

class WordProcessor():

    def __init__(self):
        self.listProcessor = ListProcessor()

    def process(self, file_path: str):
        logger = Logger()
        logger.logn(f'Start processing file with path: {file_path}')

        doc = Document(file_path)

        # fonts should be tracked and added 
        builder = LatexDocumentBuilder()

        # write images to out dir
        output_dir = "out/img"
        extract_images_from_docx(file_path, output_dir)

        paragraphProcessor = ParagraphProcessor()
        tableProcessor = TableProcessor()
        list_paragraphs = []

        for element in doc.element.body:
            logger.logn(f' < process {element.tag}')
            # print(element.tag)
            if element.tag.endswith("p"):
                paragraph = Paragraph(element, doc)

                # list = ListProcessor.is_list(paragraph, doc)
                list = ListProcessor.is_list(paragraph, doc)
                if list != None:
                    # print("inside")
                    list_paragraphs.append(paragraph)
                else:
                    out = paragraphProcessor.process(paragraph)
                    if list_paragraphs:
                        # print("called")
                        # Call ListProcessor
                        out = self.listProcessor.process(list_paragraphs, doc) + "\n" + out
                        list_paragraphs.clear()

                    builder.add_element(out)

            elif element.tag.endswith("tbl"):  # Таблиця
                table = Table(element, doc)
                out = tableProcessor.process(table)
                builder.add_element(out)
            elif element.tag.endswith("sectPr"): # end of section
                pass
            elif element.tag.endswith("sdt"):
                pass

            else:
                logger.errn(f'Unsuported tag: {element.tag}')
                
        return builder.build()
