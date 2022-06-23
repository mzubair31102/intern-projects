print("---------CV Data Extraction---------")
from PyPDF2 import PdfReader
# Regular Expression to Filter Data
import re
reader = PdfReader("CV-demo-1.pdf")
number_of_pages = len(reader.pages)
page_count = reader.getNumPages()
page = reader.pages[0]
text = page.extract_text()
text = text.replace('\n','')
text = text.lower()
print(text)
# Name Extraction using multiple Expressions in single line
print("---------First Name Extraction---------")
f_name = ""
if "name" in text:
    start_index = text.find("name")
    for i in range(start_index+6,start_index+200):
        f_name+=text[i]
        if " " in  text[i]:
            break
elif "dear" in text:
    start_index = text.find("dear")
    for i in range(start_index+6,start_index+200):
        f_name+=text[i]
        if " " in  text[i]:
            break

print(f_name.capitalize())
print("---------Last Name Extraction---------")
l_name= ""
if f_name in text:
    start_index = text.find(f_name)
    length_of_f_n = len(f_name)
    for i in range(start_index+length_of_f_n,start_index+200):
        l_name+=text[i]
        if " " in  text[i]:
            break
print(l_name.capitalize())
# Email Extraction
print("---------Email Extraction---------")
email = re.search(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)',text).group()
print(email)
"""
Expression for Mobile Formats 
03024483861
0302-4483861
"""
print("---------Phone Number Extraction---------")
phone_num = re.search(r'(\d{4}[*-]?\d{7})',text).group()
print(phone_num)
print("---------Programming Skills Extraction---------")
found_skills=""
skills_list = ['html','css','bootsrap','javascript','java','php','python','dart',]
for i in skills_list:
    if i in text:
        found_skills=found_skills+i+","
print(found_skills)


"""
get_f_name = re.compile("(?<=name: ).*?(?=\s)")
print(get_f_name.findall(text))
get_l_name = re.compile("(get_f_name).*?(?=\s)")
print(get_l_name)
"""
