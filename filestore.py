f=open ("file.txt", mode='w')
print (f.writable())
f.write("line 1\n")
f.writelines("line 2\n line 3\n line 4\n shahed hasan chowdhury\n")
f.close()

#new data add using append mode

f=open ("file.txt", mode='a')
print (f.writable())
f.write("line 5\n")
#f.writelines("line 2\n line 3\n line 4\n shahed hasan chowdhury")
f.close()

# data reading mode 
f=open ("file.txt", mode='r')
print (f.readable())
print (f.readlines())  # readlines using the list of data
print(f.read())        # read using text formate 

f.close()
'''
### Exclusive mode
f=open ("file1.txt", mode='x')
f.write("Exclusive mode\n")
#print (f.writable())
#f.write("shahed\n hello")
f.close()'''

# Read and Write

f= open("file.txt", mode='r+')
print(f.read())
f.write("Read thid line\n")
f.close()

# Read binary
f= open("file.txt", mode='rb')
print(f.read())
#f.write("Read thid line")
f.close()

#Read text form
f= open("file.txt", mode='rt')
print(f.read())
#f.write("Read thid line")
f.close()

#Every time Not using close( ) then this type code

with open("file.txt",mode='r+') as f:
    print(f.read())
    f.write("not using close()")


