#adds pdf library
import pymupdf 

#stores pdf in variable and loads it into memory
pdf_holder = 'Outline.pdf' # <----place holder file for testing
pdf = pymupdf.open(pdf_holder)


all_text = " "

#loops through each page of pdf and stores it into "all_text"
for page in pdf:
    text = page.get_text()
    all_text += text + "\n"

#puts all the words into a txt file
    with open('extracted_text.txt', 'w',encoding='utf-8') as f:
        f.write(all_text)

print("Complete")
print(all_text)




#PUT THE KEY IN THE FILE













