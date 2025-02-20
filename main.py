from logger import Logger
from processors import WordProcessor

if __name__ == "__main__":
    logger = Logger()

    logger.log("Starting Word-to-LaTeX Translator")
    logger.off()

    wordProcessor = WordProcessor()

    wordProcessor.process("/home/rr/proj/word2latex/document_examples/К25_Звіт_Рісенгін.docx")
    # wordProcessor.process("/home/rr/proj/word2latex/document_examples/lists_example.docx")
    # wordProcessor.process("/home/rr/proj/word2latex/document_examples/inner_list_example.docx")
    # wordProcessor.process("/home/rr/proj/word2latex/document_examples/list_in_table.docx")
    # wordProcessor.process("/home/rr/Downloads/Щоденник_практики_ЗРАЗОК.docx")
    # wordProcessor.process("/home/rr/proj/word2latex/document_examples/titles_example.docx")
    # wordProcessor.process("/home/rr/proj/word2latex/document_examples/bullet_list_inside_enum_list_example.docx")

    logger.on()
    logger.log("Tex file saved to : out/output.tex")
    logger.log("Finish")
