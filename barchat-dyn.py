import matplotlib.pyplot as plt

n=int(input("Enter the number of Bars: "))

x=[]

for i in range(n):
    label= input(f"Enter the label for x axis at : {i+1}:: \t")
    x.append(label)

y=[]
for i in range(n):
    label=input(f"Enter the label for y axis at {i+1}::\t")
    y.append(label)

plt.bar(x,y,color="red3")

plt.xlabel("X-values")
plt.ylabel("y-values")

plt.show()