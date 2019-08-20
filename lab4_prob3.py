# The code simulates the lifetime of a carton of 24 batteries
# Each battery's lifetime is a exponential random variable
#
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# Generate the values of the RV X
N=10000; nbatteries=24; beta=40
mu_x=beta; sig_x=beta
X=np.zeros((N,1))
for k in range(0,N):
    x=np.random.exponential(beta,nbatteries)
    C=np.sum(x)
    X[k]=C

# Create bins and histogram
nbins=30; # Number of bins
edgecolor='w'; # Color separating bars in the bargraph
#
bins=[float(x) for x in np.linspace(np.amin(X), np.amax(X),nbins+1)]
h1, bin_edges = np.histogram(X,bins,density=True)
# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] # Width of bars in the bargraph
plt.close('all')
# PLOT THE BAR GRAPH
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

#PLOT THE GAUSSIAN FUNCTION
def gaussian(mu,sig,z):
    f=np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
    return f
f=gaussian(mu_x*nbatteries,sig_x*np.sqrt(nbatteries),b1)
plt.plot(b1,f,'r')
plt.title('PDF of lifetime of a carton cotaining {} batteries'.format(nbatteries))
plt.xlabel('Lifetime for n = {} batteries'.format(nbatteries))
plt.ylabel('PDF')
plt.show()

#CALCULATE THE MEAN AND STANDARD DEVIATION
mu_C=np.mean(X)
sig_C=np.std(X)
print('mu_C = ', mu_C)
print('sig_C = ',sig_C)