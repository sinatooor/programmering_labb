# Sina Rajaeeian och Oliver folke
# function for arithmetic sums
import sys
import colorama
import typed_input

colorama.init(autoreset=True)
# reset the color back to white after each print function


def arithmetic():
    """function that calculates arithmetic sums"""
    first_element = typed_input.check_float("What is the value of a1? ")
    differens = typed_input.check_float("What is the value of d? ")
    amount = typed_input.check_int("What is the value of n? ")

    # function for sum
    n_element = first_element + differens * (amount - 1)
    sum_arithmetic = amount * ((first_element + n_element) / 2)

    return round(sum_arithmetic, 0)


def geometric():
    """function that calculates geometric sums"""
    first_element = typed_input.check_float("What is the value of g1? ")
    quota = typed_input.check_float_not_one("What is the value of q? ")
    amount_n = typed_input.check_int("What is the value of n? ")

    # function for sum
    sum_geometric = first_element * (((quota**amount_n) - 1) / (quota - 1))
    return round(sum_geometric, 0)


# information of how to choose sum type
print(
    f'{colorama.Fore.GREEN}\n \nfor arithmetic input "a" \n' 'for  geometric input "g"'
)

# First choice of sum type
first_answer = typed_input.check_ga(
    f"Is your first sum arthmetic or geometric? {colorama.Fore.GREEN}"
)  

print(end="")
if first_answer == "a":
    first_result = arithmetic()  # Stores

elif first_answer == "g":
    first_result = geometric()


# Second choice of sum type
second_answer = typed_input.check_ga(
    f"Is your second sum arthmetic or geometric? {colorama.Fore.GREEN}"
)  

print(end="b")
if second_answer == "a":
    second_result = arithmetic()

elif second_answer == "g":
    second_result = geometric()


# comparison of the answers
if first_result < second_result:
    print(f"{colorama.Fore.CYAN}Second sum is bigger")

elif first_result > second_result:
    print(f"{colorama.Fore.CYAN}First sum is bigger")

elif first_result == second_result:
    print(f"{colorama.Fore.CYAN}The answers are equal")
