import matplotlib.pyplot as plt

'''
plt.pie(values, label = [label_list], colors = [colors_list], autopct = "%1.1f%%")
'''

regions = ["North", "South", "East", "West"]
revenue = [2000,3000,1000, 1500]

plt.pie(revenue, labels = regions, autopct= "%1.1f%%")

plt.show()