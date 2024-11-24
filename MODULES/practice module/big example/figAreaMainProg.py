from figMenu import menu
from figCricle import area as ca
from figSquare import area as sa
from figTriangle import area as ta
from figReactangle import area as ra

import sys
while(True):
    menu()
    ch=input("Enter your choice")
    match(ch):
        case "R"|"r":
            ra()
        case "T"|"t":
            ta()
        case "S"|"s":
            sa()
        case "C"|"c":
            ca()
        case "E"|"e":
            print("Thanks for using this program")
            sys.exit()
        case _:
            print("Your selection action is wrong --- Try again")