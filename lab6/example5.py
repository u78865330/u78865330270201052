number=int(input("Please enter a number"))
liste1=[]
c=0
p=0
n=int(number**0.5)
for i in range(0,n):
    liste2=[]
    for j in range(0,n):
        x=int(input("Please enter a number"))
        liste2.append(x)
    liste1.append(liste2)
for i in range(n):
    c+=liste1[p][p]
    p+=1
print(c)