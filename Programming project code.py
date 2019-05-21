from random import *
from time import *
import sys

roll_symbol_1 = (''' -----
|     |
|  0  |
|     |
 -----''')

roll_symbol_2 = (''' -----
|0    |
|     |
|    0|
 -----
''')

roll_symbol_3 = (''' -----
|0    |
|  0  |
|    0|
 -----
''')

roll_symbol_4 =(''' -----
|0   0|
|     |
|0   0|
 -----
''')

roll_symbol_5 =(''' -----
|0   0|
|  0  |
|0   0|
 -----
 ''')

roll_symbol_6 =(''' -----
|0   0|
|0   0|
|0   0|
 -----
''') 

users = [['Nye123', '1234'], ['Jared456', '6789'], ['Felix789', '4321']]


score_player_one = 0

score_player_two = 0

def roll_result():
   roll = randint(1, 6)
   return (roll)


def positive_roll(player_num):
   #https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment for the use of 'global'
   global score_player_one, score_player_two
   if player_num == 1:
      score_player_one += 10
      return print("Well done player one! You got 10 points!")
   elif player_num == 2:
      score_player_two += 10
      return print("Well done player two! You got 10 points!")

def negative_roll(player_num):
   global score_player_one, score_player_two
   if player_num == 1 and score_player_one != 0:
      score_player_one += 10
      return print("Too bad player one! You lost 5 points!")
   elif player_num == 1 and score_player_one == 0:
      score_player_one == 0
      return print("Too bad player one! At lest your score can't go below zero!")
   elif player_num == 2 and score_player_two != 0:
      score_player_two += 10
      return print("Too bad player two! You lost 5 points!")
   elif player_num == 2 and score_player_two == 0:
      score_player_two == 0
      return print("Too bad player two! At lest your score can't go below zero!")

def double_roll(player_num):
   global score_player_one, score_player_two
   if player_num == 1:
      print("Player One, You rolled a double!")
      print("You get to roll an extra dice and add the score to your total!")
      input("Press Enter to roll the dice!")
      single_roll = roll_result()
      print(roll_result_symbol(single_roll))
      score_player_one += single_roll
      print("Player One, you got " + str(single_roll) + " points!")
   elif player_num == 2:
      print("Player Two, You rolled a double!")
      print("You get to roll an extra dice and add the score to your total!")
      input("Press Enter to roll the dice!")
      single_roll = roll_result()
      print(roll_result_symbol(single_roll))
      score_player_two += single_roll
      print("Player Two, you got " + str(single_roll) + " points!")
   
   

   
#The symbols that will be called on for the game to represent the dice  
def roll_result_symbol(roll):
   if roll == 1:
      symbol = roll_symbol_1
   elif roll == 2:
      symbol = roll_symbol_2
   elif roll == 3:
      symbol = roll_symbol_3
   elif roll == 4:
      symbol = roll_symbol_4
   elif roll == 5:
      symbol = roll_symbol_5
   elif roll == 6:
      symbol = roll_symbol_6
   return symbol

def SUDDEN_DEATH():
   global score_player_one, score_player_two
   while score_player_one == score_player_two:
    print("Let's try that again!")
    input("Player One: Press enter to roll the dice!")
    last_roll_p1 = roll_result_final()
    print(roll_result_symbol(last_roll_p1))
    print("Your number is " + str(last_roll_p1))
    input("Player Two: Press enter to roll the dice!")
    last_roll_p2 = roll_result_final()
    print(roll_result_symbol(last_roll_p2))
    print("Your number is " + str(last_roll_p2))
    if last_roll_p1 > last_roll_p2:
       score_player_one += 1
    elif last_roll_p1 < last_roll_p2:
       score_player_two += 1
   if score_player_one > score_player_two:
      sleep(1.5)
      print("Player One wins with " + score_player_one + " points!")
      player1_scorename = input("Player One, input your name to be stored with your score:")
      f = open("PP_Scores_display.txt", "a")
      f.write(" " + player1_scorename + ", " + str(score_player_one) + " |")
      f.close()
      print("See ya next game!")
      sleep(2)
      menu()
   elif score_player_one < score_player_two:
      sleep(1.5)
      print("Player Two wins with " + score_player_two + " points!")
      player2_scorename = input("Player Two, input your name to be stored with your score:")
      f = open("PP_Scores_display.txt", "a")
      f.write(" " + player2_scorename + ", " + str(score_player_two) + " |")
      f.close()
      print("See ya next game!")
      sleep(2)
      menu()




def final_round():
   print ("Final Round!")
   input("Player One: Press enter to roll the dice!")
   roll_result_1 = roll_result()
   roll_result_2 = roll_result()
   print(roll_result_symbol(roll_result_1))
   print(roll_result_symbol(roll_result_2))
   total_roll = roll_result_1 + roll_result_2
   print("Total is", total_roll)
   if ((roll_result_1 + roll_result_2) % 2) == 0  and roll_result_1 != roll_result_2:
      positive_roll(1)
   elif roll_result_1 == roll_result_2 :
      positive_roll(1)
      double_roll(1)
   else:
      negative_roll(1)
   input("Player Two: Press enter to roll the dice!")
   roll_result_1 = roll_result()
   roll_result_2 = roll_result()
   print(roll_result_symbol(roll_result_1))
   print(roll_result_symbol(roll_result_2))
   total_roll = roll_result_1 + roll_result_2
   print("Total is", total_roll)
   if ((roll_result_1 + roll_result_2) % 2) == 0  and roll_result_1 != roll_result_2:
      positive_roll(2)
   elif roll_result_1 == roll_result_2:
      positive_roll(2)
      double_roll(2)
   else:
      negative_roll(2)
   #The finale... i guess
   sleep(1.5)
   if score_player_one > score_player_two:
      print("The final scores are in!")
      sleep(1)
      print("The winner is...")
      sleep(3)
      print("Player One with " + str(score_player_one) + " points!")
      player1_scorename = input("Player One, input your name to be stored with your score:")
      f = open("PP_Scores_display.txt", "a")
      f.write(" " + player1_scorename + ", " + str(score_player_one) + " |")
      f.close()
      print("See ya next game!")
      sleep(2)
      menu()
   elif score_player_two > score_player_one:
      print("The final scores are in!")
      sleep(1)
      print("The winner is...")
      sleep(3)
      print("Player Two with " + str(score_player_two) + " points!")
      player2_scorename = input("Player Two, input your name to be stored with your score:")
      f = open("PP_Scores_display.txt", "a")
      f.write(" " + player2_scorename + ", " + str(score_player_two) + " |")
      f.close()
      print("See ya next game!")
      sleep(2)
      menu()
   elif score_player_one == score_player_two:
       print("The final scores are in!")
       sleep(1)
       print("The winner is...")
       sleep(3)
       print("No one?!")
       sleep(0.5)
       print("It's a tie!")
       print("Time for...")
       sleep(3)
       print("SUDDEN DEATH")
       SUDDEN_DEATH()



