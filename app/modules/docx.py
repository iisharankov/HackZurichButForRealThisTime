# Python script for docx
import docx 
import numpy as np
import subprocess
import sys

def is_sensitive(filename, detector):
    # here: produce list of lines  from html 
    cmd = ["sh", "-c",
    "unzip -p " + str(filename) + " word/document.xml | sed -e 's/<[^>]\{1,\}>/ /g; s/[^[:print:]]\{1,\}/ /g'"]

    # Execute the command
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Check for errors
    result.check_returncode()

    counter = np.array(detector.is_sensitive(result.stdout))
    if (counter[0] > 0) or (counter[1]+counter[2] > 1) or (counter[1]+counter[3] > 1):
        return True 

    return False
