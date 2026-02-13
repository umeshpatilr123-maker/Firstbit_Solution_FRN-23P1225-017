#  Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input('Enter gender M/F:')
age = int(input('Enter age:'))

if gender in ['Female', 'FEMALE', 'female', 'f', 'F']:
    if age > 17:
        print('This female is eligible to marriage')
    else:
        print('This female is not eligible to marriage')
else:
    if age > 20:
        print('This male is eligible to marriage')
    else:
        print('This male is not eligible to marriage')