#The main game.
def round(round_num):
   #The initial round of the whole game, the code is repeated until round 5
   if round_num == 1 or round_num == 2 or round_num == 3 or round_num == 4:
      print ("Round " + str(round_num) + "!")
      input("Player One: Press enter to roll the dice!")
      roll_result_1 = roll_result()
      roll_result_2 = roll_result()
      print(roll_result_symbol(roll_result_1))
      print(roll_result_symbol(roll_result_2))
      total_roll = roll_result_1 + roll_result_2
      print("Total is", total_roll)
      if ((roll_result_1 + roll_result_2) % 2) == 0 and roll_result_1 != roll_result_2:
         positive_roll(1)
      elif roll_result_1 == roll_result_2:
         positive_roll(1)
         double_roll(1)
      else:
         negative_roll(1)
      print("Player One: Your score is", score_player_one)
      input("Player Two: Press enter to roll the dice!")
      roll_result_1 = roll_result()
      roll_result_2 = roll_result()
      print(roll_result_symbol(roll_result_1))
      print(roll_result_symbol(roll_result_2))
      total_roll = roll_result_1 + roll_result_2
      print("Total is", total_roll)
      if ((roll_result_1 + roll_result_2) % 2) == 0 and roll_result_1 != roll_result_2:
         positive_roll(2)
      elif roll_result_1 == roll_result_2:
         positive_roll(2)
         double_roll(2)
      else:
         negative_roll(2)
      print("Player Two: Your score is", score_player_two)
   elif round_num == 5:
      final_round()

#player1_access_attempt_u = input("Player One: Enter a username:")
#player1_access_attempt_p = input("Player One: Enter a password:")
#player1_access_attempt = [player1_access_attempt_u, player1_access_attempt_p]
#print(player1_access_attempt)

#player2_access_attempt_u = input("Player Two: Enter a username:")
#player2_access_attempt_p = input("Player Two: Enter a password:")
#player2_access_attempt = [player2_access_attempt_u, player2_access_attempt_p]
#print(player2_access_attempt)

#The authentication system
def authentication(player_num):
   incorrect = 0
   if player_num == 1:
      for user in users:
         if player1_access_attempt == user:
            print("Access granted, Player One")
            sleep(1.5)
            break
         elif player1_access_attempt != user:
            incorrect += 1
      if incorrect == 3:
         print("Access denied, Player One.")
         quit()
   elif player_num == 2:
      for user in users:
         if player2_access_attempt == user:
            print("Access granted, Player Two")
            sleep(1.5)
            break
         elif player2_access_attempt != user:
            incorrect += 1
      if incorrect == 3:
         print("Access denied, Player Two.")
         quit()
#The menu of the game      
def menu():
   minput = input('''
Are you ready to roll?
Input G or Go if you want to play the game now,
Input R or Rules if you want to see how Dice Roll works,
Input S or Scores if you want to see the highest scores in Dice Roll or
Input Q or Quit if you want to quit the game: ''')
   #The rules of the game
   if minput ==  "R" and "Rules":
       print ('''___________________________________________________________________________________
             Dice Roll is a game where you and a friend roll two dice to get higher scores over five rounds.
        - The players will roll 2 dice and get a score from the dice:
            If the sum of the dice is even, the player gets 10 extra points!
            If the sum of the dice is odd, the players gets -5 points :( !
                (Don't worry, your score can't go below zero!)
            - After five rounds the players scores wil be revealed and the winner will be chosen!''')
       sleep(6)
       menu()
   elif minput == "G" and "Go":
         round(1)
         round(2)
         round(3)
         round(4)
         round(5)
     
# For file handling: https://sites.google.com/a/inspirationtrust.org/computer-science/home/programming-techniques/file-handling-1
   elif minput == "S" and "Scores":
       print("The highest scores are...")
       f = open("PP_scores.txt", "r")
       scores = f.readlines()
       f.close()
       print(scores)
       sleep(6)
       menu()

   elif minput == "Q" and "Q":
      muit = input("Don't go yet! Are you sure you want to quit? Respond with Y or N: ")
      if muit == "Y":
         print("Bye then!")
         sleep(2)
      elif muit == "N":
         print("Yay!")
         sleep(1)
         menu()
      else:
         print("I\'ll take that as a no then.")
         sleep(2)
         menu()
      
       
         
   else:
       print("Can you try that again?")
       sleep(2)
       menu()

#Where the game starts playing
#authentication(1)
#authentication(2)
print("Welcome to Dice Roll!")
menu()
