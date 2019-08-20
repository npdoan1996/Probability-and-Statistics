import numpy as np
import matplotlib.pyplot as plt
import numpy.random as ran

P = np.array([[1/2,1/4,1/4],[1/4,1/8,5/8],[1/3,2/3,0]])
initial_P = np.array([1/4,0,3/4])
n = 15
PA = np.zeros([n,1])
PB = np.zeros([n,1])
PC = np.zeros([n,1])

n_P = initial_P
for k in range(0,n):
    PA[k] = n_P[0]
    PB[k] = n_P[1]
    PC[k] = n_P[2]
    n_P = np.dot(n_P,P)

# Plotting
line1, = plt.plot(range(0, n), PA, ':o', color='blue', label='R')
line2, = plt.plot(range(0, n), PB, ':o', color='orange', label='N')
line3, = plt.plot(range(0, n), PC, ':o', color='green', label='S')
plt.legend(handles=[line1, line2, line3], loc=4)
# Graph labels
plt.title('Calculated three-state Markov Chain')
plt.xlabel('Step number')
plt.ylabel('State')
plt.show()