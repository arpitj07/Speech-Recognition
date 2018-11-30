import speech_recognition as sr 
import pyaudio

r = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())

mic = sr.Microphone(device_index=1)

with mic as source:
	r.adjust_for_ambient_noise(source , duration=0.5)
	audio= r.listen(source)

print(r.recognize_google(audio))


