import matplotlib.pyplot as plt
import numpy as np

Vout = np.array([499.38, 500, 482.78, 384.81, 138.91, 22.2, 24.74])
F = np.array([0.100, 0.200, 0.500, 1, 2, 5, 10])

plt.xlabel("Vce")
plt.ylabel("Ice")
plt.title("Vout vs F")
##plt.scatter(10.3, 2.59)
plt.plot(Vout, F)
plt.show()