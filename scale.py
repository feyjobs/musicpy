#!/usr/bin/python
import random
import time

CHORD=['C','#C','D','#D','E','F','#F','G','#G','A','#A','B']
INDEX=[0, 2, 4, 5, 7, 9, 11]
LEVEL=[1, 2, 3, 4, 5, 6, 7]

cur=CHORD[0:len(CHORD)]
while True:
    index = random.choice(INDEX)                                                                 
    print(CHORD[index])                                                                         
                                                                                                
    seq = random.sample(LEVEL, 5)                                                               
    print seq                                                                                   
    time.sleep(2)                                                                               
                                                                                                
    cur=CHORD[index:len(CHORD)]                                                                 
    cur = cur +  CHORD[0:index]                                                                 
                                                                                                
    list=[]                                                                                     
    for key in seq:                                                                             
        list.append(cur[INDEX[key-1]])                                                          
                                                                                                
    print list                                                                                  
    print                                                                                       
    print
