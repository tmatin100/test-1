print("hello world")
x=5
y=3
import matplotlib.pyplot as plt
import numpy as np
from numpy import random

fig, ax=plt.subplots()
x=np.linspace(0,100,100)
y=random.randint(100, size=(100))
ax.plot(x,y)