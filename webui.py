import streamlit as st

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''

st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# st.set_page_config(page_title="Word-to-LaTeX Converter", page_icon="📝", layout="centered")

st.title("📝 Word2LaTeX Converter")
st.markdown(
    """
    Завантажте ваш **Word файл (.docx)**, і ми перетворимо його в **LaTeX код**.
    """
)

uploaded_file = st.file_uploader("⬆️  Завантажте DOCX файл", type=["docx"])

if uploaded_file is not None:
    st.success("Файл успішно завантажений! 🎉")

    st.write("Файл буде оброблено, натисніть кнопку нижче, щоб отримати результат.")

    latex_content = "Ваш згенерований LaTeX-код з'явиться тут."

    if st.button("🔄 Перетворити"):
        st.code(latex_content, language="latex")
        st.download_button(
            label="⬇️ Завантажити LaTeX",
            data=latex_content,
            file_name="output.tex",
            mime="text/plain"
        )
else:
    st.info("Будь ласка, завантажте DOCX файл для початку роботи.")

# import streamlit as st
#
# # Словник перекладів
# translations = {
#     "en": {
#         "title": "Word to LaTeX Converter",
#         "upload_prompt": "Upload your Word (.docx) file",
#         "convert_button": "Convert to LaTeX",
#     },
#     "uk": {
#         "title": "Конвертер Word у LaTeX",
#         "upload_prompt": "Завантажте ваш Word (.docx) файл",
#         "convert_button": "Перетворити в LaTeX",
#     }
# }
#
# # CSS для вирівнювання кнопок у рядку праворуч
# st.markdown(
#     """
#     <style>
#     .language-buttons-container {
#         display: flex;
#         justify-content: flex-end;
#         align-items: center;
#         gap: 5px;
#         margin-bottom: 10px;
#     }
#     .language-button {
#         border: none;
#         background: none;
#         padding: 0;
#         cursor: pointer;
#     }
#     .language-button img {
#         width: 30px;
#         height: 30px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
#
# # Ініціалізація стану мови
# if "language" not in st.session_state:
#     st.session_state.language = "en"
#
# # Відображення кнопок вибору мови
# st.markdown('<div class="language-buttons-container">', unsafe_allow_html=True)
# col1, col2 = st.columns([1, 10])
# with col1:
#     if st.button("🇺🇦", key="uk_button"):
#         st.session_state.language = "uk"
#     if st.button("🇬🇧", key="en_button"):
#         st.session_state.language = "en"
# st.markdown('</div>', unsafe_allow_html=True)
#
# # Поточна мова
# language = st.session_state.language
# t = translations[language]
#
# # Інтерфейс користувача
# st.title(t["title"])
#
# uploaded_file = st.file_uploader(t["upload_prompt"], type=["docx"])
#
# if st.button(t["convert_button"]):
#     if uploaded_file is not None:
#         st.success("✅ File successfully converted!")
#     else:
#         st.error("⚠️ Please upload a file!")
