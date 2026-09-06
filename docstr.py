def square(n):
   # print(n) now this is not a docstring 
    ''' takes in a number n and returns the square of n'''
    return(n**2)

print(square(4))
print(square.__doc__)
    
# comments are the description that helps the programmer better understand the intent and functionality of the program . they are completelt ignored by the interpreter
# docstrings are the strings used right after the  definition of the function , class , method 


#PEP-8 
# FOCUS - to make a program consistent ,maintainable , readable 
