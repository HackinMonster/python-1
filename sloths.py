

import colors as c
from utils import ask

intro = c.magenta + "Welcome to the sloth quiz"

def q1():
    answer = ask(c.blue + "What are sloths most popular for" + c.reset)
    if answer == "swag":
        print("Yes, Sloths are known for their swag!" + c.reset)
        return True
    else:
        print("No sloths are better than than that!" + c.reset)
    return False; 
        
def q2():
    answer = ask(c.red + "Are sloths swaggy?" + c.reset)
    if answer == "Yes":
        print("SWAGGY SWAGGY SWAGGY" + c.reset)
        return True
    else:
        print("Narwhals are swaggy. You are wrong" + c.reset)
    return;
def q3():
    answer = ask(c.green + "Should sloths have access nuclear warheads?" + c.reset)
    if answer == "Yes":
        print("yeah sloths should... but they cant.." + c.reset)
        return True
    else:
        print("YES THEY SHOULD!!!!!!!!!!!!!!!" + c.reset)
    return False;
def q4():
    answer = ask(c.magenta + "What is the lifespan of the average sloth" + c.reset)
    if answer == "20 years":
        print("YEP." + c.red + c.reset)
        return True
    else:
        print("NOPE." + c.blue + c.reset)
        return False;
def q5():
    answer = ask(c.violet + "Are you a sloth?" + c.reset)
    if answer == "yes":
        print("OMG YOURE A SLOTH TOO!!!" + c.green + c.reset)
        return True
    else:
        print("Well thats boring" + c.reset)
questions = [q1,q2,q3,q4,q5]
