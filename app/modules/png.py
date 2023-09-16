# Python script for png

from cv2 import imread
from pytesseract import image_to_string
from text_analyzer import text_is_sensitive
import easyocr

def is_sensitive(filename):

    #predownload the Reader
    reader = easyocr.Reader(['en'])
    result = reader.readtext('filename', detail = 0)

    result = " ".join(result)
    
    return text_is_sensitive(result) 

