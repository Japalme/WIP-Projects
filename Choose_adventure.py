#Imports for pauses and typing functions

import time
import sys

# Start of game
def start():
    bedroom()


#Typing function
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


# Game openeing

def bedroom():
    delay_print ("\n You are abruptly woken up to the sound of blaring sirens")
    time.sleep(2)
    delay_print ("\n As you try and get yourself centered, you look at the clock")
    time.sleep(2)
    delay_print ("\n After blinking a few times, it reads 2 AM...")
    time.sleep(2)
    delay_print("\n You look around deciding what to do next. Do you\n 1. Turn on the TV \n 2. Look out the window\n 3. Grab your Phone")
    
    Q1 = input(" \n Choice: ")

    if Q1 == "1":
        TV()
    elif  Q1 == "2" :
        game_over()
    elif Q1==  "3":
        phone1()

# TV choices

def TV():
    delay_print (" You click on the TV, it's showing the national alert emergency channel")
    time.sleep(2)
    delay_print ("\n You flip through a few channels and realize its on every channel! What is going on?!")
    time.sleep(2)
    delay_print ("\n As you watch you start to realize what is happening, there has been an outbreak from a lab in your city and its quickly taking over...")
    time.sleep(2)
    delay_print ("\n You can hear explosions outside the window and people screaming. This is insane, how could this happen!!")
    time.sleep(2)
    delay_print ("\n Your start thinking what to do next, the next move could decide if you live or die")
    time.sleep(2)
    delay_print ("\nWhat do you do next? \n1. Grab your phone \n2. Grab your keys and head for the front door \n3. Look out the window\n")

    choice= input("\n Your Choice : ")

    if  choice == "3":
        game_over()
    elif  choice == "2":
        car2()
    elif  choice == "1":
        phone()

# phone choices

def phone():
    delay_print("You grab your phone and notice 10 missed notifications")
    time.sleep(2)
    delay_print("\n Most of these are emergency notifications alerting you to the situation, but you have two missed calls from your parents")
    time.sleep(2)
    delay_print("\n You try and call them back... no answer. This isnt good")
    time.sleep(2)
    delay_print("\n They left a voicemail explaining they are going to the cabin out of state, hoping its safer than the city and tell you to get there as soon as you can.")
    time.sleep(2)
    delay_print("\n You have two choices now. \n 1. Get to your car and drive to the cabin, knowing the roads are a mess you might not make it. \n 2. Decide to stay in place, barricade the doors and windows best you can and hope for the best.*Your parents will be fine... right?")
   
    choice= input("\n Your Choice : ")

    if choice == "1":
        car()
    elif  choice == "2":
        gameover_2()

def phone1():
    delay_print(" You grab your phone and notice 10 missed notifications")
    time.sleep(2)
    delay_print("\n Most of these are emergency notifications alerting you to the situation,\n There has been an outbreak in a lab near you and it is causing infected to lose their minds. \n You also notice you have have two missed calls from your parents")
    time.sleep(2)
    delay_print("\n You try and call them back... no answer. This isnt good")
    time.sleep(2)
    delay_print("\n They left a voicemail explaining they are going to the cabin out of state, hoping its safer than the city and tell you to get there as soon as you can.")
    time.sleep(2)
    delay_print("\n You have two choices now. \n 1. Get to your car and drive to the cabin, knowing the roads are a mess you might not make it. \n 2. Decide to stay in place, barricade the doors and windows best you can and hope for the best.*Your parents will be fine... right?")
    
    choice= input("\n Your Choice : ")

    if choice == "1":
        car()
    elif  choice =="2":
        gameover_2()

# car choice split

def car():
    delay_print("\n You grab your keys and head for the door, you hear voices outside of the door...")
    delay_print("\n Do you \n 1. Open the door? \n 2. Head to the window and look for an escape.")
    
    choice= input("\n Your Choice : ")

    if choice == "1":
        opendoor()
    elif  choice == "2":
        gameover_4()

def car2():
    delay_print("You open the door slowly and see if anyone is outside")
    time.sleep(2)
    delay_print("\nYou notice someone down the hall and sneak in the other direction towards the parking ramp")
    time.sleep(2)
    delay_print("\n They see you and start running after you! You run as fast as you can and make it down the stairs to your car, but they are right behind...")
    time.sleep(2)
    delay_print("\n You grab the keys from your pocket and quickly open the door, slamming it behind you. They are pounding on the window begging for help...")
    time.sleep(2)
    delay_print("\n You turn the car on and speed away, can't take any chances. You are able to make it to the edge of the citybut hit a checkpoint.")
    time.sleep(2)
    delay_print("\n There are two choices, \n 1. You see an opening you might be able to make it through and escape the city. \n 2. You sit through the checkpoint to hopfully get out.")
    time.sleep(2)
    choice = input()

    if  choice == "1":
        opening()
    elif  choice == "2":
        checkpoint()

