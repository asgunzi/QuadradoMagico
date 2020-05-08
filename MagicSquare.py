# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:13:32 2020

@author: asgun
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import numpy as np


def quad_impar(N):
    tabuleiro = np.zeros((N,N),dtype = np.int16)

    #Adiciona o primeiro número?
    idxCol = int(((N+1)/2)-1 )
    idxLin = 0
    tabuleiro[idxLin][idxCol] = 1
    
    #Iteracoes
    for i in range(2,N**2+1):
        if idxCol+1>=N:
            idxCol2 =0
        else:
            idxCol2 = idxCol+1
    
        if idxLin - 1 < 0:
            idxLin2 = N-1
        else:
            idxLin2 = idxLin-1
        
        #Verifica se a posicao já está ocupada
        if tabuleiro[idxLin2][idxCol2]>0:        
            if idxLin+1 >= N:
                idxLin2 = 0
            else:
                idxLin2 = idxLin + 1
    
            idxCol2 = idxCol
            
            
        #Preenche tabuleiro e vai para a próxima  
        tabuleiro[idxLin2][idxCol2]=i
        
        idxLin = idxLin2
        idxCol = idxCol2
        
    return(np.transpose(tabuleiro))
        
    
    
def quad4n(N):
    #Da forma 4*n
    tabuleiro = np.zeros((N,N),dtype = np.int16)
    
    count = 0
    padrao1 = False
    
    for i in range(N):
        if i % 4 ==0 or i % 4 ==3:
            padrao1=True
        else:
            padrao1=False
            
        for j in range(N):
            count+=1
            if j % 4 == 0 or j % 4 == 3:
                if padrao1:
                    tabuleiro[i,j] = N**2 - count +1
                else:
                    tabuleiro[i,j] = count
            else:
                if padrao1:
                    tabuleiro[i,j] = count
                else:
                    tabuleiro[i,j] = N**2 - count +1

    return(np.transpose(tabuleiro))

   
def quad4n1(N):
    #Forma 4n+1
    #Método LUX
    tabuleiro = np.zeros((N,N),dtype = np.int16)
    
    m = int((N-2)/4)

    aux1 = np.zeros((2*m+1, 2*m+1), dtype = np.int16)    
    aux2 = np.zeros((2*m+1, 2*m+1), dtype = np.int16)    

    #m+1 rows of Ls,
    for i in range(m+1):
        for j in range(2*m+1):
            aux1[i,j] = 1 #"L"
      
    #1 row of U
    for j in range(2*m+1):
        aux1[m+1,j] = 0 #"U"
    
    #n-1 rows of X
    for i in range(m+2, 2 * m + 1):
        for j in range(2*m+1):
            aux1[i,j] = -1 #"X"
    
    #exchange the U in the middle with the L above it. 
    aux1[m,m]= 0 #"U"
    aux1[m+1,m]= 1 #"L"
    
    
    tam2 = 2 * m + 1
    
    #Posicao inicial, centro superior
    posX = int( (tam2 + 1) / 2 -1)
    posY = 0 
    
    for i in range(tam2 ** 2):
        aux2[posY, posX] = i+1
        
        if aux1[posY, posX] == 1: #"L"            
            tabuleiro[2 * (posY ) + 0 , 2 * (posX ) + 1] = 4 * (i) + 1
            tabuleiro[2 * (posY ) + 1 , 2 * (posX ) + 0] = 4 * (i) + 2
            tabuleiro[2 * (posY ) + 1 , 2 * (posX ) + 1] = 4 * (i) + 3
            tabuleiro[2 * (posY ) + 0 , 2 * (posX ) + 0] = 4 * (i ) + 4
            
        elif aux1[posY, posX] ==0: #"U"
            tabuleiro[2 * (posY ) + 0, 2 * (posX ) + 0] = 4 * (i) + 1
            tabuleiro[2 * (posY ) + 1, 2 * (posX ) + 0] = 4 * (i ) + 2
            tabuleiro[2 * (posY ) + 1, 2 * (posX ) + 1] = 4 * (i ) + 3
            tabuleiro[2 * (posY) + 0, 2 * (posX ) + 1] = 4 * (i ) + 4
        else:  #aux[posY, posX] == "X":
            tabuleiro[2 * (posY ) + 0, 2 * (posX ) + 0] = 4 * (i ) + 1
            tabuleiro[2 * (posY ) + 1, 2 * (posX ) + 1] = 4 * (i ) + 2
            tabuleiro[2 * (posY ) + 1, 2 * (posX ) + 0] = 4 * (i ) + 3
            tabuleiro[2 * (posY ) + 0, 2 * (posX ) + 1] = 4 * (i) + 4

        
            
        if posY ==0:
            posYtest = tam2-1
        else:
            posYtest = posY - 1
        
        if posX== tam2-1:
            posXtest = 0
        else:
            posXtest = posX + 1
        
    
        if aux2[posYtest, posXtest] == 0:
            posY = posYtest
            posX = posXtest
        else:
            posY = posY + 1
        
    
    return(np.transpose(tabuleiro))



#Defina aqui o tamanho do quadrado mágico
N = 10

if N % 2 == 1:
    quadrado = quad_impar(N)
elif N % 4 == 0:
    quadrado = quad4n(N)
else:
    quadrado = quad4n1(N)
    
print(quadrado)



#Cria os retângulos para plotar

fig, ax = plt.subplots()
#rectangles = {'skinny' : mpatch.Rectangle((2,2), 8, 2),
#              'tabuleiro' : mpatch.Rectangle((4,6), 6, 6)}
    
rectangles = {}

for i in range(N):
    for j in range(N):
        rectangles[str(quadrado[i,j])] = mpatch.Rectangle((i,N-j-1),.9,.9, color=(.1,quadrado[i,j]/N**2,.8))
    
    
for r in rectangles:
    ax.add_artist(rectangles[r])
    rx, ry = rectangles[r].get_xy()
    cx = rx + rectangles[r].get_width()/2.0
    cy = ry + rectangles[r].get_height()/2.0 

    fsize = 10 if N< 12 else 6
    
    ax.annotate(r, (cx, cy), color='w', weight='bold', 
                fontsize=fsize, ha='center', va='center')


ax.set_xlim((0, N))
ax.set_ylim((0, N))
ax.set_aspect('equal')
plt.axis('off')

plt.show()

