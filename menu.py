import pyttsx3
import datetime
import os
x=0
print("Please enter your name: ", end='')
name = input()
t=datetime.datetime.now()
hour = int(t.strftime("%H"))
if (hour<12):
	g = "Good Morning"
elif(hour<16):
	g = "Good Afternoon"
else:
	g = "Good Evening"
pyttsx3.speak(g+name+" Welcome to the OS program") 

while True:


	if x==3:
		print("\nThis program supports only Google Chrome, Notepad, MSexcel, MSword, MSpower point, Outlook, vlc media player, command prompt, sticky note, calculator, paint")
		x=0

	print("\nType quit or exit to terminate the program\n")
	print("Please enter your requirements: ", end='')
	i=input()
	p=i.lower()

	if ("dont" not in p) and ("don't" not in p) and ("do not" not in p) and ("not " not in p) :


		if "run" in p  or "launch" in p  or "open" in p  or "execute" in p  or "initiate" in p  or "start" in p  or "activate" in p or 				"begin" in p or "create" in p:			


			if "chrome" in p  or "google" in p  or "browser" in p  :
				print("let me know if you want to open any site")
				print("Enter if you want to open any particular site or type no: ",end='')
				site=input()
				if "no" == site:
					pyttsx3.speak("Opening Chrome for you")
					os.system("chrome")
				else:
					pyttsx3.speak(f"Opening {site} for you")
					os.system(f'chrome "{site}.com"')

			elif "notepad" in p  or "text" in p  or "editor" in p  :
				pyttsx3.speak("Opening notepad for you")
				os.system("notepad")

			elif "excel" in p  or "sheet" in p  :
				pyttsx3.speak("Opening excel for you")
				os.system("excel")

			elif "word" in p  or "document" in p  :
				pyttsx3.speak("Opening MSword for you")
				os.system("winword")

			elif "outlook" in p or "mail" in p:
				pyttsx3.speak("Opening Outlook for you")
				os.system("outlook")

			elif "cmd" in p or "shell" in p or "prompt" in p or "command" in p:
				pyttsx3.speak("Opening command prompt for you")
				os.system("start cmd")

			elif "sticky" in p or " note" in p:
				pyttsx3.speak("Opening Sticky notes for you")
				os.system("stikynot")

			elif "calculator" in p or "calc" in p:
				pyttsx3.speak("Opening Calculator for you")
				os.system("calc")

			elif "draw" in p or " paint" in p :
				pyttsx3.speak("opening paint for you")
				os.system("mspaint")

			elif " ppt" in p  or "power" in p  or "presentation" in p :
				pyttsx3.speak("Opening Power point for you")
				os.system("ppt")

			elif "video" in p  or "movie" in p  or "media player" in p  or "vlc" in p :
				pyttsx3.speak("Opening vlc media player for you")
				os.system("vlc")

			else:
				print("\nSorry, Such program is not present in your system. Please try Again.")
				pyttsx3.speak("Please try again")
				x=x+1
		elif "exit" in p or "quit" in p or "close" in p :
			print("exiting...")
			pyttsx3.speak("It was nice chatting with you, Have a nice day. Bye...")
			break;
		else:
			print("\nThe requirement is not supported")		
