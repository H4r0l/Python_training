import sys
import datetime

age = input('How old are you?\n ')
year = datetime.datetime.now().year
name = input('What is your name?\n ')
heigh = input('How tall are you? (In centimeters)\n ')
stud = input('Are you a student? (Yes / No)\n ')
student = stud.lower()

if student != 'yes' and student != 'no':
    print('Please answer with yes or no')
    sys.exit()

remaining = (year - int(age)) + 100

print(f'Report: \n Name: {name} \n Age: {age} \n Height: {heigh} \n Student: {student} \n You will turn 100 years in {remaining} ')