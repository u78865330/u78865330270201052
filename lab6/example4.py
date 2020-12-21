number=int(input("Plase enter a number"))
liste1=[]
counter=0
for i in range(0,number):
    liste2=[]
    
    for i in range(0,number):
        
        if i==counter:
            liste2.append(1)
        else:
            liste2.append(0)
    liste1.append(liste2)
    counter+=1
for i in liste1:
    print(*i)
    