#Taking input
P = int(input('Enter principal amount:'))
R = int(input('Enter rate of interest:'))
T = int(input('Enter Time:'))

#Calculate compound interest
Amount = P*(1 + R/100)**T
CI = Amount - P

#Show result
print("Compound interest is:",CI)