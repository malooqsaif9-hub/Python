# try = " wrap the block of code that can cause exception "
# exception = " handle the exception if occurs "
# else = " run code if no exception occurs "
# finally = " run the code no matter what whether there is an exception "
# raise = ' manually throw an exception'

from sys import exception
a = int(input("enter your number: "))

try:
    print(10/a)
except Exception as err:
    print(f"sorry there is an exception  {err}")
else:
    print("good there is no exception")
print("ok i have handled the exception")