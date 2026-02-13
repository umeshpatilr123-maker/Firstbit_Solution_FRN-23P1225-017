#write a program to accept year from user and check if it is a leap year or not.

year = int(input('Enter a year you want to check it is a leap year or not:'))

if year % 4 != 0:
    print('not a leaf year')
elif year % 4 == 0:
    print('leaf year')
elif year % 100 != 0:
    print('leaf year')
elif year % 100 == 0:
    print('not a leaf year')
elif year % 400 != 0:
    print('not a leaf year')
elif year % 400 == 0:
    print('leaf year')
