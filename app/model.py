import re
import spacy
from phonenumbers import parse, is_valid_number, NumberParseException

import const

class SensitiveDataDetector:

    def __init__(self):

        # Create flags
        self.rsa_flag = 0
        self.direct_flag = 0
        self.indirect_flag = 0
        self.potential_indirect_flag = 0 


        self.nlp = spacy.load("en_core_web_sm")

        self.rsa_patterns = {
            "RSA private key": r"(-----BEGIN RSA PRIVATE KEY-----)?(\s|\n)*MII(.|\n){10,1616}(-----END RSA PRIVATE KEY-----)?",  # simplified pattern
        }

        self.direct_patterns = {
            # "Full Name": r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b",
            "Email Address": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            "Company name": r"\b[A-Z][a-z]+\s[A-Z][a-z]+(Co|Corp|Company|Inc|Ltd|GmbH|AG)\b",
            "RSA private key": r"-----BEGIN RSA PRIVATE KEY-----",  # simplified pattern
        }

        self.indirect_patterns = {
            "Address": r"\b\d+\s[A-Z][a-z]+(St|Ave|Blvd|Rd),\s[A-Z][a-z]+,\s[A-Z][a-z]+\b",
            "Phone number": r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b",
            "IBAN": r"\b[A-Z]{2}\d{2}[a-zA-Z0-9]{4}\d{7}\b"  # basic pattern for IBAN
        }

        self.potential_indirect_patterns = {
            "Nationality": r"\b[A-Z][a-z]+(ian|ish|ese)\b",  # simplified pattern
            "Age": r"\b\d{1,3}\syears?\sold\b",
            "Gender": r"\b(male|female)\b",
            "Professional qualification": r"\b(BSc|MSc|PhD|MD)\b"  # basic examples
        }

        
    def reset_flags(self):
        self.rsa_flag = 0
        self.direct_flag = 0
        self.indirect_flag = 0
        self.potential_indirect_flag = 0 



    def check_regex(self, text):
        for pattern in self.rsa_patterns.values():
            self.rsa_flag += len(re.findall(pattern, text))
        
        if self.rsa_flag:
            return

        for pattern in self.direct_patterns.values():
            self.direct_flag += len(re.findall(pattern, text))

        # if self.direct_flag == 0:
        #     self.direct_flag +=  self.has_full_name(text)


        for pattern in self.indirect_patterns.values():
            self.indirect_flag += len(re.findall(pattern, text))
        
        if self.direct_flag and self.indirect_flag:
            return
        

        for pattern in self.potential_indirect_patterns.values():
            count = sum(1 for _ in re.finditer(pattern, text))
            self.potential_indirect_flag += min(count, const.RE_ITER_LIMIT)
            # Exit early if we've already reached the limit
            if self.potential_indirect_flag >= const.RE_ITER_LIMIT:
                self.indirect_flag = const.RE_ITER_LIMIT
                break


            # self.potential_indirect_flag += len(re.findall(pattern, text)) 
        
        print(self.rsa_flag, self.direct_flag, self.indirect_flag, self.potential_indirect_flag)

    
    def has_full_name(self, text):
        english_nlp = spacy.load('en_core_web_sm')  
        spacy_parser = english_nlp(text)
        names = [ent.text for ent in spacy_parser.ents if ent.label_ == "PERSON"]

        for name in names:
            if len(name.split()) >= 2:
                return 1
        return 0


    def is_sensitive(self, text):
        self.reset_flags()


        # First do some fast regex tests!
        regex_result = self.check_regex(text)
        if regex_result:
            return True
    
        # direct, indirect, potential_indirect = self.detect_data(text)

        # if direct and (indirect or potential_indirect):
        #     return True

        return [self.rsa_flag, self.direct_flag, self.indirect_flag, self.potential_indirect_flag] 


