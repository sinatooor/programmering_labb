import typed_input
import colorama

class Student:
    # student is a object with 3 parameters
    def __init__(self, first_name, last_name, id_number):



        if not id_number or not first_name or not last_name:
            raise ValueError("Missing value")
        if len(str(id_number)) != 10:
            raise ValueError("Incorrect ID number")
        if isinstance(id_number, int) != True:
            raise ValueError("Incorrect ID number, It should be digits")

        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        M = colorama.Fore.MAGENTA
        W = colorama.Fore.WHITE
        return f"{M}Name: {W}{self.first_name} {self.last_name} {M}ID number: {W}{self.id_number}"
    




def main():

    while True:
        try:
            full_name = (
                input("Write first name and last name with space: ").title().strip()
            )
            first_name, last_name = full_name.split() #splits with empty space
        except ValueError:
            print(f"{colorama.Fore.RED}Type only first and last name! {colorama.Fore.WHITE}")
        else:
            break
    while True:
        try:   
            id_number = typed_input.check_int("What is the id number? ")
            School.students.append(Student(first_name, last_name, int(id_number)))
        except ValueError:
            print(f"{colorama.Fore.RED}Invalid id number! {colorama.Fore.WHITE}")
        else:
            break
        
    object1 = Student(input("First name: "), input("Last name: "), int(input("Id number: ")))
    object2 = Student(input("First name: "), input("Last name: "), int(input("Id number: ")))
    object3 = Student(input("First name: "), input("Last name: "), int(input("Id number: ")))

    print("Here are all the created objects:")
    print(object1)
    print(object2)
    print(object3)


main()