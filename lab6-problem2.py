import numpy as np
import matplotlib.pyplot as plt

P = np.array([[0,1,0,0,0],[1/2,0,1/2,0,0],[1/3,1/3,0,0,1/3],[1,0,0,0,0],[0,1/3,1/3,1/3,0]])
v1 = np.array([1/5,1/5,1/5,1/5,1/5])
n = 20
PA = np.zeros([n,1])
PB = np.zeros([n,1])
PC = np.zeros([n,1])
PD = np.zeros([n,1])
PE = np.zeros([n,1])


v_n = v1
for k in range(0,n):
    PA[k] = v_n[0]
    PB[k] = v_n[1]
    PC[k] = v_n[2]
    PD[k] = v_n[3]
    PE[k] = v_n[4]
    print(v_n)
    v_n = np.dot(v_n,P)

# Plotting
line1, = plt.plot(range(0, n), PA, ':o', color='blue', label='pageA')
line2, = plt.plot(range(0, n), PB, ':o', color='orange', label='pageB')
line3, = plt.plot(range(0, n), PC, ':o', color='green', label='pageC')
line4, = plt.plot(range(0, n), PD, ':o', color='red', label='pageD')
line5, = plt.plot(range(0, n), PE, ':o', color='yellow', label='pageE')
plt.legend(handles=[line1, line2, line3,line4,line5], loc=4)
# Graph labels
plt.title('A sample simulation run of the Google Page Rank Algorithm')
plt.xlabel('Step number')
plt.ylabel('Page')
plt.show()