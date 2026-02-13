# Write a program to calculate profit or loss.

NetProfit = int(input('Enter amount:'))
productPrice = 500

P_L = NetProfit - productPrice

if(NetProfit > 1000):
    print("invalid amount")
elif(productPrice <= NetProfit):
    print("profit of",P_L)
elif(productPrice >= NetProfit):
    print("loss of",P_L)

#2nd way
# ap = int(input('Enter actual price:'))
# sp = int(input('Enter selling price:'))

# if(sp > ap):
#     profit = sp - ap
#     print('profit =',profit)
# elif(ap > sp):
#     loss = ap - sp
#     print('loss=',loss)
# else:
#     print('no profit no loss')



