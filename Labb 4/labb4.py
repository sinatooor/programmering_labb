class Student:
    # student is a object with 3 parameters
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
      return str(self.first_name +  self.last_name + self.id_number)
        
        
        
#main function       
def main():
    
    first_name = input("First name: ")
    last_name = input("Last name: ")
    id_number = input("Id number: ")
    student = Student(first_name,last_name,id_number)

    print(student)

main()
