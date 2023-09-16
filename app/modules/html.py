# Python script for html
from bs4 import BeautifulSoup
import re
import numpy as np

def is_sensitive(filename, detector):
    # here: produce list of lines  from html 

    with open(filename, "r", encoding="utf-8") as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, "html.parser")
    plain_text = soup.get_text()
    text = re.split(r'[\n\t\f\v\r]+', plain_text) # this is a list of strings!! 
    counter = np.array([0,0,0,0])
    for line in text:
        new_count = np.array(detector.is_sensitive(line))
        counter += new_count 
        if (counter[0] > 0) or (counter[1]+counter[2] > 1) or (counter[1]+counter[3] > 1):
            return True 

    return False


    return detector.is_sensitive(text)
