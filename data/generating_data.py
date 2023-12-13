# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:42:11 2023

@author: Claire
"""

import numpy as np
import random 

import matplotlib.pyplot as plt

x = np.linspace(1, 10, 500)

noise = np.random.normal(np.exp(x), 3 * np.exp(x) , len(x))

rand_array = np.random.rand(len(x))

rand1 = 0.01 * np.random.randint(-50, 50, size = len(x))



rand_array_new = rand_array *(1 + rand1)


print(rand1)

for i in range(len(noise)):
    if abs(noise[i]) >   x[i]:
        noise[i] /= x[i]
    if np.exp(x[i]) + noise[i] < 0.1:
        noise[i] += 10
    if (np.exp(x[i]) + noise[i])/np.exp(x[i]) > 0.2:   
        noise[i] /= 5


y = np.exp(x) * (1 + rand1)

# y = np.exp(x) + noise
    
plt.semilogy(x, y)

data = np.column_stack([x, y])

np.savetxt('data_with_noise.txt', data, fmt = ['%f', '%f'])
