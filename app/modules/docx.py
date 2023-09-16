# Python script for docx
import docx 
import numpy as np

def is_sensitive(filename, detector):
    # here: produce list of lines  from html 

    doc = docx.Document("your_file.docx")
    counter = np.array([0,0,0,0])

    for paragraph in doc:
        new_count = np.array(detector.is_sensitive(paragraph.text))
        counter += new_count 
        if (counter[0] > 0) or (counter[1]+counter[2] > 1) or (counter[1]+counter[3] > 1):
            return True 

    return False

# return detector.is_sensitive(text)