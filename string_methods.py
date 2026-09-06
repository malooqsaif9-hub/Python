a  = "saif malooq !!!!!!!!!!!!!! saif"
print(a)  # print original string
print(a.upper())  # convert all characters to uppercase
print(a.lower())  # convert all characters to lowercase
print(a.rstrip("!"))  # remove trailing exclamation marks from the right end
print(a.replace("saif","sonu"))  # replace all occurrences of "saif" with "sonu"
print(a.split())  # split string into a list of words separated by whitespace

# capitalize()
blog = "introduction tO liNear aLgebra"
print(blog.capitalize())  # capitalize first character and lowercase the rest of the string

# center()
str1 = "welcome to this 100 day python tutorial"
print(str1.center(100))  # center the string in a field of width 100 with padding spaces
print(len(str1))  # print the length of the string

# count()
print(str1.count("o"))  # count how many times "o" appears in the string

# endswith()
print(str1.endswith("tutorial"))  # check if string ends with the substring "tutorial"

# find()
b = "I am a good boy. I sleep early."
print(b.find("good"))  # return the index of the first occurrence of "good" or -1 if not found

# isprintable()
b = "I am a good boy. I sleep early.\n"
print(b.isprintable())  # return False if the string contains non-printable characters such as newline

# istitle()
title = "Youtube is Social Media Platform"
print(title.istitle())  # check if the string is titlecased (each word starts with uppercase followed by lowercase)
