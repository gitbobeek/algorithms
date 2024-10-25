import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 10)

t1 = n * np.log(n)
t2 = n * np.log(n)
t3 = n * np.log(n)

plt.grid()
plt.ylabel('T(N)')
plt.xlabel('N')
plt.title('Heap sort time complexity')

plt.plot(n, t1, label="Best case ")
plt.plot(n, t2, label="Average case")
plt.plot(n, t3, label="Worst case")

plt.legend()
plt.show()