##Family Dinner Rotation calculator

""" This program creates a fortnightly dinner roation list from a total list
    of recipes that is appropraite for whole family to eat, avoiding any
    repeats """

from random import *

#Set up the lists and initialise variables#
recipes = [
    "BOLOGNESE",
    "BURGERS",
    "BURRITOS", 
    "BEEF CASSEROLE", 
    "SAUSAGE CASSEROLE", 
    "CHICKEN & LEEK BAKE", 
    "CHICKEN CURRY", 
    "CHILLI", 
    "CHILLI IN STUFFED PEPPERS", 
    "EGG NIGHT", 
    "ENCHILADAS", 
    "FISH & VEG", 
    "GAMMON", 
    "HAM PUTTENESCA", 
    "HOTDOGS", 
    "HUNTERS CHICKEN", 
    "JAMBALAYA", 
    "LASAGNE", 
    "MEATBALL MARIANA", 
    "PASTA BAKE", 
    "PIES", 
    "PIZZA", 
    "QUESIDILLAS", 
    "SALAD - CHICKEN", 
    "SALAD - HOULOMI", 
    "SAUSAGE & MASH", 
    "SAUSAGES", 
    "SHEPHERDS PIE", 
    "STIR FRY",
    "SWEET & SOUR CHICKEN",
    "TUNA NAPOLITINA" 
]
rotation = []
used_numbers = []
random_number = 0
counter = 0

#Begin loop to fill list
while counter < 14:
    random_number = randint(1,len(recipes))
    while random_number in used_numbers:
        random_number = randint(1, len(recipes))
    used_numbers.append(random_number)
    rotation.append(recipes[random_number - 1])
    counter = counter + 1
print(rotation)
    
