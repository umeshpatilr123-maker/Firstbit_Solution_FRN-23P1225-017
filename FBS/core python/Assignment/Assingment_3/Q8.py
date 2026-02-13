# Write a program to prompt user to enter userid and password. After verifying userid and password 
# display a 4 digit random number and ask user to enter the same. If user enters the same number 
# then show him success message otherwise failed. (Something like captcha) 

import random

userid = input('Enter your userid:')
password = input('Enter your password:')

uid = 'umesh@123'
passkey = '12345'

if(userid == uid and password == passkey):
    otpnumber = random.randint(1111,9999)
    print(otpnumber)
    otp = int(input("Enter OTP:"))
    
    if(otp == otpnumber):
        print("login successfully")
    else:
        print("invalid OTP")


elif(userid == uid and password != passkey):
    print('Invalid password')
else:
    print('Invalid:Try again')