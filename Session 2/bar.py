import matplotlib.pyplot as plt

sales = [320, 250, 430, 510]

plt.bar(products, sales, color = ['red', 'blue', 'green', 'orange'])
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()

