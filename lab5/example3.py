number1=(input("Please enter a number: "))
number2=(input("Please enter a number: "))
c=0
if len(number1)>len(number2):
    
    for i in number1:
        if i in number2:
            if number1.index(i)==number2.index(i)+len(number1)-len(number2):
                c+=1
elif len(number2)>len(number1):
    for i in number1:
        if i in number2:
            if number2.index(i)==number1.index(i)+len(number2)-len(number1):
                c+=1
else:
    for i in number1:
        if i in number2:
            if number1.index(i)==number2.index(i):
                c+=1
print(c)