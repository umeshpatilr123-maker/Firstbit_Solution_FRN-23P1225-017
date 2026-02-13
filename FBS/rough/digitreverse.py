num = 123

d1 = num // 100
num = num % 100

d2 = num // 10
num = num % 10

d3 = num

x = str(d3)
y = str(d2)
z = str(d1)


print(x+y+z)