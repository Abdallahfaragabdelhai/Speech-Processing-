
import pyttsx3
import PyPDF2

book = open('THE MAGIC WINDOW.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
speaker = pyttsx3.init()
page = pdfReader.getPage(0)
text = page.extractText()
#speaker.setProperty("volume",100)
#rate = speaker.getProperty("rate")
#speaker.setProperty("rate",200)
#print(rate)

voices = speaker.getProperty("voices")
print("Male Voice : {0}".format(voices[0].id))
print("Female Voice : {0}".format(voices[1].id))
speaker.setProperty("voice",voices[1].id)

speaker.say(text)
speaker.runAndWait()

