"""PINK FLUFFY UNICORNS RULE THE WORLD!!!!"""

import colors as c
from utils import ask

intro = c.magenta + "Welcome to the Pink Fluffy Unicorns quiz!!! " + c.reset

def q1():
    answer = ask(c.blue + "What color are the Pink Fluffy Unicorns?")
    if answer == "pink":
        print("pink, pink, pink, pink, pink, pinky, pink...")
        return True
    return False;

def q2():
    answer = ask(c.red + "Where were the Pink Fluffy Unicorns?")
    if answer == "Rainbows":
        print("Its raining, its poring, the rainbows are falling down and breaking their ankles")
        return True
    return False;

def q3():
    answer + ask(c.green + "What texture were the Pink Fluffy Unicorns?")
    if answer == "Smiles":
        print("Do you smile? I smile. You should smile! Smile everyday!")
        return True 
    return False;

questions = [q1,q2,q3]
