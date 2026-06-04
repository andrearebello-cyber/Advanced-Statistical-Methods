#Plotting pdf, cdf, pmf, for discrete and continuous distribution

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
N = 100
data = np.random.randn(N)
count, bins_count = np.histogram(data, bins=10)
pdf = count / sum(count)

cdf = np.cumsum(pdf)

plt.plot(bins_count[1:], pdf, color="red", label="PDF")
plt.plot(bins_count[1:], cdf, label="CDF")
plt.legend()
plt.show()
