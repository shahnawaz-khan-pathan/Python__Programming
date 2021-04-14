fileopen=open("file.txt","w")
L=["my name is sahib \n","i am from rajasthan \n","city Bhilwara \n"]
fileopen.write("Hello \n")
fileopen.writelines(L)
fileopen.close()

fileopen=open("file.txt","r+")
print("output of read " )
print(fileopen.read())
print()