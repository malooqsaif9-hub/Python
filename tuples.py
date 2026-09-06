
# this is a tuple 
coord = (10,20)
#single element tuple comma is essential
single = (10,)
not_a_tuple = (10)#just an int

# Accesing elements in tuple 
colors = ("red","blue","green")
print(colors[0])
print(colors[1:3])

#Immutability 
#colors[0]="black" this gives an error

#But if a tuple contains a mutable object, that object can still change:
t = ([1, 2], [3, 4])
print(t[0].append(99))   # ✅ → ([1, 2, 99], [3, 4])

#Tuples only have two built-in methods (since they're immutable):
t = (1,2,3,4,5,6,2)
print(t.count(2))
print(t.index(2))
for i in t:
    print(i)