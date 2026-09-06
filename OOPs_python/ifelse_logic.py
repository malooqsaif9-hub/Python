# take two user inputs and determine which number is equal or largest
a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))

if a>b:
    print(f"{a} is greater ")
    
elif b>a:
    print(f"{b} is greater")
else: 
    print(f" {a} is = {b}")
    