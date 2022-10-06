# Sina Rajaeeian och Oliver folke
# function for arithmetic sums
import sys
import colorama
colorama.init(autoreset=True)

def arithmetic():
    try:
        first_element = int(input("What is the value of a1? "))
        differens = int(input("What is the value of d? "))
        amount = int(input("What is the value of n? "))
        # funtion for sum
        n_element = first_element + differens * (amount - 1)

        sum_arithmetic= amount * ((first_element + n_element) / 2)

        return round(sum_arithmetic,0)
    except ValueError:
        print(f"{colorama.Fore.RED}Wronge type of input!")
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
        print(f"{colorama.Fore.RED}Wronge type of input!")
        sys.exit()
    except ZeroDivisionError:
        print(f"{colorama.Fore.RED}First value can not be count!")
        sys.exit()
    

# information of how to choose sum type
print (f"{colorama.Fore.GREEN}\n \nfor arithmetic input \"a\" \n" "for  geometric input \"g\"" )

# First choice of sum type
first_answer = str(input(f"Is your first sum arthmetic or geometric?{colorama.Fore.GREEN}"))
print(end="")
if first_answer == "a":
    first_result = arithmetic() # Stores 

elif first_answer == "g":
    first_result = geometric()

# Second choice of sum type
second_answer = str(input(f"Is your second sum arthmetic or geometric?{colorama.Fore.GREEN}"))
print(end="")

if second_answer == "a":
    second_result = arithmetic()
elif second_answer == "g":
    second_result = geometric()

# comparison of the answers
if first_result < second_result:
    print(f"{colorama.Fore.CYAN}Second sum is bigger")

elif first_result > second_result:
    print (f"{colorama.Fore.CYAN}First sum is bigger")

elif first_result == second_result:
    print(f"{colorama.Fore.CYAN}The answers are equal")