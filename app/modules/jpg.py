# Python script for jpg

import numpy as np

import helpers

def is_sensitive(filename, detector, reader):
    result = reader.readtext(str(filename), detail = 0)
    
    counter = np.array(detector.is_sensitive(result))
    return helpers.check_valid_sensitivities(counter)


