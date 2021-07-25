#>Create hangman game where a words chosen from a pre defined list or input from
#   the user, counting the number of letters and setting up the game as if from list.

#>>Ask user if they have a word or want random one chosen
#>>> If input is 'random' then choose from pre list, else take input as chosen word
#>>> Read through word and add each letter into word_letter_list
#
#>>> Create display_list but with the words letters converted to '_' to represent unknown word
#>>> Initialise number of guesses counter to 3 

#>>While new word list of letters != Chosen word letter list OR number of guesses < 1
#>>> Initialise empty user_list
#>>> Ask user for letter input
#>>> Read through word_letter_list to check the guess matches any letter in list
#>>>> If guess matches any letter within word_letter_list:
#       >remove that letter(s) from list
#       >change the correct index in display_list to letter
#       >and print out the display list   
#
#    else:
#       >decrement the guess counter
#       >print message corresponding to number of guesses remaining
#       >and print the display list
#

#>>If number of guesses remaining == 0:
#     print "sorry mate you got the poor sod killed. Get better at literacy skills to stop killing people"
#
#   else:
#     print "You managed to save him, congratulations! I didn't expect you'd do it, honestly."

def split(word):
    return list(word)

def head():
    circle(35)
    #centre the arrow
    penup()
    right(90)
    pendown()

def body():
    forward(100)

def right_leg():
    right(45)
    forward(75)
    penup()
    left(180)
    forward(75)
    right(90)

def left_leg():
    pendown()
    forward(75)

def right_arm():
    #move to arms
    penup()
    right(180)
    forward(75)
    right(45)
    forward(100)
    right(180)
    pendown()
    #do arms
    right(45)
    forward(75)
    penup()
    left(180)
    forward(75)
    right(90)

def left_arm():
    pendown()
    forward(75)
    #move to top of head
    penup()
    left(180)
    forward(75)
    right(45)
    forward(70)

def hanging_frame():
    #draw rope and frame
    pendown()
    forward(100)
    right(90)
    forward(40)
    left(30)
    forward(50)
    left(150)
    forward(250)
    left(90)
    forward(400)
    #draw frame base
    right(45)
    forward(50)
    left(135)
    forward(103)
    left(135)
    forward(50)
    right(45)
    forward(375)
    right(90)
    forward(138)




import random
import collections
random_list = ['trebuchet', 'plant', 'twix', 'animal', 'human', 'cheetah', 'lion', 'separate',
               'umbrella', 'fairy', 'angola', 'november', 'kilogram', 'furlong', 'polygraph'
               'crutches', 'octopus', 'evil', 'vulture', 'xylophone', 'liver', 'zebra', 'graphite',
               'hippopotumus', 'cereal', 'quill', 'voldemort', 'harrypotter', 'sam', 'the', 'he',
               'she','it', 'to', 'a', 'fish', 'duck', 'grass', 'tron', 'introspective', 'wrong']
game_word = ""
user_input = input("What word do you want in play? or type 'random' if you want to be surprised: ")
user_input = user_input.lower()
if user_input == "random":
    game_word = random.choice(random_list)
else:
    game_word = user_input

word_letter_list = split(game_word)
display_list = []
for i in range(len(word_letter_list)):
    display_list.append('_')

from turtle import *
guess_counter = 7
fail_responses = ["sorry mate you got the poor sod killed. Get better at literacy skills to stop killing people.",
                  "He is practically dead, probably a vegetable even if you did save him.",
                  "It's not looking good, he's very purple right now.",
                  "Hmm, alright the rope looks a bit tighter but you still have plenty of opportunity left!",
                  "It's fine, he's fine, no one will die today I am sure of it!",
                  "Not that one, that one is wrong!",
                  "Come on now, another attempt please. Let's get this poor fellow down!"]
while display_list != word_letter_list and guess_counter > 0:
    print(display_list)
    user_guess = input("What letter do you guess? ")
    user_guess = user_guess.lower()
    if user_guess in word_letter_list:
        list_indicies = [i for i, x in enumerate(word_letter_list) if x == user_guess]
        for i in list_indicies:
            display_list[i] = user_guess
    else:
        guess_counter -= 1
        print(fail_responses[guess_counter])
        if guess_counter == 6:
            head()
        if guess_counter == 5:
            body()
        if guess_counter == 4:
            right_leg()
        if guess_counter == 3:
            left_leg()
        if guess_counter == 2:
            right_arm()
        if guess_counter == 1:
            left_arm()
        if guess_counter == 0:
            hanging_frame()

if guess_counter != 0:
    print("You managed to save him, congratulations! I didn't expect you'd do it, honestly.")
    print("You got the correct answer: " + game_word)
else:
    print("Your answer is wrong, the right answer is " + game_word)

