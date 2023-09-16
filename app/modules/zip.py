# Python script for zip
import zipfile
import os

def extract_text_from_zip(zip_path):
    text_content = None

    def process_zip(z_path):
        nonlocal text_content
        with zipfile.ZipFile(z_path, 'r') as z:
            for item in z.namelist():
                _, ext = os.path.splitext(item)  # Get the file extension
                if ext == ".zip":  # If item is a zip file, extract and process it
                    with z.open(item) as nested_zip:
                        temp_path = "temp_inner_zip.zip"
                        with open(temp_path, 'wb') as f:
                            f.write(nested_zip.read())
                        process_zip(temp_path)
                        os.remove(temp_path)
                elif ext == ".txt":
                    with z.open(item) as txt_file:
                        text_content = txt_file.read().decode()  # Decode bytes to string
                        return

    process_zip(zip_path)
    return text_content

# Example
zip_file_path = "/content/budget-game-their.zip"
text_content = extract_text_from_zip(zip_file_path)
if text_content:
    print(text_content)
else:
    print("No text file found inside the zip (and nested zips).")
