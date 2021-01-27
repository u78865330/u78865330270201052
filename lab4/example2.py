year = int(input("Please enter a year: "))

year1 = year%4 
year2 = year%400 

if year1 ==0 and year2 ==0:
 print("a leap year")

else: 
 print("not leap year")