import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)

t1 = n * np.log(n)
t2 = n * np.log(n)
t3 = n**2

plt.grid()
plt.ylabel('T(N)')
plt.xlabel('N')
plt.title('Quick sort time complexity')

plt.plot(n, t1, label="Best case ")
plt.plot(n, t2, label="Average case")
plt.plot(n, t3, label="Worst case")

plt.legend()
plt.show()