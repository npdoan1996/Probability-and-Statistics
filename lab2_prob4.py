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
        S = S-1
        m[k] = S
    return m

def generateR(S):
    n = np.zeros((N, 3))
    for k in range(0,N):
        for j in range(0,3):
            if S[k] == 0:
                R = nSidedDie([1-e0,e0])
            if S[k] == 1:
                R = nSidedDie([e1,1-e1])
            R = R-1
            n[k,j] = R
    return n



p0 = 0.6
e0 = 0.05
e1 = 0.03
N = 100000
preferred = np.zeros((N, 1))
S = generateS()
R = generateR(S)
D = np.zeros((N,1))
for k in range(0,N):
    if np.sum(R[k]) > 1:
        D[k] = 1
    else:
        D[k] = 0

for j in range(0,N):
    if S[j] == D[j]:
        preferred[j] = 0
    else:
        preferred[j] = 1

p1 = np.sum(preferred)
p0 = np.sum(R)
prob = p1/p0
print('Probability of error with enhanced transmission is', prob)

