# Write a Program to input two angles from user and find third angle of the triangle.

a = int(input("enter first angle of triangle:"))
b = int(input("enter second angle of triangle:"))
c = 180

sum = a + b
angle = c - sum

print("Third angle of triangle is:",angle)