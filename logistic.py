# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:46:39 2017

@author: user1
"""

import numpy as np
import matplotlib.pyplot as plt

def logistic_map(x0,r,n,view_plot):
  logistic_series = np.zeros(n)
  logistic_series[0] = x0
  
  for ii in np.arange(1,n):
    tmp= r*logistic_series[ii-1]*(1-logistic_series[ii-1])
    logistic_series[ii] = np.mod(tmp,1)
    
    
    
    
  if view_plot==1:
    
    plt.figure(1)
    plt.subplot(211)
    plt.plot(logistic_series)
    
    plt.subplot(212)
    plt.plot(logistic_series[1:-2],logistic_series[2:-1],'o')
    
    plt.subplot(221)
    plt.plot(logistic_series)

    plt.show()
  
  return logistic_series
  

