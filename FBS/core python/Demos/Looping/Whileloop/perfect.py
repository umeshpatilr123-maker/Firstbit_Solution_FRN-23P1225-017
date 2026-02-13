num = int(input('Enter number:'))
sum = 0
for i in range(1, num):
    if(num % 1 == 0):
        sum += 1 #sum = sum + 1
if(num == sum):
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect numbere')