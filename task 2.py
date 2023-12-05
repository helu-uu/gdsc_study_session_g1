char = input("Enter a character: ")

for i in range(1, 6):
    if i == 1:
        print(char * i)
    elif i == 2:
        print(char * i)
    elif i == 3:
        print(char * (i+1))
    elif i == 4:
        print(char * (i+2))
    else:
        print(char * (i+3))