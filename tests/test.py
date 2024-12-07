"""Module providing a function printing python version."""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)
x = np.cos(t)

plt.figure()
plt.plot(t,x)
plt.show()
