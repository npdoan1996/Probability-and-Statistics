import matplotlib.pyplot as plt
import numpy as np
import numpy.random as ran

def roll2dice():
    d1=ran.randint(1,7)
    d2=ran.randint(1,7)
    sum=d1+d2
    return sum

def rollscount():
    rolls = 1
    while (roll2dice() !=  7):
        rolls += 1
    return rolls

N = 100000
s = np.zeros((N,1))
for j in range(0,N):
    s[j] = rollscount();

b=range(1,40)
sb=len(b)
h1, bin_edges = np.histogram(s, bins=b)
b1=bin_edges[0:sb-1]
prob=h1/N
plt.stem(b1,prob)
plt.title('PMF for numbers of rolls needed to get 7')
plt.xlabel('Numbers of successes')
plt.ylabel('Probability')
plt.show()