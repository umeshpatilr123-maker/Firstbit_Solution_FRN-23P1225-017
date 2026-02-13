# Program to Find the Roots of a Quadratic Equation 

a = int(input('Enter number:'))
b = int(input('Enter number:'))
c = int(input('Enter number:'))

d = b*b-4*a*c

r1 = (-b + d**0.5)/(2*a)
r2 = (-b - d**0.5)/(2*a)

print(f'Root of Quadratic equation is:{r1} and {r2}')