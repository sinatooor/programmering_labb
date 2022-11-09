from operator import truediv
import colorama



print("sina")

def check_int(prompt):
    """function that checks so input is int"""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print(f"{colorama.Fore.RED}Wrong input! try again with an integer")

        else:
            if value > 0:
                break
            print(f"{colorama.Fore.RED}Wrong input! n needs to be bigger than 0")

    return value


def check_float(prompt):
    """function that checks so input is float"""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print(f"{colorama.Fore.RED}Wrong input! try again with a float")
        else:
            break
    return value


def check_float_not_one(prompt):
    """function that checks so input is float and 1"""
    while True:
        try:
            value = float(input(prompt))

        except ValueError:
            print(f"{colorama.Fore.RED}Wrong input! try again with a float")
        else:
            if value == 1:
                print(
                    f"{colorama.Fore.RED}Wrong input! it can not be 1 try again with another float"
                )
            else:
                break
    return value


def check_ga(prompt):
    """function that checks so input is either g or a"""
    while True:
        value = str((input(prompt)).lower())
        if value == "g" or value == "a":
            return value
        else:
            print(f"{colorama.Fore.RED}Wrong input! try again with a or g")


