import matplotlib.pyplot as plt

labels = []
sizes = []

n=int(input("Enter the number of Bars: "))

for i in range(n):
    label= input(f"Enter the label for x axis at : {i+1}:: \t")
    labels.append(label)

for i in range(n):
    label=input(f"Enter the label for y axis at {i+1}::\t")
    sizes.append(label)

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title("User Input Pie Chart")
plt.axis('equal')                                                                                                                                                                                    
plt.show()
