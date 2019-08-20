import numpy.random as ran
import numpy as np

def passwordtrials(m):
    mypassword = ran.randint(0,26**4)
    hackerlist = ran.randint(0,26**4, m)
    for k in range(0,m):
        if hackerlist[k] == mypassword:
            return 1
    return 0

N = 1000
m = 80000
k = 1
s = np.zeros([N,1])
for j in range(0,N):
    s[j] = passwordtrials(m*k)
numofsuccesses = np.sum(s)
print('Probability that at least one of the words matches the password', numofsuccesses/N)