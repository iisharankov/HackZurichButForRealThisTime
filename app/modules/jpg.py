# Python script for jpg

import numpy as np

def is_sensitive(filename, detector, reader):
    result = reader.readtext(str(filename), detail = 0)
    
    counter = np.array(detector.is_sensitive(result))
    if (counter[0] > 0) or (counter[1]+counter[2] > 1) or (counter[1]+counter[3] > 1):
        return True 

    return False 


