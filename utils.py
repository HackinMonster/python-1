"""This is a cool file"""

import colors as c

def ask(question):
    print(question)
    answer =  input('> ' + c.yellow).lower().strip
    print(c.reset)
    return answer

if __name__ == '__main__':
    print(c.clear)
    name = ask("What is your name?" + c.magenta)
    color = ask("What is your favorite color?" + c.magenta)
