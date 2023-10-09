"""
x=2.3
print(type(x))

x=2.4
y=int(x)
print(y)

a='23'
b=int(a)
print(type(b))

a= input ('Enter a number:')
b= input('Enter a num:')
c=a+b
print(c) # output will be 1020 when we will provide value of a=10 and b=20. Always provide string value.

a= input ('Enter a number:')
b= input('Enter a num:')
x=int(a)
y=int(b)
z=x+y
print(z) # after type costing it will be provide output some of x=10 and y=20 then print z=30.


a= int(input ('Enter a number:')) # first run inner function then outer.
b= int(input('Enter a num:'))
c=a+b
print ('Print sum is :', c)

"""
print ('Print sum is :',int(input('Enter a num:'))+int(input('Enter a number:')))

