# Python script for png

import easyocr
import numpy as np

import helpers
def is_sensitive(filename, detector):

    #predownload the Reader !!! 
    reader = easyocr.Reader(['en'])
    result = reader.readtext(filename, detail = 0)

    counter = np.array(detector.is_sensitive(result))
    return helpers.check_valid_sensitivities(counter)
