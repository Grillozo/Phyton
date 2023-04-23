#Guess the number 2 (While)

from random import randint
c = randint(0,5)#Computer choose number
n1 = 6
att = 1
print("-=-" * 15)
print("Im thinking of a number between 0 and 5")  # interface
print("-=-" * 15)
while n1 != c:
    n1 = int(input('Try to guess the number: '))#player input
    if n1 != c:
        att += 1
if att == 1:
    print("Good job! You got it on your first guess!")
elif n1 == c:
    print("It took you {} guesses.".format(att))


#                           OR

'''import random
n1 = int(input('Guess the number that Im thinking of, choose between 0 and 5: '))
lista = [0,1,2,3,4,5]
rnumb = (random.choice(lista))
if n1>5:
    print('The number you chose is not between 0 and 5!')
if n1 == rnumb:
    print("Congratulations you got it right, you're a true wizard!")
else:
    print("Sorry, try again!")'''