# import streamlit as st
# from word_processor import process_docx
# import tempfile
# from PIL import Image
# from io import BytesIO
#
# uploaded_file = st.file_uploader("Завантажте DOCX-файл", type=["docx"])
#
# if uploaded_file:
#     st.write("Обробляємо файл...")
#
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
#         temp_file.write(uploaded_file.read())
#         temp_file_path = temp_file.name
#
#     result = process_docx(temp_file_path)
#
#     if isinstance(result, dict):
#         st.subheader("Текстовий контент:")
#         for text in result["text"]:
#             st.text(text)
#
#         st.subheader("Таблиці:")
#         for i, table in enumerate(result["tables"]):
#             st.write(f"Таблиця {i + 1}:")
#             st.table(table)
#
#         st.subheader("Зображення:")
#         for i, img_blob in enumerate(result["images"]):
#             image = Image.open(BytesIO(img_blob))
#             st.image(image, caption=f"Зображення {i + 1}")
#
#     else:
#         st.error(result)

# import streamlit as st
# from word_processor import process_docx
# import tempfile
# from PIL import Image
# from io import BytesIO
#
# uploaded_file = st.file_uploader("Завантажте DOCX-файл", type=["docx"])
#
# if uploaded_file:
#     st.write("Обробляємо файл...")
#
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
#         temp_file.write(uploaded_file.read())
#         temp_file_path = temp_file.name
#
#     result = process_docx(temp_file_path)
#
#     if isinstance(result, dict):
#         st.subheader("Вміст документа:")
#         for item in result["content"]:
#             if item["type"] == "text":
#                 st.text(item["value"])
#             elif item["type"] == "table":
#                 st.write("Таблиця:")
#                 st.table(item["value"])
#             elif item["type"] == "image":
#                 st.write("Зображення:")
#                 image = Image.open(BytesIO(item["value"]))
#                 st.image(image)
#     else:
#         st.error(result)

import streamlit as st
from processors.word_processor import process_docx
import tempfile
from PIL import Image
from io import BytesIO

uploaded_file = st.file_uploader("Завантажте DOCX-файл", type=["docx"])

if uploaded_file:
    st.write("Обробляємо файл...")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    result = process_docx(temp_file_path)

    if isinstance(result, dict):
        st.subheader("Вміст документа:")
        for item in result["content"]:
            if item["type"] == "text":
                st.text(item["value"])
            elif item["type"] == "table":
                st.write("Таблиця:")
                st.table(item["value"])
            elif item["type"] == "image":
                st.write("Зображення:")
                image = Image.open(BytesIO(item["value"]))
                st.image(image)
    else:
        st.error(result)
