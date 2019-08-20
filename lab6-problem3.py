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
           d = k
    return d

P = np.array([[1,0,0,0,0],[0.3,0,0.7,0,0],[0,0.5,0,0.5,0],[0,0,0.6,0,0.4],[0,0,0,0,1]])
n = 15
D = np.zeros([n,1])

D[0] = 2
for k in range(0,n-1):
    if D[k] == 0:
        D[k+1] = nSidedDie(P[0])
    elif D[k] == 1:
        D[k+1] = nSidedDie(P[1])
    elif D[k] == 2:
        D[k+1] = nSidedDie(P[2])
    elif D[k] == 3:
        D[k+1] = nSidedDie(P[3])
    else:
        D[k+1] = nSidedDie(P[4])

# Plotting
plt.plot(range(0, n), D, ':o', color='blue')
plt.ylim(0,4.5)

# Graph labels
plt.title('A sample simulation run of a Drunkard Walk sample')
plt.xlabel('Step number')
plt.ylabel('Page')
plt.show()