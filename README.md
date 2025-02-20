# Word2LaTeX

## Project Description
`word2latex` is a tool for converting Microsoft Word (`.docx`) documents into LaTeX format.

## Installation & Setup

### 1. Clone the repository
```sh
 git clone https://github.com/ngnsr/word2latex.git
 cd word2latex
```

### 2. Create and activate a virtual environment (recommended)
```sh
 python3 -m venv venv
 source ./venv/bin/activate  # for Linux/macOS
 venv\Scripts\activate     # for Windows
```

### 3. Install dependencies
```sh
 ./venv/bin/pip install python-docx streamlit
```

### 4. Run the web interface
```sh
 ./venv/bin/streamlit run webui.py
```

## Usage Example
1. Open the web interface in a browser after launching `streamlit`.
2. Upload a `.docx` file.
3. View the generated LaTeX code.
4. Copy or download the result for further use.
