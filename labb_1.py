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
        

# function for geometric sums
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
        

# information of how to choose sum type
print ("\n \nfor arithmetic input \"a\" \n" "for  geometric input \"g\"" )

# First choice of sum type
first_answer = str(input("Is your first sum arthmetic or geometric?"))
if first_answer == "a":
    first_result = arithmetic() # Stores 

elif first_answer == "g":
    first_result = geometric()

# Second choice of sum type
second_answer = str(input("Is your second sum arthmetic or geometric?"))

if second_answer == "a":
    second_result = arithmetic()


elif second_answer == "g":
    second_result = geometric()

second_result= int(second_result)
first_result = int(first_result)

# comparison of the answers
if first_result < second_result:
    print("Second sum is bigger")

elif first_result > second_result:
    print ("First sum is bigger")

elif first_result == second_result:
    print("The answers are equal")


564




