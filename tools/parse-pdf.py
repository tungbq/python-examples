import PyPDF2
import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize


PDF_PATH="C:\\Users\\ASUS\\OneDrive\\BOOK\\AWS-SAA\\AWS Certified Solutions Architect Slides v13 Parse.pdf"


# Open the PDF file
pdf_file = open(PDF_PATH, 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Initialize the summary variable
summary = ''

# Loop through each page in the PDF file
for page_num in range(len(pdf_reader.pages)):
    # Extract the text from the page
    # page = pdf_reader.getPage(page_num)
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    
    # print(text)
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    print("Working on page_num: ", page_num)
    # print("sentence: ", sentences)
    # print("sentence len: ", len(sentences))

    # Check first sentence in the page
    first_sentence = sentences[0]
    # print("first_sentence: ", first_sentence)
    first_sentence = first_sentence.replace("© Stephane MaarekNOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com", "")
    # print("first_sentence Updated: ", first_sentence)
    first_sentence_title = first_sentence.split("•")[0]
    # print(">>> first_sentence_title: ", first_sentence_title)

    summary += first_sentence_title + '\n'

# Print the summary
print(summary)
print("Parsing completed! Writing output to the file")
OUT_PUT_FILE="../output/summary.txt"
# Open the file in write mode
with open(OUT_PUT_FILE, 'a', encoding="utf-8") as file:
    # Write the string to the file
    file.write(str(summary))
