
class LatexDocumentBuilder:
    def __init__(self):
        self.content = []
        self._initialize_document()

    def _initialize_document(self):
        # Add initial LaTeX packages and document setup
        self.content.append("\\documentclass{article}")

        self.content.append("\\usepackage[utf8]{inputenc}")
        self.content.append("\\usepackage[T2A]{fontenc}")
        self.content.append("\\usepackage[ukrainian]{babel}")

        self.content.append("\\usepackage{graphicx}")
        self.content.append("\\usepackage{amsmath}")
        self.content.append("\\usepackage{hyperref}")
        self.content.append("\\begin{document}")

    def _post_construct_document(self):
        self.content.append("\\end{document}")

    def add_element(self, element):
        self.content.append(element)

    def build(self):
        self._post_construct_document()
        print(self.content)

        

        self.content = [item if item != '' else '\\newline' for item in self.content]

        return "\n".join(part for part in self.content)
        # return "\n".join(part for part in self.content if part is not None)
