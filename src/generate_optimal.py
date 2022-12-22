# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:29:22 2021

@author: xujingxu
"""
import numpy as np
d=20
B=np.random.uniform(0.05,0.2,(d,d))
for i in range(d):
    B[i][i]=1
print(B)
mu=np.random.uniform(0.6,0.8,d)
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
print(np.matmul(V_inverse,a))
print(np.array([0.1225206,  0.05452594, 0.01628473, 0.10638712, 0.07991563, 0.11723473,
 0.15481239, 0.04868666, 0.04770507, 0.03623724])/np.sum(np.array([0.1225206,  0.05452594, 0.01628473, 0.10638712, 0.07991563, 0.11723473,
 0.15481239, 0.04868666, 0.04770507, 0.03623724])))