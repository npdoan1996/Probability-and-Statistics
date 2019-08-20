import numpy.random as ran
import numpy as np
import matplotlib.pyplot as plt

def nSidedDie(p):
    n = len(p)
    cs = np.cumsum(p)
    cp = np.append(0,cs)
    r = ran.rand()
    for k in range(0,n):
       if r>cp[k] and r<=cp[k+1]:
           d = k+1
    return d

def successesInnRolls(n):
    m = np.zeros((n,3))
    for k in range(0,n):
        for j in range(0,3):
            m[k,j] = nSidedDie(P);
    success = 0
    for k in range(0,n):
        if m[k,0] == 1 and m[k,1] == 2 and m[k,2] == 3:
            success += 1
    return success


n = 1000
N = 10000
P = [0.2,  0.1,  0.15, 0.3, 0.2, 0.05]

preferred = np.zeros((N,1))
for i in range(0,N):
    preferred[i] = successesInnRolls(n);

# Plotting
b = range(0,20+2)
sb = len(b)
h1, bin_edges=np.histogram(preferred, bins=b)
b1=bin_edges[0:sb-1]
prob=h1/N
plt.stem(b1,prob)
# Graph labels
plt.title('Bernoulli Trials: PMF - Experimental Results')
plt.xlabel('Number of successes in n=1000 trials')
plt.ylabel('Probability')
plt.xticks(b1)
plt.show()
