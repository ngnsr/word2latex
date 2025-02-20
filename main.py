from logger import Logger
from processors import WordProcessor

if __name__ == "__main__":
    logger = Logger()

    logger.log("Starting Word-to-LaTeX Translator")
    logger.off()

    wordProcessor = WordProcessor()

    latex_document = wordProcessor.process("/Users/rr/proj/word2latex/document_examples/К25_Звіт_Рісенгін.docx")
    # latex_document = wordProcessor.process("/Users/rr/proj/word2latex/document_examples/lists_example.docx")
    # latex_document = wordProcessor.process("/Users/rr/proj/word2latex/document_examples/inner_list_example.docx")
    # latex_document = wordProcessor.process("/Users/rr/proj/word2latex/document_examples/list_in_table.docx")
    # latex_document = wordProcessor.process("/Users/rr/Downloads/Щоденник_практики_ЗРАЗОК.docx")
    # latex_document = wordProcessor.process("/Users/rr/proj/word2latex/document_examples/titles_example.docx")
    # latex_document = wordProcessor.process("/Users/rr/proj/word2latex/document_examples/bullet_list_inside_enum_list_example.docx")

    with open("out/output.tex", "w") as f:
        f.write(latex_document)

    logger.on()
    logger.log("Tex file saved to : out/output.tex")
    logger.log("Finish")
