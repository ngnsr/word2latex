import os
import zipfile

def extract_images_from_docx(docx_file, output_dir="out/img"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with zipfile.ZipFile(docx_file, 'r') as docx_zip:
        media_files = [f for f in docx_zip.namelist() if f.startswith("word/media/")]

        for media_file in media_files:
            filename = os.path.basename(media_file)
            output_path = os.path.join(output_dir, filename)

            with docx_zip.open(media_file) as source, open(output_path, 'wb') as target:
                target.write(source.read())
                print(f"Image {filename} saved to {output_path}")

