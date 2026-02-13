# Write a program to input all sides of a triangle and check whether triangle is valid or not.

####Logic: sum of any two sides is greater than the third side

a = int(input('Enter A angle:'))
b = int(input('Enter B angle:'))
c = int(input('Enter c angle:'))

if a + b > c and b + c > a and a + c > b:
    print('Valid angle')
else:
    print('invalid')