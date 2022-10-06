# function for arithmetic sums


from ast import Break
import sys

def arithmetic():
    try:
        first_element = int(input("What is the value of a1? "))
        differens = int(input("What is the value of d? "))
        amount = int(input("What is the value of n? "))

        n_element = first_element + differens * (amount - 1)

        sum_arithmetic= amount * ((first_element + n_element) / 2)

        return round(sum_arithmetic,0)
    except ValueError:
        print("Wrong type of input!")
        sys.exit()