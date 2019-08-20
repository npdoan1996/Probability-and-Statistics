import numpy as np
import matplotlib.pyplot as plt
import numpy.random as ran

def nSidedDie(p):
    n = len(p)
    cs = np.cumsum(p)
    cp = np.append(0,cs)
    r = ran.rand()
    for k in range(0,n):
       if r>cp[k] and r<=cp[k+1]:
           d = k+1
    return d


P = np.array([[1/2,1/4,1/4],[1/4,1/8,5/8],[1/3,2/3,0]])
initial_P = np.array([1/4,0,3/4])
n = 15
N = 10000
s = np.zeros([n,1])
T = np.zeros([N,n])
PA = np.zeros([n,1])
PB = np.zeros([n,1])
PC = np.zeros([n,1])

for j in range(0,N):
    s[0] = nSidedDie(initial_P)
    T[j,0] = s[0]
    for k in range(0,n-1):
        if s[k] == 1:
            s[k+1] = nSidedDie(P[0])
        elif s[k] == 2:
            s[k+1] = nSidedDie(P[1])
        else:
            s[k+1] = nSidedDie(P[2])
        T[j,k+1] = s[k+1]

for j in range(0,N):
    for k in range(0,n):
        if T[j,k] == 1:
            PA[k]+=1
        elif T[j,k] == 2:
            PB[k]+=1
        else:
            PC[k]+=1

PA = PA/N
PB = PB/N
PC = PC/N
# Plotting
line1, = plt.plot(range(0, n), PA, ':o', color='blue', label='R')
line2, = plt.plot(range(0, n), PB, ':o', color='orange', label='N')
line3, = plt.plot(range(0, n), PC, ':o', color='green', label='S')
plt.legend(handles=[line1, line2, line3], loc=4)
# Graph labels
plt.title('Simulated three-state Markov Chain')
plt.xlabel('Step number')
plt.ylabel('State')
plt.show()
