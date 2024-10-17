"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down


import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 

print("Players, Please Stand Up!")

im = Image.open("times-up.jpeg")

# ask user to enter desired countdown time
set_time = int(input("Please set your timer in seconds: "))

while not (10<=set_time<=25):
	set_time=int(input("Please choose a number between 10 to 25 seconds: ")

time.sleep(set_time)

#Create a list to track the name of users who sat down

players_sat = []

#Initiate New Variables
current_time = time.time()
limit=current_time + set_time

while current_time <= limit:
	players=input("Enter the name of players who sat down: ")
	if players:
		player_sat.append(players)
	else:
		print("Nobody sat down!")
print ("Time 's up!")
im.show()

if player_sat:
	winner = player_sat[-1]
	print(f"The winner's {winner}~Yeah!")
else:
	print("No one wins :-(")
