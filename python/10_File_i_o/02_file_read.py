f = open("learning/python/10_File_i_o/demo.txt", "r")  # Open the file in read mode
line1 = f.readline()       # Read the contents on line 1 only(cursur will move to the end of the line)
print(line1)
data = f.read()            # Read the contents
print(data)                # Print the contents
f.close()                  # Close the file


