# Jankenpon

import emoji
import random
from time import sleep
print ("Hey! let's play Rock, Paper, Scissors?")
p = int(input(emoji.emojize("1 - :oncoming_fist:"
                            "\n2 - :hand_with_fingers_splayed:"
                            "\n3 - :victory_hand:\n")))
print ("\033[36m-=" * 5)1
print ("Jankenpon!")
print (5 * "-=")
sleep(1)
one = emoji.emojize(":oncoming_fist:")
two = emoji.emojize(":hand_with_fingers_splayed:")
three = emoji.emojize(":victory_hand:")
list = [one, two, three]
random = random.choice(list)
if p == 1:
    print(emoji.emojize(":oncoming_fist:"),"\033[31mX",random)
    if random == one:
        print("\033[36mRematch!")
    if random == two:
        print("\033[31mToo bad, you lost!")
    if random == three:
        print("\033[32mGood job, you won!")

if p == 2:
    print(emoji.emojize(":hand_with_fingers_splayed:"),"\033[31mX",random)
    if random == one:
        print("\033[32mGood job, you won!")
    if random == two:
        print("\033[36mRematch!")
    if random == three:
        print("\033[31mToo bad, you lost!")

if p == 3:
    print(emoji.emojize(":victory_hand:"),"\033[31mX  ",random)
    if random == one:
        print("\033[31mToo bad, you lost!")
    if random == two:
        print("\033[32mGood job, you won!")
    if random == three:
        print("\033[36mRematch!")
if p > 3:
    print("\033[31mAre you cheating?")