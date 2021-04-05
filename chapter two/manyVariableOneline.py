
name,age = 'toufiq. ', 20

print('hello ' + name + 'your age is '+ str(age))


# when you declare many variable in oneline then you must maintain the order of variable otherzise wrong data will be stored . Exmple below

# wrong way
name,age,country = 'Bangladesh','limon',20
print(name,country,age)


# correct way
name,age,country = 'Mostafiz',20,'Bangladesh'
print(name+'\n',country+'\n',str(age)+'\n')


#another exmple
# you can stored this way also

a=b=c=100
print(a+b+c)
