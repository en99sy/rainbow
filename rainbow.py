import colorama

from colorama import init
init()
from colorama import Fore, Back, Style

colors = {"green": Fore.GREEN,
          "red": Fore.RED,
          "yellow": Fore.YELLOW,
          "blue": Fore.BLUE,
          "cyan": Fore.CYAN,
          "magenta": Fore.MAGENTA,
          "white": Fore.WHITE}

def clearColorSettings():
    print(Style.RESET_ALL, end = '', flush = True)

def printTwoColor(string, c1, c2, alt = "word", delim = "|"):
    c1 = colors[c1.lower()]
    c2 = colors[c2.lower()]
    if alt == "word":
        parts = string.split()
    elif alt == "delim":
        parts = string.split(delim)
    elif alt == "char":
        parts = list(string)
    else:
        print("Error: unknown alternating argument.")
    i = 0
    for p in parts:
        if i % 2 == 0:
            print(c1, end = '', flush = True)

        else:
            print(c2, end = '', flush = True)
        i += 1
        if alt == "word" or alt == "delim":
            print(p, end = ' ', flush = True)
        else:
            print(p, end = '', flush = True)

    print(Style.RESET_ALL)

def printXColor(string, c_list, alt = "word", delim = "|"):
    x = len(c_list)
    if alt == "word":
        parts = string.split()
    elif alt == "delim":
        parts = string.split(delim)
    elif alt == "char":
        parts = list(string)
    else:
        print("Error: unknown alternating argument.")
    i = 0
    for p in parts:
        for j in range(0, x):
            if i % x == j:
                print(colors[c_list[j].lower()], end = '', flush = True)
                if alt == "word" or alt == "delim":
                    print(p, end = ' ', flush = True)
                else:
                    print(p, end = '', flush = True)
        i += 1

    print(Style.RESET_ALL)

def printRainbow(string, alt = "word", delim = "|"):
    c_list = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    printXColor(string, c_list, alt, delim)

def printColor(string, color, set = False):
    c = colors[color.lower()]
    print(c, end = '', flush = True)
    print(string, end = '', flush = True)
    if set:
        print("")
    else:
        print(Style.RESET_ALL)



def main():
    printTwoColor("they all lived happily ever after", "CYAN", "red")
    printTwoColor("they all lived happily ever after","Cyan", "rED", alt = "char")
    printTwoColor("they all lived|happily ever after", "cyan", "red", alt = "delim")

    printXColor("they all lived happily ever after", ["CYAN", "RED", "YELLOW", "GREEN"])
    printXColor("they all lived happily ever after", ["CYAN", "RED", "YELLOW", "GREEN"], alt = "char")
    printXColor("they all.lived happily.ever.after", ["CYAN", "RED", "YELLOW", "GREEN"], alt = "delim", delim = ".")

    printRainbow("they all lived happily ever after", alt = "char")

    printColor("this is magenta", "magenta")
    print("This is normal.")
    printColor("this is yellow", "YELLOW", set = True)
    print("This is still yellow because I used set = True.")
    clearColorSettings()
    print("Now we are back to normal.")

main()
