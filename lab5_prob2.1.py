import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

N = 1500000
M = 10000
u = 55
sigma = 5
n = 120
Z_c = 2.58
T_c = 2.62

B = np.random.normal(u,sigma,N)
N_success = np.zeros([M,1])
T_success = np.zeros([M,1])
result = np.zeros([2,1])

def Experiment(B):
    X = B[random.sample(range(N),n)]
    S_hat = 0
    X_bar = np.sum(X)/n
    for k in range(0,n):
        S_hat = S_hat + (X[k]-X_bar)**2
    S_hat = S_hat/(n-1)
    S_hat = np.sqrt(S_hat)
    # calculate the confidence interval using normal distribution
    upperN_u = X_bar + Z_c*S_hat/(np.sqrt(n))
    lowerN_u = X_bar - Z_c*S_hat/(np.sqrt(n))
    # calculate the actual sample mean and sample deviation
    u_X = np.mean(X)
    S = np.std(X,ddof = 1)
    # calculate the confidence interval using t-distribution
    upperT_u = X_bar + T_c*S_hat/np.sqrt(n)
    lowerT_u = X_bar - T_c*S_hat/np.sqrt(n)
    success = np.zeros([2,1])
    if u >= lowerN_u and u <= upperN_u:
        success[0] = 1
    else:
        success[0] = 0
    if u >= lowerT_u and u <= upperT_u:
        success[1] = 1;
    else:
        success[1] = 0;
    return success

for i in range(0,M):
    result = Experiment(B)
    N_success[i] = result[0]
    T_success[i] = result[1]

print("The success rate using the normal distribution is ", np.sum(N_success)/M)
print("The success rate using the Student's T - distribution is ", np.sum(T_success)/M)
