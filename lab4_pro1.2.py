# The following code provides a way to create the bar graph of a
# exponentially distributed  probability
# where bera = 40
# The code generates n=10000 values of the random variable.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# Generate the values of the RV X
beta = 40; n=10000;
x=np.random.exponential(beta,n)
# Create bins and histogram
nbins=30; # Number of bins
edgecolor='w'; # Color separating bars in the bargraph
#
bins=[float(x) for x in np.linspace(np.amin(x), np.amax(x),nbins+1)]
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
def ExpPDF(beta,x):
    f=(1/beta)*(np.exp(-x/beta))*np.ones(np.size(x))
    return f
f=ExpPDF(beta,b1)
plt.plot(b1,f,'r')
plt.title('PDF of exponential distributed random variable T')
plt.xlabel('T')
plt.ylabel('PDF')
plt.show()

#CALCULATE THE MEAN AND STANDARD DEVIATION
mu_x=np.mean(x)
sig_x=np.std(x)
print('mu_T = ', mu_x)
print('sig_T = ',sig_x)