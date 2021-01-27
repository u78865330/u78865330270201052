x = int(input("How many numbers will you enter? "))
e = 0
o = 0
for i in range(1, x+1):
  y = int(input("Please enter a value: "))
  if y % 2 ==1:
    o += 1
  else:
    e += 1
print("percentage of even numbers:", e/(o+e)*100)