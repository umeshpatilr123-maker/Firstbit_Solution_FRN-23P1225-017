# Write a program to convert days into years, weeks and days. 

days = int(input('Enter days:'))

y = days // 365
days = days % 365

w = days // 7
days = days % 7

print(y)
print(w)
print(days)