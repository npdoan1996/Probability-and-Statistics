import numpy.random as ran
import numpy as np

def tossacoin(n):
    success = 0
    coin=ran.randint(0,2,n)
    heads=sum(coin)
    tails=n-heads
    if heads == 50:
        success=1
    return success

N = 100000
s=np.zeros((N,1))
for j in range(0,N):
    s[j] = tossacoin(100)

numofsuccesses=np.sum(s)
print('Probability of 50 heads in tossing 100 fair coins:', numofsuccesses/N)

