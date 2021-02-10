#! C:\Users\kemfj\AppData\Local\Programs\Python\Python38-32\python.exe

import os
import sys
sys.path.append('C:\\Bitnami\\wampstack-7.4.14-0\\apache2\\htdocs\\texttospeech\\tts\\Lib\\site-packages')

credential_path = 'C:\\Bitnami\\wampstack-7.4.14-0\\apache2\\htdocs\\project-tts-303101-2f266bc85a53.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

import cgi
form = cgi.FieldStorage()
tts_text = form["tts_text"].value
file_text = form["file_text"].value

import pyglet

import pygame

"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=tts_text)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="ko-KR", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open(file_text, "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
#    print('Audio content written to file "output.mp3"')

# audio play
#song = pyglet.media.load(file_text)
#song.play()
#pyglet.app.run()

# audio play2
music_file = file_text   # mp3 or mid file


freq = 16000    # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
bitsize = -16   # signed 16 bit. support 8,-8,16,-16
channels = 1    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)

# default : pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.init(freq, bitsize, channels, buffer)
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    clock.tick(30)
pygame.mixer.quit()  

#Redirection
print("Location: index2.py")
print()

