import streamlit as st
import tempfile
import os
from processors import WordProcessor

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''

st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

st.title("📝 Word2LaTeX Converter")
st.markdown(
    """
    Upload your **Word file (.docx)**, and we will convert it into **LaTeX code**.
    """
)

uploaded_file = st.file_uploader("⬆️ Upload DOCX file", type=["docx"])

if uploaded_file is not None:
    st.success("File successfully uploaded! 🎉")

    st.write("The file will be processed. Click the button below to get the result.")

    if st.button("🔄 Convert"):
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_path = temp_file.name

        # Process the file and get ZIP path
        archive_path = WordProcessor.process(temp_path)

        # Remove the temporary file after processing
        os.remove(temp_path)

        # Read ZIP file and provide download button
        with open(archive_path, "rb") as f:
            st.download_button(
                label="⬇️ Download ZIP",
                data=f,
                file_name="output.zip",
                mime="application/zip"
            )

        # Remove ZIP file after providing it for download
        os.remove(archive_path)

else:
    st.info("Please upload a DOCX file to get started.")
