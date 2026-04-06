
from colorama import init, Fore, Back, Style

# Initialize Colorama

init(autoreset=True)

print(Fore.RED + "This is red text")

print(Back.GREEN + "This has a green background")

print(Style.BRIGHT + Fore.BLUE + "This is bright blue text")

print("This text will be back to normal because of autoreset=True")

num=int(input(Style.BRIGHT + Fore.BLUE +"enter a number"))