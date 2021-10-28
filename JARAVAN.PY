import pyautogui
import random as ran
import time
import os 
time.sleep(3)

word = ""


def Clear_Console():
	return os.system('cls')

def open_browser(i,Browser_name):
	while( i > 0):
	  pyautogui.press("win")
	  word = Browser_name
	  pyautogui.write(word)
	  pyautogui.press("enter")
	  i-= 1


def Web_Serch(word):


	open_browser(1,"edge")
	time.sleep(0.5)
	pyautogui.typewrite(word)
	pyautogui.press("enter")
	pyautogui.press("f11")
	pyautogui.leftClick()
	pyautogui.leftClick()
	time.sleep(3)


def volMax(i):
	while(i > 0):
		#pyautogui.press("volumeUp")
		pyautedgei.press("space")
		i-=1  


def browser_Depace(i):
	for i in range(i):
		pyautogui.press("tab")


def Play_Music(Music_Name):
	pyautogui.press("win")
	pyautogui.write("Youtube.com")
	pyautogui.press("enter")
	time.sleep(3)
	browser_Depace(4)
	pyautogui.typewrite(Music_Name)
	time.sleep(1)
	pyautogui.press("enter")
	time.sleep(2)

	#browser_Depace(1)	
	#pyautogui.press("enter")


def sent_fb_message(ToWho,Message):
	time.sleep(1)
	pyautogui.press("win")
	pyautogui.write("Facebook.com")
	pyautogui.press("enter")
	time.sleep(4)
	pyautogui.press("/")
	time.sleep(1)
	browser_Depace(8)
	pyautogui.press("enter")
	browser_Depace(5)
	pyautogui.typewrite(ToWho)
	time.sleep(2)
	pyautogui.press("down")
	pyautogui.press("enter")
	time.sleep(2)
	pyautogui.typewrite(Message)
	time.sleep(1)
	pyautogui.press("enter")


def sent_gmail(ToWho,Message):
	pyautogui.press("win")
	time.sleep(1)
	pyautogui.write("gmail.com")
	pyautogui.press("enter")
	time.sleep(4)
	browser_Depace(12)
	pyautogui.press("enter")
	time.sleep(1)
	pyautogui.typewrite(ToWho)
	time.sleep(1)
	pyautogui.press("enter")
	time.sleep(2)
	browser_Depace(2)
	pyautogui.write(Message)
	time.sleep(3)
	pyautogui.hotkey("ctrl","enter")




order = input("YOUR ORDER SIR: ")


orders = ["sent message","Sent Message","sent gmail","Sent Gmail", "play song","Play","playsong","play","Search","search","start","Start","Clean", "clean"]

while(True):


	if (order == "Clean" or order == "clean"):
		Clear_Console()
		order = ""
		order = input("Your Order Sir: ")


	if(order =="sent message" or order == "Sent Message"):
		towho = input("To who Should I Sent a Message: ")
		message = input("What Should I Say: ")
		sent_fb_message(towho,message)
		order = ""
		order = input("Anything Else?: ")

	if(order =="sent gmail" or order == "Sent Gmail"):
		towho = input("To who Should I Sent a Gmail: ")
		message = input("What Should I Say: ")
		sent_gmail(towho,message)
		order = ""
		order = input("Anything Else?: ")

	if(order == "play song" or order == "Play" or order == "playsong" or order == "play"):
	    songname = input("What Song Or Artist You Want To Listen?:")
	    Play_Music(songname)
	    order = ""
	    order = input("Anything Else?: ")


	if(order == "Search" or order == "search"):
	    search_subject = input("What You Want To Search?: ")
	    Web_Serch(search_subject)
	    order = ""
	    order = input("Anything Else?: ")

	if(order == "start" or order == "Start"):
		search_program = input("What You Want To Start?: ")
		pyautogui.press("win")
		pyautogui.write(search_program)
		pyautogui.press("enter")
		order = input("Anything Else?: ")

	for i in range(len(orders)):
		if(orders[i] == order):
			break

		else:
			i +=1

		if(i == len(orders)):
			order = input("Try Something Else: ")


        #pyautogui.write(search_program)

## Check if inputed order exsists

       


	
    


