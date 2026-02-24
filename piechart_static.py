import matplotlib.pyplot as plt
labels = ['SUZUKI', 'TATA', 'MAHINDRA', 'TOYOTA']
marketShare = [30, 25, 20, 25]
plt.figure(figsize=(6,6))
plt.pie(marketShare, labels=labels, autopct='%1.1f%%', startangle=90)

plt.axis('equal')

plt.title('Car Market Share')
plt.show()
