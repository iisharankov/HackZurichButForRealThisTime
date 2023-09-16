# Python script for png

import cv2
import pytesseract
from text_analyzer import text_is_sensitive

def is_sensitive(filename):

    img = cv2.imread(filename)   
    text = pytesseract.image_to_string(img)
    
    return text_is_sensitive(text) 

