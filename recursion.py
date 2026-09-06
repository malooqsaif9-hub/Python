# recursion: recursion is the  process of defining something in terms of itself
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
        
    
print(factorial(5))       
    
    
#fibonacci sequence 
def fibinacci(n):
    a,b = 0,1
    for i in range(n):
        print(a,end=" ")
        a,b = b,a+b
    print()
        
fibinacci(6)
#by recursive approach

def fibonaci(n):
    if(n<=1):
        return n
    return fibonaci(n-1)+fibonaci(n-2)
for i in range(6):
     print(fibonaci(i),end=" ")

