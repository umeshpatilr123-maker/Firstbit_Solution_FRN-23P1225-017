# Write a program to find the are of perimeter of following figure

l = int(input('Enter length:'))
b = int(input('Enter breadth:'))
r = int(input('Enter radius:'))

pie = 3.14

area = l * b * 0.5 * pie * r
perimeter = 2*b+l+pie+r

print(f'Area is {area}')
print(f'perimeter is {perimeter}')