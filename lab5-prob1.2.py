import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

N = 1500000
u = 55
sigma = 5
n = 200

sample = np.ones([n,1])
X_bar = np.zeros([n,1])
S = np.zeros([n,1])
B = np.random.normal(u,sigma,N)
for k in range(0,n):
    X = B[random.sample(range(N),k+1)]
    X_bar[k] = np.mean(X)
    S[k] = np.std(X,ddof = 1)
    sample[k] = k+1


#PLOT THE CURVES DEFINING THE 95% CONFIDENCE INTERVAL
def ConInterval(u,sigma,n):
    f = u + 2.58*sigma/(np.sqrt(n))
    return f
f = ConInterval(u,sigma,sample)
g = ConInterval(u,-sigma,sample)

# Plotting
plt.plot(sample,X_bar, 'bx')
plt.axhline(u, color='k')
plt.plot(sample,f, 'g--')
plt.plot(sample,g, 'g--')

# Graph labels
plt.title('Sample Means and 99% confidence interval')
plt.xlabel('Sample size')
plt.ylabel('x_bar')
plt.show()
