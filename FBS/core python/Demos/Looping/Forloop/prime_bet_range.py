#WAP tp print prime numbers between range
n = int(input('Enter number till prime number you want to print'))
for num in range(2, n):
    for i in range(2, num):
        if(num % i == 0):
            break
    else:
        print(num)

#WAP to print first n prime numbers

# n = int(input('Enter how many prime numbers you want:'))
# count = 0
# num = 2

# while count < n:
