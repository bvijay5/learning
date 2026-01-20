import matplotlib.pyplot as plt

'''
plt.plot(x,y, color = "Color_name", linestyle = "line_style", 
linewidth = value, marker = "marker_symbol", label = "label_name")
'''

x = [1,2,3,4]
y = [1000, 1500, 1200, 1800]

plt.plot(x,y, color = "blue", marker = "*", label = "Sales data", linestyle = "--", linewidth = 2)

# legend
plt.legend(loc = "upper left")

# grid
plt.grid(color = "grey", linestyle = ":", linewidth = 1)

# Axis limits
plt.xlim(1,4)
plt.ylim(500,2000)

# axis ticks
plt.xticks([1,2,3,4], ["m1","m2","m3","m4"])

# Display
plt.show()