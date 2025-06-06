from docx.table import Table

from .paragraph_processor import ParagraphProcessor
from .element_processor import ElementProcessor
from logger import Logger

class TableProcessor(ElementProcessor):

    def __init__(self):
        self.logger = Logger()
        self.paragraphProcessor = ParagraphProcessor()


    def process(self, element: Table):
        self.logger.logn("> process table")
        res = []
        table = element
        columnNum = 0
        if table and table.rows[0]: columnNum = table.rows[0].cells.__len__()

        # self.logger.logn(f"# columnNum {columnNum}")
        # \begin{tabular}{|c|c|...|c|} 
        # \hline
        # val & val & ... & val \\
        # \hline
        # \end{tabular}

        res.append("\\begin{tabular}{" + "|l"*columnNum + "|}")
        for row in table.rows:
            res.append('\\hline')
            out = ''
            for idx, cell in enumerate(row.cells):
                for paragraph in cell.paragraphs:
                    # TODO: process enum/bullet lists
                    out = out + self.paragraphProcessor.process(paragraph).removesuffix("\\newline")
                    if idx  < columnNum - 1: out = out + " & " 
            res.append(out.replace('\n', '') + ' \\\\')
                    
        res.append("\\hline")
        res.append("\\end{tabular}")
        return '\n'.join(res)
