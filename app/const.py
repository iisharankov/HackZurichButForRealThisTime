import re

FILE_TYPES = ["csv", "db", "docx", "html", "jpg", "log", "md", "mp3", "msg", "pdf", "pem", "png", "ps1", "pub", "py", "txt", "xlsx", "xml", "zip"]

SENSITIVE_HEADERS = ["email", "name", "fullname", "full name", "full_name", "address", "phone", "iban"]
SENSITIVE_TOKENS = ["First Name", "First name", "first name", "Last Name", "Last name", "last name", "phone number", "Phone number", "Phone Number", "email"]

PATTERN_EMAIL = re.compile(r"\S+@\S+\.\S+")
PATTERN_IBAN = re.compile(r"(AD|AE|AL|AO|AT|AZ|BA|BE|BF|BG|BH|BI|BJ|BL|BY|BR|CH|CR|CY|CZ|CF|CG||CI|CM|CV|DE|DK|DO|DZ|EE|EG|ES|FI|FO|FR|GA|GB|GE|GI|GF|GL|GP|GR|GT|HR|HU|IE|IL|IQ|IS|IT|JO|KW|KZ|LB|LC|LI|LT|LU|LV|LY|MC|MD|ME|MF|MG|MK|MQ|MR|MT|MU|MZ|NI|NC|NL|NO|PF|PK|PL|PM|PS|PT|QA|RE|RO|RU|RS|SA|SE|SI|SM|SK|ST|TL|TF|TN|TR|VA|VG|WF|XK|YT)\d{16,32}")
PATTERN_RSA = re.compile(r"(-----BEGIN RSA PRIVATE KEY-----)(\s|\n)*MII(.|\n){10,1616}(-----END RSA PRIVATE KEY-----)")

ENCODINGS = ['utf-8', 'ISO-8859-1', 'windows-1252']
