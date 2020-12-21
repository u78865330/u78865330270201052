email=input("Please enter an email.").lower()
number_of_signs=email.count("@")
if number_of_signs==1:
    
    x=email.split("@")
    y=x[0]
    z=x[1]
for i in y:
    if i==".":
        y=y.replace(".","")
        if y=="ceng113" and z=="example.com":
            print("True")
        else:
            print("False")
else:
    print("Plase write valid email.")