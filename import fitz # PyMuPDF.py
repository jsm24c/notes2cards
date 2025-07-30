import fitz  # PyMuPDF
import openai


PDF_PATH = "Outline.pdf"  #place holder/ name of pdf being extracted
OUTPUT_TSV = "flashcards.tsv"
OPENAI_API_KEY = "Don't be Nosey"

#opens pdf
file = fitz.open(PDF_PATH)

#extracts all the text and joins it together
all_text = "\n".join(page.get_text() for page in file)

#prompts chat gpt th turn the text parsed from the pdf into question answer pairs
openai.api_key = OPENAI_API_KEY

prompt = f"""
From these lecture notes, generate flashcards in Q&A format.

\"\"\"{all_text}\"\"\"

Respond only with Q&A like:
Q: What is X?
A: X is...
"""
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You generate study flashcards from lecture notes."},
        {"role": "user", "content": prompt}
    ],
    #creative but still somewhat responsible
    temperature=0.6 
)

#stores the output
qa_text = response.choices[0].message.content.strip()
