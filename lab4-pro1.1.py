# The following code provides a way to create the bar graph of a
# uniform probability distribution in the interval [a,b)
# where a=1, b=4.
# The code generates n=10000 values of the random variable.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# Generate the values of the RV X
a=1; b=4; n=10000;
x=np.random.uniform(a,b,n)
# Create bins and histogram
nbins=30; # Number of bins
edgecolor='w'; # Color separating bars in the bargraph
#
bins=[float(x) for x in np.linspace(a, b,nbins+1)]
h1, bin_edges = np.histogram(x,bins,density=True)
# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] # Width of bars in the bargraph
plt.close('all')

# PLOT THE BAR GRAPH
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

#PLOT THE UNIFORM PDF
def UnifPDF(a,b,x):
    f=(1/abs(b-a))*np.ones(np.size(x))
    return f
f=UnifPDF(a,b,b1)
plt.plot(b1,f,'r')
plt.title('PDF of uniform random variable X')
plt.xlabel('X')
plt.ylabel('PDF')
plt.show()

#CALCULATE THE MEAN AND STANDARD DEVIATION
mu_x=np.mean(x)
sig_x=np.std(x)
print('mu_x = ', mu_x)
print('sig_x = ',sig_x)