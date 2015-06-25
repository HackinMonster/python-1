"""SLOTHS"""

import colors as c
from utils import ask

intro = c.magenta + "Welcome to the sloth quiz" + c.reset

def q1():
    answer = ask(c.blue + "What are sloths most popular for")
    if answer == "swag":
        print("Yes, Sloths are known for their swag!")
        return True
    else:
        print("No narwhals are better than than that!
    return False; 
        
def q2():
    answer = ask(c.red + "Are sloths swaggy?")
    if answer == "Yes":
        print("SWAGGY SWAGGY SWAGGY")
        return True
    else:
        print("Narwhals are swaggy. You are wrong")
    return;
def q3():
    answer + ask(c.green + "Should sloths have access nuclear warheads?")
    if answer == "Yes":
        print("Narwhals know how to use nukes")
        return True
    else:
        print("YES THeY SHOULD!!!!!!!!!!!!!!!")
    return False;

questions = [q1,q2,q3]
