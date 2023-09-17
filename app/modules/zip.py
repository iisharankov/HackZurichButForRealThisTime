# Python script for zip
import os
import zipfile
import numpy as np

def process_zip(z_path, text_content):
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
                    text_content.append(txt_file.read().decode())  # Decode bytes to string
                    return


def extract_text_from_zip(zip_path):
    text_content = []
    process_zip(zip_path, text_content)
    return " ".join(text_content)


def is_sensitive(filename, detector):
    # here: produce list of lines  from html 

    doc = process_zip(filename)

    conuter = np.array(detector.is_sensitive(doc))
    return helpers.check_valid_sensitivities(counter)