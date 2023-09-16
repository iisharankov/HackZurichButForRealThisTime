# Python script for xlsx

import pandas as pd
import re

from const import *

def regex_filter(string): 
    return {
        "email": re.search(PATTERN_EMAIL, string) is not None, 
        "iban": re.search(PATTERN_IBAN, string) is not None
    }

def is_sensitive(filename, detector = None): 

    df = pd.read_excel(filename, nrows = 20)

    # Check 1: Has header
    has_header = not any([not isinstance(col, str) for col in df.columns])
    if has_header: # If there is a header

        headers = df.columns
        headers = [col.lower().strip() for col in df.columns]

        if sum(sens in headers for sens in SENSITIVE_HEADERS) > 1: 
            # print("Check 1", filename)
            return True

    # Check 2: Has email or IBAN

    df_string = df.__str__()
    regex = regex_filter(df_string)
    has_email, has_iban = regex["email"], regex["iban"]

    if has_email and not "git@" in df_string: # Only true if it isn't github email...
        # print("Check 2 (MAIL)", filename)
        return  True 
    
    if has_iban: 
        # print("Check 2 (IBAN)", filename)
        return True
    
    # Check 3: Has a sensitive token in it
    if sum(sens in df_string for sens in SENSITIVE_TOKENS) > 1: 
        # print("Check 3", filename)
        return True

    return False