a = 'A'
print(ord(a))
a = 65 
print(chr(a))
#-------------------INDEXING IN STRING----------------------
a = 'SAIF'
print(a[2])

#-------------------STRING SLICING-----------------------------
a ='saif malooq'
print(a[0:5])  #[start:stop:steps]
print(a[0:5:2])
print(a[5::])
print(a[::-1])
print(len(a))
# a[1] = 'e'  Immutable Nature = you cannot change the string 
##-------------------TYPECONVERSION----------------------------
a = 12
print(type(a))
a = str(a)
print(type(a))
a=bool(a)
print(bool(a))
#7 falsy values of boolean datatype
#false," ",0,0.0,[],{},()

#name='saif malooq'#
#age=20
#print(f"my name is {name} and my age  is {20}")
#num = int(input("enter your number "))
#print(num)
#print(type(num))

#age=int(input("enter your age "))
#print(f"your age is {age}")

#-----------ARITHMETIC OPERATORS----------------------
w = 5
u = 100
print(w+u)
print(w-u)
print(w*u)
print(w/u)
print(w//u) #flow division
print(w**u)
print(32%5)