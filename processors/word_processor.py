from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

from document_builder import LatexDocumentBuilder
from logger import Logger

from .paragraph_processor import ParagraphProcessor
from .table_processor import TableProcessor
import os

class WordProcessor():
    def process(self, file_path: str):
        logger = Logger()
        logger.logn(f'Start processing file with path: {file_path}')

        doc = Document(file_path)
        # print(doc.element.body.xml)
        # exit(0)
        images = []
        # imagesCount = 0

        # fonts should be tracked and added 
        builder = LatexDocumentBuilder()

        # make sure out dir exists if not - create
        output_dir = "out/img"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        if not os.path.exists(output_dir):
            logger.logn("can't create out directory")
            exit(-1)

        # write images to out dir
        imagesCount = 0
        for idx, rel in enumerate(doc.part.rels):
            if "image" in doc.part.rels[rel].target_ref:
                image_data = doc.part.rels[rel].target_part.blob
                images.append(image_data)
                image_path = os.path.join(output_dir, f"img{imagesCount}.png")
                with open(image_path, "wb") as img_file:
                    img_file.write(image_data)
                print(f"Image {idx} saved as {image_path}")
                imagesCount+=1

        logger.logn(f'Founded {images.__len__()} images.')
        paragraphProcessor = ParagraphProcessor()
        tableProcessor = TableProcessor()

        for element in doc.element.body:
            # logger.logn(f' < process {element.tag}')
            # print(element.tag)
            if element.tag.endswith("p"):
                # logger.logn('< process paragraph')
                paragraph = Paragraph(element, None)
                out = paragraphProcessor.process(paragraph)
                builder.add_element(out)

            elif element.tag.endswith("tbl"):  # Таблиця
                # logger.logn('< process table')
                table = Table(element, None)
                out = tableProcessor.process(table)
                builder.add_element(out)
            elif element.tag.endswith("sectPr"): # end of section
                pass
            elif element.tag.endswith("sdt"):
                pass

            else:
                logger.errn(f'Unsuported tag: {element.tag}')
                
        return builder.build()

