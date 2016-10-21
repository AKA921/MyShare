import random
import numpy as np
import pygame,sys
import matplotlib.pyplot as plt 
from pygame.locals import *

def init_array(n):
    vector=np.random.random_integers(0,1,(n,n))
    vector[0,:]=0
    
    vector[:,0]=0
    vector[n-1,:]=0
    vector[:,n-1]=0
    return vector

def zeros_array(n):
    vector=np.random.random_integers(0,0,(n,n))
    return vector

def count(vector,row,col):
    num=0
    if (vector[row-1][col-1]==1):
        num+=1
    if (vector[row-1][col]==1): 
        num+=1
    if (vector[row-1][col+1]==1):
        num+=1  
    if (vector[row][col+1]==1):
        num+=1    
    if (vector[row+1][col+1]==1):
        num+=1 
    if (vector[row+1][col]==1):
        num+=1
    if (vector[row+1][col-1]==1):
        num+=1 
    if (vector[row][col-1]==1):
        num+=1
    return num
         
def change_array(vector1,vector2,n):
    for i in range(1,n-1): 
        for j in range(1,n-1):
            num=count(vector1,i,j)
            if(num==3):
                vector2[i][j]=1
            elif(num==2):
                vector2[i][j]=vector1[i][j]
            else:
                vector2[i][j]=0

def plot_array(vector,n):
    pygame.init()
    screen = pygame.display.set_mode((610, 600), 0, 32) 
    pygame.display.set_caption('Life Demo')
    for i in range(n):
        for j in range(n):
            if (vector[i][j]==1):
                sysFont=pygame.font.SysFont('None',19)
                rendered=sysFont.render('@',0,(255,0,0))
                screen.blit(rendered,(i*10,j*10))  
                for event in pygame.event.get():
                    if event.type== QUIT:
                        pygame.quit()
                        sys.exit()
    pygame.display.update()        
                        
def main():
    while(1):
        n=60
        vector1=init_array(n)
        vector2=init_array(n)
        change_array(vector1, vector2,n)
        plot_array(vector2, n)     
        vector1=vector2
        

main()


    

            

