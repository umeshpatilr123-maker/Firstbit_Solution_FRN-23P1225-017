# Write a program to accept distance in km and convert it into meter and centimeter both

km = int(input('Enter Killometers:'))

meter = 1000 * km
centimeter = 100 * meter

print(f'The converted distance of meter is {meter}')
print(f'The converted distance of centimeter is {centimeter}')