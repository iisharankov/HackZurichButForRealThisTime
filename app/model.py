import re
import spacy
from phonenumbers import parse, is_valid_number, NumberParseException


class SensitiveDataDetector:

    def __init__(self):

        # Create flags
        self.rsa_flag = 0
        self.direct_flag = 0
        self.indirect_flag = 0
        self.potential_indirect_flag = 0 


        self.nlp = spacy.load("en_core_web_sm")

        self.direct_patterns = {
            # "Full Name": r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b",
            "Email Address": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            "Company name": r"\b[A-Z][a-z]+\s[A-Z][a-z]+(Co|Corp|Company|Inc|Ltd)\b",
            "RSA private key": r"-----BEGIN RSA PRIVATE KEY-----",  # simplified pattern
        }

        self.indirect_patterns = {
            "Address": r"\b\d+\s[A-Z][a-z]+(St|Ave|Blvd|Rd),\s[A-Z][a-z]+,\s[A-Z][a-z]+\b",
            "Phone number": r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b",
            # "IBAN": r"\b[A-Z]{2}\d{2}[a-zA-Z0-9]{4}\d{7}\b"  # basic pattern for IBAN
            "IBAN": r"\b([A-Z]{2}[ '+'\\\\'+'-]?[0-9]{2})(?=(?:[ '+'\\\\'+'-]?[A-Z0-9]){9,30}\$)((?:[ '+'\\\\'+'-]?[A-Z0-9]{3,5}){2,7})([ '+'\\\\'+'-]?[A-Z0-9]{1,3})?\b"
        }

        self.potential_indirect_patterns = {
            "Nationality": r"\b[A-Z][a-z]+(ian|ish|ese)\b",  # simplified pattern
            "Age": r"\b\d{1,3}\syears?\sold\b",
            "Gender": r"\b(male|female)\b",
            "Professional qualification": r"\b(BSc|MSc|PhD|MD)\b"  # basic examples
        }


    # def regex2(self):
    #     PATTERN_EMAIL = re.compile(r"\S+@\S+\.\S+")
    #     PATTERN_IBAN = re.compile(r"(AD|AE|AL|AO|AT|AZ|BA|BE|BF|BG|BH|BI|BJ|BL|BY|BR|CH|CR|CY|CZ|CF|CG||CI|CM|CV|DE|DK|DO|DZ|EE|EG|ES|FI|FO|FR|GA|GB|GE|GI|GF|GL|GP|GR|GT|HR|HU|IE|IL|IQ|IS|IT|JO|KW|KZ|LB|LC|LI|LT|LU|LV|LY|MC|MD|ME|MF|MG|MK|MQ|MR|MT|MU|MZ|NI|NC|NL|NO|PF|PK|PL|PM|PS|PT|QA|RE|RO|RU|RS|SA|SE|SI|SM|SK|ST|TL|TF|TN|TR|VA|VG|WF|XK|YT)\d{16,32}")


    #     def regex_filter(string):
    #         return {
    #         "email": re.search(PATTERN_EMAIL, string) is not None,
    #         "iban": re.search(PATTERN_IBAN, string) is not None
    #         }
        
    def reset_flags(self):
        self.rsa_flag = 0
        self.direct_flag = 0
        self.indirect_flag = 0
        self.potential_indirect_flag = 0 


    def check_regex(self, text):
        for pattern in self.direct_patterns.values():
            self.direct_flag += len(re.findall(pattern, text))
        
        for pattern in self.indirect_patterns.values():
            self.indirect_flag += len(re.findall(pattern, text))

        for pattern in self.potential_indirect_patterns.values():
            self.potential_indirect_flag += len(re.findall(pattern, text))
        
        print(self.rsa_flag, self.direct_flag, self.indirect_flag, self.potential_indirect_flag)

    

    def is_valid_phone(self, text):
        try:
            number = parse(text, None)
            return is_valid_number(number)
        except NumberParseException:
            return False

    # def detect_data(self, text):
    #     doc = self.nlp(text)

    #     direct_detected = any([ent.label_ in ["PERSON", "ORG", "EMAIL"] for ent in doc.ents]) or "-----BEGIN RSA PRIVATE KEY-----" in text
    #     indirect_detected = any([ent.label_ in ["GPE", "LOC"] for ent in doc.ents]) or self.is_valid_phone(text)
    #     potential_indirect_detected = any([word in text.lower() for word in ["male", "female", "bsc", "msc", "phd", "md"]])

    #     return direct_detected, indirect_detected, potential_indirect_detected

    def is_sensitive(self, text):
        self.reset_flags()


        # First do some fast regex tests!
        regex_result = self.check_regex(text)
        if regex_result:
            return True
    
        # direct, indirect, potential_indirect = self.detect_data(text)

        # # RSA private key is always sensitive
        # if "-----BEGIN RSA PRIVATE KEY-----" in text:
        #     return True

        # if direct and (indirect or potential_indirect):
        #     return True

        return [self.rsa_flag, self.direct_flag, self.indirect_flag, self.potential_indirect_flag] 

if __name__ == '__main__':
    detector = SensitiveDataDetector()
    text = input("Enter text: ")

    if detector.is_sensitive(text):
        print("Sensitive Data detected.")
    else:
        print("NON-sensitive data.")
