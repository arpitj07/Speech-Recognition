import time 
import random
#import pyaudio
import speech_recognition as sr 



def SpeechRecognition(recognizer , microphone):


	if not isinstance(recognizer , sr.Recognizer):
		raise Typeerror(" `recognizer` must me `Recognizer` isinstance")

	if not isinstance(microphone , sr.Microphone):
		raise Typeerror(" `microphone must be Microphone instance")


	with microphone as source:
		recognizer.adjust_for_ambient_noise(source , duration=0.5)
		audio = recognizer.listen(source)


	response = {
				"success" : True,
				"error" : None,
				"transcription" : None
	}

	try:
		response["transcription"] = recognizer.recognize_google(audio)
	except sr.RequestError:
		response["success"] = False
		response["error"]	= "API unavailable"
	except sr.UnknownValueError :
		response["error"] = "Unable to recognize speech"

	return response




if __name__ == "__main__":

	words = ["apple" , "banana" , "grape" , "orange" , "mango" , "lemon"]
	Num_guesses = 3
	Prompt_Limit = 5

	#create the instances
	recognizer = sr.Recognizer()
	microphone = sr.Microphone()


	word = random.choice(words)

	#format the instructions string 
	instructions = ("I am thinking of one of these words: {words}\n"
					"you have {n} tries to guess which one.\n").format(words=",".join(words), n=Num_guesses)



	print(instructions)
	time.sleep(2)

	for i in range(Num_guesses):
		# get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
		for j in range(Prompt_Limit):

			print("Guess {}. Speak !".format(i+1))
			guess = SpeechRecognition(recognizer , microphone)

			if guess['transcription']:
				print("You said {}".format(guess["transcription"]))
				break
			if not guess['success']:
				print("I didnt catch that . what did you say? \n")
				break

		if guess["error"]:
				print("ERROR: {}".format(guess["error"]))
				break

		
		guess_is_correct = guess["transcription"].lower() == word.lower()
		more_attempts = i < Num_guesses -1

		if guess_is_correct:
			print("Correct ! You Win".format(word))
			break

		elif more_attempts:
			print("Incorrect. Try Again.\n")

		else:
			print("Sorry, You lose ! \n I was thinking of {}".format(word))
			break



