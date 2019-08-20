import math
import numpy as np
import matplotlib.pyplot as plt

def combination(n,k):
    C = math.factorial(n)/((math.factorial(k))*(math.factorial(n - k)))
    return C

N = 1000
p = 0.003
q = 1 - p
prob = np.zeros((21,1))
for i in range(0,21):
    prob[i] = combination(N,i)*(p**i)*(q**(N-i))

# Plotting
b = range(0,21)
plt.stem(b,prob)
# Graph labels
plt.title('Bernoulli Trials: PMF - Binomial Formula')
plt.xlabel('Number of successes in n=1000 trials')
plt.ylabel('Probability')
plt.xticks(b)
plt.show()
