# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

S1 = int(input('Enter marks:'))
S2 = int(input('Enter marks:'))
S3 = int(input('Enter marks:'))
S4 = int(input('Enter marks:'))
S5 = int(input('Enter marks:'))

#A = 90 to 100
#B = 75 to 90
#C = 60 to 75
#Bellow average = 35 to 60
#Fail = Bellow 35

allmarks = S1+S2+S3+S4+S5
percentage = allmarks / 5
print(percentage)

if(percentage >= 90 and percentage <= 100):
    print('grade A')
elif(percentage >= 75 and percentage <= 90):
    print('grade B')
elif(percentage >= 60 and percentage <= 75):
    print('grade C')
elif(percentage >= 35 and percentage <= 60):
    print('Bellow average')
elif(percentage < 35):
    print('Fail')
else:
    print("wrong marks")