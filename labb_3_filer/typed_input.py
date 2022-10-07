from operator import truediv
import colorama

def check_int(prompt):
    """function that """
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

#denna "fungerar inte" går vidare även om man skriver annat än a och b
def check_ga(prompt):
    while True:
        value = str((input(prompt)).lower())
        if value == "g" or "a":
            break
        else:
            print(f"{colorama.Fore.RED}Wrong input! try again")
    return value
