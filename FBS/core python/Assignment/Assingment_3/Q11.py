#  Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition : 
# a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full. 

ticket_amt = 1000

child = ticket_amt * 0.70
senior = ticket_amt * 0.50
full = ticket_amt

P1 = int(input('Enter age:'))

if(P1 < 12 and P1 > 0):
    payablep1 = child
    print(f"dicount 30%:{payablep1}")
elif(P1 < 0):
    payablep1 = child
    print('invalid amount')
elif(P1 > 59 and P1 < 110):
    payablep1 = senior
    print(f"discount 50%:{payablep1}")
elif(P1 > 110):
    print('invalid amount')
else:
    payablep1 = full
    print(f"No discount for adult:{payablep1}")

P2 = int(input('Enter age:'))

if(P2 < 12):
    payablep2 = child
    print(f"discout 30%:{payablep2}")
elif(P2 > 59):
    payablep2 = senior
    print(f'discount 50%:{payablep2}')
else:
    payablep2 = full
    print(f'No discout for adult:{payablep2}')

P3 = int(input('Enter age:'))

if(P3 < 12):
    payablep3 = child
    print(f'discout 30%:{payablep3}')
elif(P3 > 59):
    payablep3 = senior
    print(f'discout 50%:{payablep3}')
else:
    payablep3 = full
    print(f'No discout for adult:{payablep3}')

P4 = int(input('Enter age:'))

if(P4 < 12):
    payablep4 = child
    print(f'discout 30%:{payablep4}')
elif(P4 > 59):
    payablep4 = senior
    print(f'discout 50%:{payablep4}')
else:
    payablep4 = full
    print(f'No discout fo adult:{payablep4}')

P5 = int(input('Enter age:'))

if(P5 < 12):
    payablep5 = child
    print(f'discout 30%:{payablep5}')
elif(P5 > 59):
    payablep5 = senior
    print(f'discout 50%:{payablep5}')
else:
    payablep5 = full
    print(f'No discout for adult:{payablep5}')

total_amt_of_travel = payablep1+payablep2+payablep3+payablep4+payablep5
print('Total payable',total_amt_of_travel)
