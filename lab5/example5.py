true_password = input("Please save your password:\n")
lis = []
lis1 = []
lis.append(true_password)
for i in lis:
    lis1 = list(i)
letter = []
while True:
    enter_password = input("Enter password:\n")

    if enter_password != true_password:
        if "help" == enter_password:
                print(lis1[0])
        else:
            print("Wrong")
    else:
        print("Welcome")
        break