#a = [1,12,21,13,3,2,True,23.55,"saif"] HETEREOGENOUS NATURE
# LIST CAN STORE DUPLICATES AND THEY ARE MUTABLE
#print(a)
#indexing and slicing  modifying in list 

#print(a[6])
#for i in range(len(a)):#
    #print(a[i])

#for i in a:#
    #print(i)
    
#a[7]= 'malooq'
#for i in range(len(a)):#
   #print(a[i])
    
 # reference copy
# a = [10,20,30,45,50]
# b = a
# b[0]=100
# print(a) 
# print(b)  

# # shallow copy
# a = [20,30,40,50,60]
# b = a.copy()
# b[0]=200
# print(a)#a doesn't change
# print(b)


#using multiple methods in python
#a.append(9)
#for i in range(len(a)):
   # print(a[i])
    
#using insert function
#a.insert(1,1)
#for i in range(len(a)):
   # print(a[i])
   
   
#find the greatest element in the list
# l=[2,4,7,98,32,1]
# largest = l[0]
# second_largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i]>largest:
#         second_largest=largest
#         largest = l[i]
#         index = i
#     elif l[i]>second_largest:
#         second_largest=l[i]
#     #elif l[i]<largest:
#      #   second_largest == l[i]

    
# print(f"your largest number is {largest} at index {index}")
# print(f"your second largest number is {second_largest}")
    
        
# WE WANT TO CHECK WHETHER A GIVEN LIST IS SORTED IN DESCRNDING ORDER OF NOT
a = [90,80,60,7,50,30,20,10,5,1]

for i in range(len(a)-1):
   if a[i]>a[i+1]:
      continue
     
   else:
      print("List is not sorted")
      break

else:
   print("List is sorted")

#Q= Rotate a list one element to the left
a = [90,80,60,7,50,30,20,10,5,1]
for i in range(len(a)-1):
   a[i],a[i+1] = a[i+1],a[i]

print(a)

