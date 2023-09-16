# Python script for png

import easyocr

def is_sensitive(filename, detector):

    #predownload the Reader !!! 
    reader = easyocr.Reader(['en'])
    result = reader.readtext('filename', detail = 0)

    result = " ".join(result)

    return detector.is_sensitive(result)

