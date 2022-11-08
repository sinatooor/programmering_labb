

def main():
    friends = []
    file = open('students.txt', 'r')
    for line in file:
        friends.append(line)
    
    i = 1
    count = 0
    while i == 1:
        print(f"Namn: {friends[count+2]}, {friends[count+1]} Personnr: {friends[count]}")
        if friends[count] == "":
            break
        count = count+3

    file.close()





main()
