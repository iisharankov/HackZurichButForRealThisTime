# Python script for jpg

import easyocr
import numpy as np

def is_sensitive(filename, detector):

    #predownload the Reader !!! 
    reader = easyocr.Reader(['en'])
    result = reader.readtext(filename, detail = 0)

    counter = np.array([0,0,0,0])

    for line in result:
        new_count = np.array(detector.is_sensitive(line))
        counter += new_count
        if (counter[0] > 0) or (counter[1]+counter[2] > 1) or (counter[1]+counter[3] > 1):
            return True 

    return False 


