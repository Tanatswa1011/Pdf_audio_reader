import pyttsx3
import PyPDF2

book = open("money.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()

audio_content = ""
for page in range(12, 178):  
    current_page = pdfReader.getPage(page)
    text = current_page.extractText()
    audio_content += text + " "  
speaker.save_to_file(audio_content, "moneyaudiobook.mp3")
speaker.runAndWait()






     

