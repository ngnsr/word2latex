from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from document_builder import LatexDocumentBuilder
from .paragraph_processor import ParagraphProcessor
from .table_processor import TableProcessor
from .list_processor import ListProcessor
from  utils import extract_images_from_docx
from logger import Logger

import shutil

class WordProcessor():

    @staticmethod
    def process(file_path: str):
        logger = Logger()
        logger.logn(f'Start processing file with path: {file_path}')

        doc = Document(file_path)

        builder = LatexDocumentBuilder()

        # write images to out dir
        output_dir = "out"
        extract_images_from_docx(file_path, output_dir=output_dir+'/img')

        paragraphProcessor = ParagraphProcessor()
        tableProcessor = TableProcessor()
        listProcessor = ListProcessor()
        list_paragraphs = []

        for element in doc.element.body:
            logger.logn(f' < process {element.tag}')
            if element.tag.endswith("p"):
                paragraph = Paragraph(element, doc)

                list = ListProcessor.is_list(paragraph, doc)
                if list != None:
                    list_paragraphs.append(paragraph)
                else:
                    out = paragraphProcessor.process(paragraph)
                    if list_paragraphs:
                        # Call ListProcessor
                        out = listProcessor.process(list_paragraphs, doc) + "\n" + out
                        list_paragraphs.clear()

                    builder.add_element(out)

            elif element.tag.endswith("tbl"):  # Table
                table = Table(element, doc)
                out = tableProcessor.process(table)
                builder.add_element(out)
            elif element.tag.endswith("sectPr"): # End of section
                pass
            elif element.tag.endswith("sdt"): # Table of contents
                pass

            else:
                logger.errn(f'Unsuported tag: {element.tag}')

        if list_paragraphs: # Process last list. TODO: process bibliography
            # Call ListProcessor
            out = listProcessor.process(list_paragraphs, doc) + "\n"
            list_paragraphs.clear()
            builder.add_element(out)

        latex_document = builder.build()
        with open("out/output.tex", "w") as f:
            f.write(latex_document)                
        archive_path = shutil.make_archive("out", "zip", output_dir)

        return archive_path
