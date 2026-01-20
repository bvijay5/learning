import matplotlib.pyplot as plt

'''
plt.bar(x, height, color = "enter_color", width = value, label = "enter label")
'''

product = ["a", "b", "c", "d"]
sales = [1000,1500,800,1200]

plt.bar(product , sales, color = "orange", label = "Sales")     #plt.barh(x,y) for horizontal bar graph
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Sales Trend")
plt.legend()
plt.show()

