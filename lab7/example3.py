employees = dict()
for _ in range(5):
    name = input("Enter name:")
    salary = int(input("Enter salary:"))
    employees[name] = salary
# Names are not necessarily sorted by their salaries. (We didn't explicitly say this)
# We can print them in any order as long as they are the top 3.
best_three_salaries = sorted(employees.values(),reverse=True)[:3]
print(best_three_salaries)
for name in employees.keys():
    salary = employees[name]
    if salary in best_three_salaries:
        print(name)
