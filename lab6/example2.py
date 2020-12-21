grades=[]
number_of_students=int(input("Number of students:"))
best_grades=[]
avarage_grades=[]
for i in range(number_of_students):
    liste=[]
    midterm1=int(input("Please enter midterm1"))
    midterm2=int(input("Please enter midterm2"))
    final=int(input("Please enter final exam."))
    grades.append([midterm1,midterm2,final])
    for i in grades:
        avarage_grade=i[0]*0.3+i[1]*0.3+i[2]*0.4
        avarage_grades.append(avarage_grade)
        
    if avarage_grade>90:
        best_grades.append(avarage_grade)
print(avarage_grades)
print(best_grades)