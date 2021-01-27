age = float(input('please enter your age: '))

t = 3

if (age<6) or (60<age):
    t = 0
    print("price: ",t)

elif (6<age) and (age<18):
  t = t/2
  print("price: ",t)
else:
  print("price: ",t)