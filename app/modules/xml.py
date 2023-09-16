# Python script for xml

import chardet
import numpy as np
from xml.etree import cElementTree as ET
import os 

def is_sensitive(filename, detector):

    with open('dict.xml', 'r') as f:
        data = f.read()

    def read_text_from_file(file_path):
        """Reads and returns the content of a file using the appropriate encoding."""
        
        with open(file_path, 'rb') as file:
            rawdata = file.read()
            
        encoding_detected = chardet.detect(rawdata)['encoding']
        
        # List of encodings to try:
        encodings_to_try = [encoding_detected, 'utf-8', 'ISO-8859-1', 'windows-1252']
        
        for encoding in encodings_to_try:
            try:
                content = rawdata.decode(encoding)
                return content
            except UnicodeDecodeError:
                pass

        # If we've tried all encodings and none worked, then the file might contain binary or non-textual data
        return ''


    
    Bs_data = BeautifulSoup(data, "xml")
    b_unique = Bs_data.find_all('unique')

    for line in plain_text:
        new_count = np.array(detector.is_sensitive(line))
        counter += new_count 
        if (counter[0] > 0) or (counter[1]+counter[2] > 1) or (counter[1]+counter[3] > 1):
            return True 

    return False



def read_text_from_file(file_path):
        """Reads and returns the content of a file using the appropriate encoding."""
        
        with open(file_path, 'rb') as file:
            rawdata = file.read()
            
        encoding_detected = chardet.detect(rawdata)['encoding']
        
        # List of encodings to try:
        encodings_to_try = [encoding_detected, 'utf-8', 'ISO-8859-1', 'windows-1252']
        
        for encoding in encodings_to_try:
            try:
                content = rawdata.decode(encoding)
                return content
            except UnicodeDecodeError:
                pass

        # If we've tried all encodings and none worked, then the file might contain binary or non-textual data
        return ''

for filename in os.listdir('files'):
    if '.xml' in filename:
        content = read_text_from_file('files/'+filename)
        print(content[:200])
        print('--------------------')
