#for loop :- works only at a certain number
#while loop :- works until to reach the conditons 
# general example or  syntax of for loops
#n = int(input("please tell me which table you want "))
#for i in range(n,(n*10)+1,n):
#    print(i)


#num = int(input("please tell me your number :- "))
#sum = 0
#for i in range(1,num):#
   ##   sum = sum +i
        
#if sum == num:
   # print("this is a perfect number")
#else:
  #  print("this is not a perfect number")
  
  
# accessing string using for loop in reverse order
#a ='SAIF MALOOQ IS A BAD GUY'

#for i in range(len(a)-1,-1,-1):
    #print(a[i])
    
for i in range(-10,21):
   print(i)   
    
    


#/// while loop ///
a = 256
while a > 0:
    print(a % 10)
    a = a//10

