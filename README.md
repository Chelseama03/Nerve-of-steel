# Nerve of Steel
### Nerve of Steel is a party game!
This is a program written in Python  

![times-up!](https://media.makeameme.org/created/times-up-5923e0.jpg)\
timer.py is a simple Python script allowing users to set timer duration, track the names of users, and complete the game.
The game follows the steps below:
1. Initially all players sit in a circle and the program displays the words to let everybody stand up.
2. The program will sleep a time between 15-20 seconds. During this time, people can sit down.
3. The program tracks the players who sat down and creates a list to record their names.
4. When sleep is over, the last player to sit down wins the game.
   
*Upon timer expiry, the user will see the time-up meme.
timer.py uses the **time library** to help keep track of time and the **pillow library** to facilitate the meme display.

Please see the documentation for the library used:
- [time](https://docs.python.org/3/library/time.html)
- [pillow](https://pypi.org/project/Pillow/)
