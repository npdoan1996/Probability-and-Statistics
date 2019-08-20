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

def generateS():
    m = np.zeros((N, 1))
    for k in range(0,N):
        S = nSidedDie([p0,1-p0])
        S=S-1
        m[k] = S
    return m

def generateR(S):
    n = np.zeros((N, 1))
    for k in range(0,N):
        if S[k] == 0:
            R = nSidedDie([1-e0,e0])
        if S[k] == 1:
            R = nSidedDie([e1,1-e1])
        R = R-1
        n[k] = R
    return n



p0 = 0.6
e0 = 0.05
e1 = 0.03
N = 100000
preferred = np.zeros((N, 1))
S = generateS()
R = generateR(S)
for j in range(0,N):
    if (S[j] == 1) and (R[j] == 1):
        preferred[j] = 1
    else:
        preferred[j] = 0

p1 = np.sum(preferred)
p0 = np.sum(S)
prob = p1/p0
print('Probability of P(R=1|S=1) is', prob)

