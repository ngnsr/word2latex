import argparse
from logger import Logger
from processors import WordProcessor

def main():
    parser = argparse.ArgumentParser(description="Convert a Word (.docx) document to LaTeX.")
    parser.add_argument("path", type=str, help="Path to the .docx file")

    args = parser.parse_args()

    logger = Logger()
    logger.log("Starting Word-to-LaTeX Translator")
    logger.off()

    word_processor = WordProcessor()
    word_processor.process(args.path)

    logger.on()
    logger.log(f"Tex file saved to : out/output.tex")
    logger.log("Finish")

if __name__ == "__main__":
    main()
