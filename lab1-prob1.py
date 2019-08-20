import matplotlib.pyplot as plt
import numpy.random as ran
import numpy as np

def nSidedDie(p):
    n = len(p)
    cs = np.cumsum(p)
    cp = np.append(0,cs)
    r = ran.rand()
    for k in range(0,n):
       if r>cp[k] and r<=cp[k+1]:
           d = k+1
    return d

N = 10000
p=[0.10,  0.15,  0.20,  0.05,  0.30, 0.10, 0.10]
n=len(p)
s = np.zeros((N,1))
for j in range(0,N):
    s[j] = nSidedDie(p)

# Plotting
b  = range(1, n+2)
sb = len(b)
h1, bin_edges=np.histogram(s, bins=b)
b1=bin_edges[0:sb-1]
prob=h1/N
plt.stem(b1,prob)
# Graph labels
plt.title('PMF for an unfair {}-sided die'.format(n))
plt.xlabel('Number on the face of the die')
plt.ylabel('Probability')
plt.xticks(b1)
plt.show()