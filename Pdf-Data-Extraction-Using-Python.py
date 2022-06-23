print("")

from PyPDF2 import PdfReader
# Regular Expression to Filter Data
import re
reader = PdfReader("CV-demo-1.pdf")
number_of_pages = len(reader.pages)
page_count = reader.getNumPages()
page = reader.pages[0]
text = page.extract_text()
text = text.replace('\n','')
print(text)
# Email Extraction
email = re.search(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)',text).group()
print(email)
phone_num = re.search(r'(?:\+?\d{2}[ -]?)?\d{10}',text).group()
print(phone_num)