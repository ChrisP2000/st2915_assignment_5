#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''''
#Created on Mon Oct 23 11:32:12 2023

#@author: christopherpang
'''

def is_divisible_by_k(x,k):
    '''
    checks wheather x is divisible by k
    '''
    assert x%k ==0
    
    '''
    store all the integers that are multiples of 2 or 5 or 7
    that are lower or equal to 1000 (excluding doubles)
    '''
    
x=()
for i in range(1000):
    if is_divisible_by_k(i,2) | is_divisible_by_k(i,5) | is_divisible_by_k(i,7):
        
         x.append(i)
    
    
    '''
    Sum all the inetgers hat are multiples of 2 or 5 or 7 that 
    are lower or equal to 1000 (exlcuding doubles )
    '''
    
sum(x)