# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:15:48 2021

@author: TNC TECHNOLOGIE
"""

import numpy as np 
state_number = 4
#environment_columns = 17

#Notre tableau contient 4 lignes et 17 colonnes pour pouvoir correspondre a la forme de l'environnement
#Les lignes repésentent les états et les colonnes représentent les actions
#On créé un tableau numpy 3D pour contenir les Q-vakues actuelles pour chaque paire d'état-action
#La valeur de chaque paire (etat,action) est initialisée à 0.
#La formule est la suivante:
V = np.zeros((state_number, 4))

temp = np.zeros((state_number, 4))


#definition des 17 actions différentes que l'attaquant peut exécuter
#code numérique correspondant à chaque action : 0 = A1, 1 = A2, 2 = = A3, .... 15 = A16, 16 = A17
actions = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17'] 


#Déclaration des récompenses par états de vulnérabilité
rewards = np.zeros((state_number, 4))
rewards[3] = 1
# affichage des récompenses par état devulnérabilité
print(Recompense[i])

P_Matrix = np.zeros((state_number, state_number, 16))
print (P_Matrix)
discount_factor = 0.9
tolerance = 0.01
negligeable = True



#Déclaration de la matrice des récompenses
P_Matrix = np.array([[0.222,0.333,0.444,0],[0.142,0.214,0.357,0.285],[0.142,0.214,0.357,0.285],[0.666,0,0,0.333]])

#initialisation  de V , valeur des états
V = ([0,0,0,0])


print (V)
print (P_Matrix)



for row_index in range(0, 1):
    for column_index in aisles[0]:
        rewards[row_index, column_index] = -1.
        
        # -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:15:48 2021

@author: TNC TECHNOLOGIE
"""

import numpy as np 
state_number = 4
#define the shape of the environment (it's states)
environment_rows = 4
environment_columns = 4




#Notre tableau contient 4 lignes et 17 colonnes pour pouvoir correspondre a la forme de l'environnement
#Les lignes repésentent les états et les colonnes représentent les actions
#On créé un tableau numpy 3D pour contenir les Q-vakues actuelles pour chaque paire d'état-action
#La valeur de chaque paire (etat,action) est initialisée à 0.
#La formule est la suivante:
V = np.zeros((state_number, 4))

temp = np.zeros((state_number, 4))

P_Matrix = np.zeros((environment_rows, environment_columns, 4))
#definition des 17 actions différentes que l'attaquant peut exécuter
#code numérique correspondant à chaque action : 0 = A1, 1 = A2, 2 = = A3, .... 15 = A16, 16 = A17
actions = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17'] 


#Déclaration des récompenses par états de vulnérabilité
#rewards = np.zeros((state_number, 4))
#rewards[3] = 1
#print(rewards)
R = np.array([0,0,0,1])
print('on fixe les récompenses par état:')
print('R1 = 0, R2 = 0, R3 = 0 et R4 = 1')
print('ce qui nous donne le vecteur ci-dessous')
print (R)
# affichage des récompenses par état devulnérabilité


#P_Matrix = np.zeros((state_number, state_number, 4))
#print (P_Matrix)
discount_factor = 0.9
tolerance = 0.00001
iteration = 3


i = 0
j = 0
k = 0


negligeable = True

def myFunction() :
  return True

#Déclaration de la matrice des récompenses
P_Matrix = np.array([[0.222,0.333,0.444,0.000],[0.142,0.214,0.357,0.285],[0.142,0.214,0.357,0.285],[0.666,0.000,0.000,0.333]])
print('La matrice des probabilités est la suivante :')
print (P_Matrix)



#On déclare V , valeur des états comme vecteur de coonnes et initialisation  de V à zéros 
print ('V est la valeur des états')
print ('Valeurs de V initialisées à zéro')

V = np.array([[0],
              [0],
              [0],
              [0]])

#print (V)
temp = np.zeros(4)
Vp = np.zeros(4)
#print(temp)






#New_V = np.zeros((environment_columns, 4))

  

while k < iteration:
    i=0
    print('========Itération========')
    print(k)
    while i < 4 :
        j=0
        while j < 4:
           print(V[j])
           print(P_Matrix[i, j])
           temp[j] = P_Matrix[i, j]* V[j]
           j=j+1
        print('Voici la valeur de temp')  
        print(temp)
        Vp[i]=R[i]+ (discount_factor*max(temp))
        print(max(temp))
        print(discount_factor*max(temp))
        print(R[i])
        print(Vp)
        # if abs(V[i]-V[(i+1)%4]) <= tolerance :
        # print(True)
        #negligeable = False
                   
        i=i+1
    V=Vp
    k = k+1   
    print(k) 
    print(V) 
        

        
        
        
        
        
        
        
        
    
        
        
        #f = max(temp)
        #print(f)
                             
                    
        #New_V = R+(discount_factor*f)
        #V = New_V
       # print(V)
          #column_index = column_index + 1
                   
         
#if abs((v(i+1)-v(i)) < tolerance
       #tolerance = False
       
       




        
        

        
        












        

        
        
#Affiche le vecteur des récompenses
for row in rewards: 
    print (row)     

#Affiche la matrice des probabilités

    print (P_Matrix[i, j])    








while negligeable:
    {
     
     for j in range(0, 3):
         {      
                 for i in range(0, 3):
                     {
                             temp(i)=(P_Matrix[j, i])*V(i)
                             f = max(temp(i))
                     }
                     New_V(i) = (R(i) + discount_factor*f)
                             V(i) = New_V(i)
          j = j+1
                   
         }
     if abs((v(i+1)-v(i)) < tolerance
            tolerance = False
     }
    