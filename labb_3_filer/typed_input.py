from operator import truediv
import colorama

def check_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print(f"{colorama.Fore.RED}Wrong input! try again")
        else:
            break
    return value

def check_float(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print(f"{colorama.Fore.RED}Wrong input! try again")
        else:
            break
    return value

def check_ga(prompt):
    while True:
        value = (input(prompt)).lower()
        if value == "g" or "a":
            break
        else:
            print(f"{colorama.Fore.RED}Wrong input! try again")
    return value