day=input('Enter the weak days:')
amt=int(input('Enter the amount:'))
if day.lower()=='sunday' and amt>=5000:
    dis=(amt*40)/100
    amt=amt-dis
    print('After 40% discount ,final price:', amt)
elif day.lower()=='sunday' and amt>=4000:
    dis=(amt*20)/100
    amt=amt=dis
    print('After 20% discount:',amt)
else:
    print('No discount:',amt)