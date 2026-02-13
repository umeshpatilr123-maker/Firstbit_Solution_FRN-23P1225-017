# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input('Enter A angle:'))
b = int(input('Enter B angle:'))
c = int(input('Enter c angle:'))

if(a == b == c):
    print('equilateral')
elif(a == b or b == c or a == c):
    print('isosceles')
elif(a != b != c):
    print('scalene')