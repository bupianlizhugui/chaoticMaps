# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:46:39 2017

@author: bklimowski
"""




"""
Import pakietów, numpy służy do obliczeń numerycznych, dostarcza pythonowi funkcjonalnośći matlaba. Matplotlib generuje wykresy.
Do funkcji dostarczanych przez pakiet dostajemy się następująco: 
<nazwa_pakietu>.<funkcja> na przykład np.zeros(100) [generuje wektor 100 zer]

Dla formalności przypomnę, że w pythonie intendancja determinuje działanie programu.
Nie korzysta się z sredników,klamerek itp.
"""

import numpy as np
import matplotlib.pyplot as plt

"""
Funkcje definujemy:

def nazwa_funkcji(argument1,argument2):
  
  <jakieś działania na argumentach>
  
  return 4000
  
 
Poniżej jest przykład funkcji generującej odwzorowanie logisyczne, wykreśla 
również ten szereg i jego przekrój Poincare.
"""


def circle_map(x0,r,n,view_plot):
  
  #x0 - warunek początkowy  
  #r - parametr odwzorowania
  #n - długość szeregu
  #view_plot - jeżeli 1 rysuje wykresy
  
  
  #inicializacja wektora, przypisanie wartości początkowej
  circle_series = np.zeros(n)
  circle_series[0] = x0
  
  
  
  """
  Przykład pętli for
  
  for jj in <zakres>:
    print jj
    
  zakresem może być właściwie każdy typ zmiennej, str,char też.
  """
  for ii in np.arange(1,n):
    tmp= circle_series[ii-1]+a+(b/(2*np.pi))*np.sin(2*np.pi*circle_series[ii-1])
    cirlce_series[ii] = np.mod(tmp,1)
   
  
  
  
  
  
  #Narysowanie wykresów
  if view_plot==1:
    
    plt.figure(1)
    plt.subplot(311)
    plt.plot(circle_series)
    
    plt.subplot(212)
    plt.plot(circle_series[1:-2],circle_series[2:-1],'o')
  
    plt.show()
  
  return circle_series
  

