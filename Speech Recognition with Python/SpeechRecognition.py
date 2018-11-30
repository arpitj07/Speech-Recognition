import speech_recognition as sr


r = sr.Recognizer()

harward = sr.AudioFile("harvard.wav")

#storing AudioFile instance as source
with harward as source:
	r.adjust_for_ambient_noise(source)
	audio = r.record(source)

print(type(audio))


print(r.recognize_google(audio , show_all=False))
