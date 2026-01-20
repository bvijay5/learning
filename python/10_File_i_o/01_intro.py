# We have to open a file before reading or writing

# f = open("File_name", "mode")

# mode -> r / w

# data = f.read()
# f.close()


# Character       Meaning
# 'r'             open for reading (default)
# 'w'             open for writing, truncating the file first (overwrites the previous data)
# 'x'             create a new file and open it for writing
# 'a'             open for writing, appending to the end of the file if it exists
# 'b'             binary mode
# 't'             text mode (default)
# '+'             open a disk file for updating (reading and writing)

# 'r+'            open for both reading and writing (file must already exist)
# 'w+'            open for reading and writing, but first truncates the file (clears old data)
# 'a+'            open for reading and appending (creates file if it doesn’t exist, writes at end)
