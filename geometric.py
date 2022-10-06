# function for geometric sums

from ast import Break
import sys


def geometric():
    try:
        first_element = int(input("What is the value of g1? "))
        quota = int(input("What is the value of q? "))
        amount_n = int(input("What is the value of n? "))
        sum_geometric = first_element * (((quota**amount_n) - 1) / (quota - 1))
        return round(sum_geometric,0)
    except ValueError:
        print("Wrong type of input!")
        sys.exit()