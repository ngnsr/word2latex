from processors import *

class ProcessorFactory:
    @staticmethod
    def get_processor(element_type):
        if element_type == "text":
            return ParagraphProcessor()
        elif element_type == "table":
            return TableProcessor()
        elif element_type == "image":
            return DrawingProcessor()
        else:
            raise ValueError(f"Unsupported element type: {element_type}")
