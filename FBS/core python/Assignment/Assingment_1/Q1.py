# Write a program to calculate the percentage of student based on marks of any 5 subjects. 

S1 = int(input('Enter sub1 marks:'))
S2 = int(input('Enter sub2 marks:'))
S3 = int(input('Enter sub3 marks:'))
S4 = int(input('Enter sub4 marks:'))
S5 = int(input('Enter sub5 marks:'))

sum = S1+S2+S3+S4+S5
Percentage = sum/5

print(f'Percentage of student is:{Percentage}%')