# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:29:22 2021

@author: xujingxu
"""
# calculate optimal solution for portfolio selection

import numpy as np
d=20 # we can also set d=2 and d=5
B=np.random.uniform(0.05,0.2,(d,d)) # the covariance matrix is randomly generated
for i in range(d):
    B[i][i]=1
print(B)
mu=np.random.uniform(0.6,0.8,d) # the mean return is randomly generated
print(mu)
S_0=0.5
r=0.1
V= np.matmul(B,np.transpose(B))
V_S=np.zeros((d,d))
for i in range(d):
    for j in range(d):
        V_S[i][j]=(S_0**2)*(np.exp(mu[i]+mu[j]+V[i][j])-np.exp(mu[i])*np.exp(r)-np.exp(mu[j])*np.exp(r)+np.exp(2*r))
V_inverse=np.linalg.inv(V_S)
print(np.matmul(V_inverse,V_S))
a=np.zeros(d)
for i in range(d):
    a[i]=S_0*(np.exp(mu[i])-np.exp(r))*(2-S_0*np.exp(r))
a=np.transpose(a)
optvalue = np.matmul(V_inverse,a)
print(optvalue) # If all entries are in [0,1], then it is optimal; otherwise we generate another B and mu and recalculate
