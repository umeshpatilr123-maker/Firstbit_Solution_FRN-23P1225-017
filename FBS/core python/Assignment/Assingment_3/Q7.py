# Write a program to check if user has entered correct userid and password. 

userid = input('Enter your userid:')
password = input('Enter your password:')

uid = 'umesh@123'
passkey = '12345'

if(userid == uid and password == passkey):
    print('Login successfully')
elif(userid == uid and password != passkey):
    print('Invalid password')
# elif(userid != uid and password == passkey):  -----> doubt
#     print('Invalid userid')
else:
    print('Invalid:Try again')