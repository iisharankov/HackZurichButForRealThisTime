# Python script for html
from bs4 import BeautifulSoup
import re

def is_sensitive(filename, detector):
    # here: produce list of lines  from html 

    with open(filename, "r", encoding="utf-8") as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, "html.parser")
    plain_text = soup.get_text()
    text = re.split(r'[\n\t\f\v\r]+', plain_text) # this is a list of strings!! 
    
    return detector.is_sensitive(text)
