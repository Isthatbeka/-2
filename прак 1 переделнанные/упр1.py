import numpy as np

x = int(input())
y = (x, np.log((np.exp(1/(np.sin(x)+1))/((5/4)+(1/5*x**1))/np.log(1+x**2))))
print(y)