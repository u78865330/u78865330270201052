inputlist = []
for _ in range(5):
  name = input("Enter name :")
  age = int(input("Enter age :"))
  person = (name,age)
  inputlist.append(person)

for name,age in inputlist:
  if age > 18:
    print(name)