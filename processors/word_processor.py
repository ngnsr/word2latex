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

import ollama

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
        first_page_processed = False
        page_paragraphs = []

        for element in doc.element.body:
            logger.logn(f' < process {element.tag}')
            if element.tag.endswith("p"):
                paragraph = Paragraph(element, doc)

                if not first_page_processed:
                    if ParagraphProcessor.has_page_break(paragraph) or ParagraphProcessor.has_title(paragraph):
                        print('process page: ')
                        print(page_paragraphs)
                        latex = self.process_first_page(page_paragraphs, builder)
                        print('----------')
                        print(latex)
                        if latex:
                            builder.add_element(latex)
                        first_page_processed = True
                    else:
                        page_paragraphs.append(paragraph.text)

                    continue

                # list = ListProcessor.is_list(paragraph, doc)
                list = ListProcessor.is_list(paragraph, doc)
                if list != None:
                    list_paragraphs.append(paragraph)
                else:
                    out = paragraphProcessor.process(paragraph)
                    if list_paragraphs:
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

        if list_paragraphs: # Process last list. Prob should check for bibliography and do smth else
            # Call ListProcessor
            out = self.listProcessor.process(list_paragraphs, doc) + "\n"
            list_paragraphs.clear()
            builder.add_element(out)

                
        return builder.build()

    def process_first_page(self, page_paragraphs, builder):
        if not page_paragraphs:
            return
        
        page_text = "\n".join(page_paragraphs)
        
        check_prompt = (
            "Is the following text a title page? A title page typically appears at the beginning of a document and includes elements like institution name, course title, author(s), document type, and date. "
            "Reply only with 'true' or 'false'.\n\n" + page_text
        )
        
        check_response = ollama.chat(model="phi3", messages=[{"role": "user", "content": check_prompt}], options={"temperature": 0.2})
        print(check_response.get("message", {}).get("content", "false"))
        is_title_page = check_response.get("message", {}).get("content", "false").strip().lower().startswith("true")
        
        if is_title_page:
            generate_prompt = ("Generate a properly formatted LaTeX title page using the following text as content. "
                               "Ensure the output includes a structured layout with title, author(s), institution, and date, following LaTeX conventions. "
                               "Preserve formatting details that are relevant and structure them appropriately in LaTeX. "
                               "Ensure that the generated title page properly reflects the document type (e.g., lab report, dissertation, or academic paper).\n\n" + page_text)
            
            response = ollama.chat(model="phi3", messages=[{"role": "user", "content": generate_prompt}])
            latex_output = response.get("message", {}).get("content", "")
            
            if latex_output:
                builder.add_element(latex_output)
            else:
                builder.add_element(page_text) # TODO: rm -rf /