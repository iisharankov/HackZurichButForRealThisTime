"""
This is a simple crawler that you can use as a boilerplate for your own
implementation. The crawler labels `.txt` files that contain the word
"hello" as "true", `.txt` files without "hello" as "false" and every other
item as "review". Try to modify this simple implementation so that it finds
some sensitive data and then expand your crawler from there.

You can change the code however you want, just make sure that following
things are satisfied:

- Grab the files from the directory "../files" relative to this script
- If you use Python packages, add a "requirements.txt" to your submission
- If you need to download larger files, e.g. NLP models, don't add them to
  the `app` folder. Instead, download them when the Docker image is build by
  changing the Docker file.
- Save your labels as a pickled dictionary in the `../results` directory.
  Use the filename as the key and the label as the value for each file.
- Your code cannot the internet during evaluation. Design accordingly.
"""

import os
from pathlib import Path
import pickle
import importlib
import time

import pandas as pd

import const
import model
import modules
from modules import csv, db, docx, html, jpg, log, md, mp3, msg, other, pdf, pem, png, ps1, pub, py, txt, xlsx, xml, zip






def classifier(file_path, detector):
    # Check the data type
    for extension in const.FILE_TYPES:
        

        match file_path.suffix[1:]:
            # case "csv":
            #     return csv.is_sensitive(file_path, detector)
            # case "db":
            #     return db.is_sensitive(file_path, detector)
            # case "docx":
            #     return docx.is_sensitive(file_path, detector)
            # case "html":
            #     return html.is_sensitive(file_path, detector)
            # case "jpg":
            #     return jpg.is_sensitive(file_path, detector)
            # case "log":
            #     return log.is_sensitive(file_path, detector)
            # case "md":
            #     return md.is_sensitive(file_path, detector)
            # case "mp3":
            #     return mp3.is_sensitive(file_path, detector)
            # case "msg":
                # return msg.is_sensitive(file_path, detector)
            case "pdf":
                return pdf.is_sensitive(file_path, detector)
            # case "pem":
            #     return pem.is_sensitive(file_path, detector)
            # case "png":
            #     return png.is_sensitive(file_path, detector)
            # case "ps1":
            #     return ps1.is_sensitive(file_path, detector)
            # case "pub":
            #     return pub.is_sensitive(file_path, detector)
            # case "py":
            #     return py.is_sensitive(file_path, detector)
            # case "txt":
            #     return txt.is_sensitive(file_path, detector)
            # case "xlsx":
            #     return xlsx.is_sensitive(file_path, detector)
            # case "xml":
            #     return xml.is_sensitive(file_path, detector)
            # case "zip":
            #     return zip.is_sensitive(file_path, detector)
            # case _:
            #     return other.is_sensitive(file_path, detector)

    return None
    


def main():

    # Init detector
    detector = model.SensitiveDataDetector()

    # Get the path of the directory where this script is in
    script_dir_path = Path(os.path.realpath(__file__)).parents[1]

    # Get the path containing the files that we want to label
    file_dir_path = script_dir_path / "files"


    # print(file_dir_path)
    if os.path.exists(file_dir_path):

        # Initialize the label dictionary
        labels = {}

        start = time.time()
        # Loop over all items in the file directory
        for file_name in os.listdir(file_dir_path):
            file_path = file_dir_path / file_name

            result = classifier(file_path, detector)

            # add result to labels
            if result is None:
                result = "Review"
            labels[file_name] = result


        time_tot = time.time() - start
        print(f"total time was {time_tot}")
        # Convert dictionary to DataFrame
        df = pd.DataFrame(list(labels.items()), columns=['key', 'value'])

        # Save the DataFrame to a CSV
        df.to_csv(script_dir_path / 'results' / 'crawler_results.csv', index=False)

    else:
        print("Please place the files in the corresponding folder")

    # print(labels)
if __name__ == "__main__":
    main()
