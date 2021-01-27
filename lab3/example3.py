gpa = float(input('Enter your gpa: '))

number_of_Lectures = int(input('Enter your number of lectures: '))

if (gpa <= 2.0 and number_of_Lectures < 47) :
   print('Not enough number of lectures and GPA!')

elif (gpa >= 2.0 and number_of_Lectures < 47 ) :
    print('Not enough number of GPA!')
elif number_of_Lectures <= 47 :
    print('Not enough number of lectures')
else:
    print('GRADUATED!!!')