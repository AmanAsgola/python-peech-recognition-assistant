import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()
def wishme():
	hour=int(datetime.datetime.now().hour)
	if hour>0 and hour<12:
		speak("Good Morning Aman !")
	elif hour>12 and hour<18:
		speak("Good Afternoon!")
	else:
		speak("Good Evening Aman !")
def command():
	r=sr.Recognizer()

	with sr.Microphone() as source:
		print("Listening....")
		r.pause_threshold = 1
		audio=r.listen(source)
		try:
			print("Recognizing.....")
			query=r.recognize_google(audio, language="en-in")
			print(f"user said:{query}")
		except Exception as e:
			speak("sorry not able to recognize")
			return "None"
		return query

if __name__=="__main__":
	wishme()	
	while True:
		query=command().lower()
		if 'wikipedia' in query:
			speak("wikipedia searching")
			query=query.replace("wikipedia", " ")
			results=wikipedia.summary(query, sentences=2)
			print(results)
			speak(results)
		elif 'thank you' in query:
			break
		elif f'open {query[5:]}' in query:
			webbrowser.open(f"www.{query[5:]}.com")
		elif 'current time' in query:
			time=datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"its {time}")

