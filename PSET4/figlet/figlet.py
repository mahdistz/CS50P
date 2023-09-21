from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts_list = figlet.getFonts()

if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 3:
        if not sys.argv[1] in ["-f", "--font"]:
            sys.exit("Invalid usage")
        elif sys.argv[2] not in fonts_list:
            sys.exit("Invalid usage")
        else:
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print("Output: ",figlet.renderText(text))
    else:
        text = input("Input: ")
        random_item = random.choice(fonts_list)
        figlet.setFont(font=random_item)
        print("Output: ",figlet.renderText(text))
else:
    sys.exit("Invalid usage")

