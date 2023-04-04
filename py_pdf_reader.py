from PyPDF2 import PdfReader # pip install PyPDF2
import pyttsx3 # pip install pyttsx3

# Initializing files in python //
read = PdfReader("question_answers.pdf") # The python file and pdf file should be in same directory

# reading page number //
page = read.pages[6]

# making speaker ready to speak //
speaker = pyttsx3.init()

# Speaker is speaking with this line of code //
speaker.say(page.extract_text())

# End of speaking
speaker.runAndWait()