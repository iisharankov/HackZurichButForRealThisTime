# Python script for mp3

import eyed3
import re

def is_sensitive(filename):
    audiofile = eyed3.load(filename)
    if audiofile is not None:
         if audiofile.tag.title or audiofile.tag.artist or re.search('dvd', audiofile.tag.comments[0].text):
                 return False 
         else:
             return None
    return False 