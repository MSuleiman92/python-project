# Python Text to Speech (Code)

# Install a library that can take any text and convert it to speech 
# pip3 install pyttsx3 (Python text to speech ver 3)

from docx import Document  #from library docx we need
from docx.shared import Inches 
import pyttsx3

#pyttsx3.speak('Hello Rakiya I love you')

def speak(text):
    pyttsx3.speak(text)

name = input('What is your name ? ')
speak('Hello'+ name + 'how are you today?')
speak('What is your phone number?')