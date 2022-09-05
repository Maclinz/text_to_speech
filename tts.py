from gtts import gTTS
from tkinter import *
import os

fileText = ''
fileText2 = ''

with open('file1.txt', 'r') as file1:
    fileText = file1.read()

with open('file2.txt', 'r') as file2:
    fileText2 = file2.read()


class TextToSpeech:
    def __init__(self, text, lang, filename):
        self.text = text
        self.lang = lang
        self.filename = filename
    
    def speak(self):
        text = gTTS(self.text, lang=self.lang, slow=False)
        text.save(f"{self.filename}.mp3")
        os.system(f"start {self.filename}.mp3")


person1 = TextToSpeech(fileText, "en", "John")
person2 = TextToSpeech(fileText2, "en", "Mike")

window = Tk()
window.title("Text To Speech")

canvas = Canvas(window, width=300, height=300)
canvas.pack()

button = Button(window, text=person1.filename, command=person1.speak, padx=20, pady=7)
button_win = canvas.create_window(150, 150, window=button)

button2 = Button(window, text=person2.filename, command=person2.speak, padx=20, pady=7)
button_win2 = canvas.create_window(150, 200, window=button2)

window.mainloop()