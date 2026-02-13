gender = input('Enter gender (M/F):')  #F, f, female, Female
age = int(input('Enter age:'))
# if gender == 'F':
if gender in ['f', 'F', 'female', 'Female', 'FEMALE']:
    if age > 17:
        print('Eligible for marriage.')
    else:
        print('Not elligible')
else:
    if age > 20:
        print('Eligible for marriage.')
    else:
        print('Not eligible')


# check person is eligible for voting or not

age = int(input('Enter age:'))
if age > 17:
    print('Eligible for voting')
else:
    print('Not eligible')



