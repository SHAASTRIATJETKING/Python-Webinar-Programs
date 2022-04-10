myfirstfile = open("Myfirsttextfile.xlsx", "w")

print("What is the file name that I am created?", myfirstfile.name)
print("In Which Mode the file is created?", myfirstfile.mode)
print("Can I write content in the file?", myfirstfile.writable())
print("Can I read content in the file?", myfirstfile.readable())
print("Did I closed my file or not?", myfirstfile.closed)

myfirstfile.write(
    "This is the content I am writing for Explaining how to Open a file in Python\n")
myfirstfile.write(
    "Thank You, Now My Students able to open files at their home after listening this class\n")

print("Writing Data into the file is completed!!!!!")

myfirstfile.close()

print("Did I closed my file or not?", myfirstfile.closed)