# GAME OVER SCENARIOS

def game_over():
    delay_print("You notice the window is smashed in, unsure how it didnt wake you up you walk over to the window and look out.")
    time.sleep(2)
    delay_print("\nYou see the world in chaos, everything is on fire! What happened...")
    time.sleep(2)
    delay_print("\nYou hear a scream behind you, in the reflection of the remaining window you see a man with a raised machette")
    time.sleep(2)
    delay_print("\nYou try and spin around to defend yourself, its to late you and you brace for the impact...")
    time.sleep(2)
    delay_print("\nAll you feel is the warmth and the light fading away, the man just laughs...")
    time.sleep(4)
    delay_print("\nDo you want to play again? (y / n)\n")
    
    choice = input()
    
    if  choice == "y":
        start()
    elif  choice == "n":
        exit(0)
    else:
        retry()

def gameover_2():
    delay_print("You decide to barricade yourself in with a desk in front of the door and hope for the best")
    time.sleep(2)
    delay_print("\nYou notice the window is broke, how did that not wake you up?")
    time.sleep(2)
    delay_print("\n You go over and investigate the window, and notice someone out on the fire escape...")
    time.sleep(2)
    delay_print("\n Before you can react you see a shadow coming at you and knocking into your face")
    time.sleep(2)
    delay_print("\nAll you feel is the warmth and the light fading away...")
    time.sleep(4)
    delay_print("\nDo you want to play again? (y / n)\n")
   
    choice = input()
    
    if  choice =="y":
        start()
    elif  choice == "n":
        exit(0)
    else:
        retry()


def checkpoint():
    delay_print("You sit through the checkpoint for what must be an hour, wondering what is happening. Everyone seems to be losing their minds")
    time.sleep(2)
    delay_print("\n Once you finally make it to the checkpoint the guards ask who you are and where you are going, you explian who you are and that you are going to your parents cabin. ")
    time.sleep(2)
    delay_print("\n The guards do not believe your story and investigate further, you see in the distance people being rounded up for suspected insanity. You are getting frustrated and the guards see this change...")
    time.sleep(2)
    delay_print("\n The guards pull you from your car, you attempt to make an escape but are shot in the back as you run. ")
    time.sleep(2)
    delay_print("\nAll you feel is the warmth and the light fading away...")
    time.sleep(4)
    delay_print("\nDo you want to play again? (y / n)\n")
    choice = input()
    
    if choice == "y":
        start()
    elif  choice =="n":
        exit(0)
    else:
        retry()
        
def gameover_4():
    delay_print("You notice the window is smashed in, unsure how it didnt wake you up you walk over to the window and look out.")
    time.sleep(2)
    delay_print("\nYou see the world in chaos, how could this happen?")
    time.sleep(2)
    delay_print("\nYou hear footsets on the fire escape grate outside the window")
    time.sleep(2)
    delay_print("\nYou see a shadow coming at you fast and you raise your hands to defend yourself, its to late...")
    time.sleep(2)
    delay_print("\nAll you feel is the warmth and the light fading away...")
    time.sleep(4)
    delay_print("\nDo you want to play again? (y / n)\n")
    choice = input()
    
    if  choice =="y":
        start()
    elif  choice == "n":
        exit(0)
    else:
        retry()


def retry():
    print("Do you want to play again?")

    choice = input("\n (y/n):\n  ")
    if choice == "y":
        start()
    elif choice == "n":
        exit(0)
    else:
        retry()

#good endings

def opening():
    delay_print("You gun it for the opening in the checkpoint the guards at the checkpoint open fire!")
    time.sleep(2)
    delay_print("\n You are able to make it through without injury somehow and the car still runs")
    time.sleep(2)
    delay_print("\n You are able to make it to your parents cabin and take refuge in the woods. The insanity never makes it this far. ")
    time.sleep(4)
    delay_print("\nDo you want to play again? (y / n)\n")
    choice = input()
    
    if  choice == "y":
        start()
    elif  choice == "n":
        exit(0)
    else:
        retry()

def opendoor():
    delay_print("You open the door slowly and see if anyone is outside")
    time.sleep(2)
    delay_print("\nYou notice someone down the hall and sneak in the other direction towards the parking ramp")
    time.sleep(2)
    delay_print("\n They see you and start running after you! You run as fast as you can and make it down the stairs to your car, but they are right behind...")
    time.sleep(2)
    delay_print("\n You grab the keys from your pocket and quickly open the door, slamming it behind you. They are pounding on the window begging for help...")
    time.sleep(2)
    delay_print("\n You turn the car on and speed away, can't take any chances. You are able to escape the city and make it to your parents cabin, the insanity stays away from the woods and you are able to weather the storm.  ")
    time.sleep(4)
    delay_print("\nDo you want to play again? (y / n)\n")
    choice = input()
    
    if  choice == "y":
        start()
    elif choice == "n":
        exit(0)
    else:
        retry()



start()