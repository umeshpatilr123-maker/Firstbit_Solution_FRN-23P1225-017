# Write a program to calculate simple interest based on principal, Rate and Time

principal = int(input('Enter principal value:'))
Rate = int(input('Enter Rate:'))
Time = int(input('Enter Time:'))

SI = principal * Rate * Time/100

print(f'simple interest based on principal, Rate and Time is {SI}')