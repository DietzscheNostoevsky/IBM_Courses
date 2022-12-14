# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)
z = np.cos(x)

# %matplotlib inline
plt.plot(x, y)
plt.plot(x, z)

# %%
