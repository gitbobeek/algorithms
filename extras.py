import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0, 1000, 1000)

t1 = (6*n + 12*n)
t2 = (1/2)*n**2 +(17/2)*n
t3 = (1/2)*n**2 + (8/2)*n

plt.grid()
plt.ylabel('T(N)')
plt.xlabel('N')
plt.title('Insertion sort time complexity')

plt.plot(n, t1, label="Worst case")
plt.plot(n, t2, label="Best case")
plt.plot(n, t3, label="Average case")

plt.legend()
plt.show()