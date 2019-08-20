import math
import numpy as np
import matplotlib.pyplot as plt


n = 1000
p = 0.003
q = 1 - p
lam = n*p
prob = np.zeros((21,1))
for k in range(0,21):
    prob[k] = ((lam**k)*math.exp(-lam))/math.factorial(k)

# Plotting
b = range(0,21)
plt.stem(b,prob)
# Graph labels
plt.title('Bernoulli Trials: PMF - Poisson Results')
plt.xlabel('Number of successes in n=1000 trials')
plt.ylabel('Probability')
plt.xticks(b)
plt.show()
