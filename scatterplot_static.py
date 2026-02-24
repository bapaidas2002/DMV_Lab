import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.figure(figsize=(6,4))
plt.scatter(x, y)

plt.title("Basic Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")


plt.show()
