import matplotlib.pyplot as plt

'''
plt.savefig("filename.extension", dpi = value, bbox_inches = "tight")
'''

x = [1,2,3,4]
y = [1000, 1500, 1200, 1800]

plt.plot(x,y, color = "blue", marker = "*", label = "Sales data", linestyle = "--", linewidth = 2)
plt.legend(loc = "upper left")
plt.grid(color = "grey", linestyle = ":", linewidth = 1)
plt.xlim(1,4)
plt.ylim(500,2000)
plt.xticks([1,2,3,4], ["m1","m2","m3","m4"])
plt.savefig("Vijaychart.png", dpi = 300, bbox_inches = "tight")
plt.show()
