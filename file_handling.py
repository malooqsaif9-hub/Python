# file handling 
# file = open('tut1.py','r')
# print(file.read())

# lets create file 
#file = open('python.txt','w')
# file.write("This is the  file i created while studying file handling.")
# file.write("This file is created using open function and in w mode in this mode we can write in the file and overrites the existing content")

 # now we open file in append mode now we add the content in the existing .
 # the previous mode 'w' we studied we create a new file and write in it or if there is content in that file then the new content we write using w mode overrites it.while
file=open('python.txt','a')
file.write("\nnow i am appending some content in the python file ")
file = open('python.txt','r')
print(file.read())
file.close()