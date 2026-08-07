import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)
y = x ** 2
plt.plot(x, y, "r")
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()

plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')

plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')

plt.show()