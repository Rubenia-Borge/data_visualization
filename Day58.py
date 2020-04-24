# -*- coding: utf-8 -*-




import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd



fname = cbook.get_sample_data('msft.csv', asfileobj=False)
with cbook.get_sample_data('msft.csv') as file:
    msft = pd.read_csv(file)


pd.plotting.register_matplotlib_converters()

with cbook.get_sample_data('msft.csv') as file:
    msft = pd.read_csv(file, parse_dates=['Date'])



# Deprecated:
plt.plotfile(fname, (0, 5, 6))

# Use instead:
msft.plot(0, [5, 6], subplots=True)



# Deprecated:
plt.plotfile(fname, ('date', 'volume', 'adj_close'))

# Use instead:
msft.plot("Date", ["Volume", "Adj. Close*"], subplots=True)



# Deprecated:
plt.plotfile(fname, ('date', 'volume', 'adj_close'),
             plotfuncs={'volume': 'semilogy'})

# Use instead:
fig, axs = plt.subplots(2, sharex=True)
msft.plot("Date", "Volume", ax=axs[0], logy=True)
msft.plot("Date", "Adj. Close*", ax=axs[1])



# Deprecated:
plt.plotfile(fname, (0, 5, 6), plotfuncs={5: 'semilogy'})

# Use instead:
fig, axs = plt.subplots(2, sharex=True)
msft.plot(0, 5, ax=axs[0], logy=True)
msft.plot(0, 6, ax=axs[1])



# Deprecated:
plt.plotfile(fname, ('date', 'open', 'high', 'low', 'close'), subplots=False)

# Use instead:
msft.plot("Date", ["Open", "High", "Low", "Close"])



# Deprecated:
plt.plotfile(fname, (0, 5, 6), plotfuncs={5: "bar"})

# Use instead:
fig, axs = plt.subplots(2, sharex=True)
axs[0].bar(msft.iloc[:, 0], msft.iloc[:, 5])
axs[1].plot(msft.iloc[:, 0], msft.iloc[:, 6])
fig.autofmt_xdate()



fname2 = cbook.get_sample_data('data_x_x2_x3.csv', asfileobj=False)
with cbook.get_sample_data('data_x_x2_x3.csv') as file:
    array = np.loadtxt(file)



# Deprecated:
plt.plotfile(fname2, cols=(0, 1, 2), delimiter=' ',
             names=['$x$', '$f(x)=x^2$', '$f(x)=x^3$'])

# Use instead:
fig, axs = plt.subplots(2, sharex=True)
axs[0].plot(array[:, 0], array[:, 1])
axs[0].set(ylabel='$f(x)=x^2$')
axs[1].plot(array[:, 0], array[:, 2])
axs[1].set(xlabel='$x$', ylabel='$f(x)=x^3$')



# For simplicity of the example we reuse the same file.
# In general they will be different.
fname3 = fname2

# Depreacted:
plt.plotfile(fname2, cols=(0, 1), delimiter=' ')
plt.plotfile(fname3, cols=(0, 2), delimiter=' ',
             newfig=False)  # use current figure
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x) = x^2, x^3$')

# Use instead:
fig, ax = plt.subplots()
ax.plot(array[:, 0], array[:, 1])
ax.plot(array[:, 0], array[:, 2])
ax.set(xlabel='$x$', ylabel='$f(x)=x^3$')

plt.show()