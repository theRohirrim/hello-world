# Magic 8 Ball

#>Ask/allow user to enter their question
#>Display progress message
#>Call a function of 20 randomised responses
#>Allow user to ask another question/terminate

from time import sleep
import random

def random_response():
    ran = random.randint(0,20)
    if ran == int('1'):
        resp = "Outcome is unclear"
    if ran == int('2'):
        resp = "Ask your mother"
    if ran == int('3'):
        resp = "That's illegal"
    if ran == int('4'):
        resp = "Satan says 'sounds good to me'"
    if ran == int('5'):
        resp = "Of course not, you mouldy piece of cheese"
    if ran == int('6'):
        resp = "Yes.........idiot"
    if ran == int('7'):
        resp = "No shit"
    if ran == int('8'):
        resp = "I'm a magic 8 ball, not your friend"
    if ran == int('9'):
        resp = "Umm, yeah......now ask something not completely braindead"
    if ran == int('10'):
        resp = "Join a credit union"
    if ran == int('11'):
        resp = "I think you're dreaming a bit too big pal"
    if ran == int('12'):
        resp = "I'm afraid I cannot answer that"
    if ran == int('13'):
        resp = "You can act as if it is true but I couldn't tell you if it isn't"
    if ran == int('14'):
        resp = "Wait hold on I forgot to pick up my kids from the alleyway"
    if ran == int('15'):
        resp = "I slept with your wife"
    if ran == int('16'):
        resp = "Please shake again"
    if ran == int('17'):
        resp = "Why are you taking advice from me?"
    if ran == int('18'):
        resp = "How about you think that one through, champ"
    if ran == int('19'):
        resp = "Don't worry, they are just jealous of you"
    if ran == int('20'):
        resp = "'Do you feel lucky punk?' - Ghandi"
    return resp

def eightball(): 
    question = input("Ask a question and ye shall receieve an answer!")
    print('  "', question,'" you ask?')
    sleep(1)
    print('Give me a bit to consult with the Gods')
    sleep(3)
    answer = random_response()
    print('The gods say: "', answer,'"')
    sleep(1)
    end()

def end():
    print("That was fun! Want to try again? Type yes or no.")
    play = input()
    if play == "yes":
        eightball()

print("WELCOME TO THE ORACLE - Answerer of lifes mysteries...")
eightball()
        
