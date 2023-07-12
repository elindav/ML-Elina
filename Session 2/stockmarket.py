import matplotlib.pyplot as plt

dates = ["01","02","03","04","05","06","07","08","09","10","11","12"]
price = [45.67, 46.12, 45.89, 45.55, 44.92, 45.28, 44.76, 45.13, 45.21, 45.49, 45.75, 46.02]

plt.plot(dates,price, marker = 'o', linestyle = '--', color = 'green')
plt.xlabel('Date (in 2022 January)')
plt.ylabel('Closing Price($)')
plt.title("Stock Market Analysis")
for i in len(price):
	dif = price[i]
	print(price[i])
plt.show()



