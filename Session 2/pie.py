import matplotlib.pyplot as plt

categories = ['Category A','Category B', 'Category C', 'Category D', 'Category E']
percentages = [25, 30, 15, 15, 15]

explode = [1, 1, 1, 1, 1]
colors = ['red', 'blue', 'orange', 'green', 'purple']

plt.pie(percentages, explode = explode, labels = categories,colors = colors,shadow = True)
plt.title("Percentage Destribution")
plt.legend(categories)
plt.show()

