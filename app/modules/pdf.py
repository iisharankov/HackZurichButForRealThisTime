
import subprocess

import numpy as np
import helpers

# Maybe faster?
def extract_text_from_pdf(pdf_path):
    # Use subprocess to run pdftotext and capture output
    result = subprocess.run(["pdftotext", "-q", pdf_path, "-"], stdout=subprocess.PIPE)
    
    # Check if the process completed successfully
    result.check_returncode()
    
    # Convert bytes to string and return
    return result.stdout.decode('utf-8')


def is_sensitive(file_path, detector):

    text = extract_text_from_pdf(file_path)
    
    counter = np.array(detector.is_sensitive(text))
    return helpers.check_valid_sensitivities(counter)
    