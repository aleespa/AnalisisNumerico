import matplotlib.pylab as plt
import numpy as np
from math import log
def re(x):
    if x== 0:
        return 0
    else:
        return round(x/(10**int(log(abs(x),10)+1)),3)*10**int(log(abs(x),10)+1)
f  = lambda x: x**2-2*x+1
f1 = lambda x: re(re(re(x)*re(x)-2*re(x))+1)
f2 = lambda x: re(re(x)*(re(x)-2) +1)
f3 = lambda x: re(re(x-1)**2)
X = np.linspace(0.96,1.04,200)
Y  = [f(x) for x in X]
Y1 = [f1(x) for x in X]
Y2 = [f2(x) for x in X]
Y3 = [f3(x) for x in X]
p = plt.figure(figsize=(8,5))
p = plt.plot(X,Y,color='red',label='Valor Real',alpha=0.7)
p = plt.scatter(X,Y1,s=1.5,label='Metodo 1')
p = plt.scatter(X,Y2,s=1.5,color='orange',label='Metodo 2')
p = plt.scatter(X,Y3,s=1.5,color='green',label='Metodo 3')
p = plt.title('Valor flotante de $x^2-2x+1$')
p = plt.legend()
p = plt.show()