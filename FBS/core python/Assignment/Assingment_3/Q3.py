# Write a program to input angles of a triangle and check whether triangle is valid or not. 

a = int(input('Enter A angle:'))
b = int(input('Enter B angle:'))
c = int(input('Enter c angle:'))

sum = a+b+c

if(sum == 180):
    print("Angle of triangle is valid")
else:
    print("angle of triangle is not valid")
