from logger import Logger
from processors import WordProcessor

if __name__ == "__main__":
    logger = Logger()
    logger.log("Starting Word-to-LaTeX Translator")

    wordProcessor = WordProcessor()

    # latex_document = wordProcessor.process("/home/rr/proj/word2latex/document_examples/page_break_test.docx")
    latex_document = wordProcessor.process("/home/rr/Downloads/Щоденник_практики_ЗРАЗОК.docx")

    with open("out/output.tex", "w") as f:
        f.write(latex_document)

    logger.log("Finish")
