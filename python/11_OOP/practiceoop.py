f = open("feedback", "w")

f.write("Great product!\n")
f.write("Needs improvement in packaging\n")
f.write("Delivery was fast.\n")
f.write("Quality is excellent.\n")

f.close()


f = open("feedback", "r")


data = True
while data==True:
    data = f.readline()
    print(data)

f.close()
