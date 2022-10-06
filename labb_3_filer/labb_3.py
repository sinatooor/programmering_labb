import typedinput

def geometric():
    try:
        first_element = int(input("What is the value of g1? "))
        quota = int(input("What is the value of q? "))
        amount_n = int(input("What is the value of n? "))
        sum_geometric = first_element * (((quota**amount_n) - 1) / (quota - 1))
        return round(sum_geometric,0)
    except ValueError:
        print("Wrong type of input!")
        geometric()

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
        arithmetic()

