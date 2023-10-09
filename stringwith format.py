id = 101
name='harihar'
city='Noida'
#str1="Hello My ID is {} Name is {} and I am from {} ".format(id,name,city) --This is also working.
str1="Hello My ID is {a} Name is {b} and I am from {c} ".format(a=id,b=name,c=city)
print(str1)