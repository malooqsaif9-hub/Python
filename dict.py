# dict = {1:"hello",2:200} #keys and values 
# print(type(dict))

# print(dict[1])#acces values through keys

# dict.update({3:400})#updating
# dict[4]=600#updating
# del dict[2]# deleting
# print(dict)

# #traversing a dictionary
# for i in dict:
#     print(i)# this gives only keys 

# for i in dict:
#     print(dict[i])#this gives values

# for i in dict.values():
#     print(i)#this will also gives values 

# # help(dict)

# dictionary quesstions
# write a python program to merge two dictionaries 

# d1 = {10:200,20:400,30:600}
# d2 = {30:800,40:1000,50:1500}
# d1.update(d2)
# print(d1)

# for i in d2:
#     d1[i] = d2[i]
# print(d1)

# wap to sum all the values in dictonary
# sum = 0
# d1 = {10:200,20:400,30:600}
# for i in d1:
#     sum+=d1[i]
# print(sum)

# count the frequency of each element in the list

# a = [1,1,1,1,2,2,3,3,3,4,4,4,4,4,5,5,5,6]
# # suppose if i have to calculate only one number frequency
# count = 0
# for i in a:
#     if i == 1:
#         count+=1
# print(count)       
# # now with different logic using dictionary
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

