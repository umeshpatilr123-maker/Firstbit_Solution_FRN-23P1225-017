

num = int(input('Enter 3 digit num:'))

a = num // 100
num = num % 100
b = num // 10
num = num % 10
c = num // 1
num = num % 1

if b == 0.5*a and a == 0.5*c:
    print('Yes, you have done it')
else:
    print('Plase try next time')
