# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 04:11:45 2021

@author: TNC TECHNOLOGIE
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 09:17:10 2021

@author: TNC TECHNOLOGIE
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:00:42 2021

@author: TNC TECHNOLOGIE
"""

"""
Created on Wed Mar  3 17:50:27 2021

@author: ALIMA-PC
"""


#importation des librairies
import numpy as np 

#import matplotlib.pyplot as plt


#define the shape of the environment (it's states)
environment_rows = 4
environment_columns = 4

#Notre tableau contient 4 lignes et 17 colonnes pour pouvoir correspondre a la forme de l'environnement
#Les lignes repésentent les états et les colonnes représentent les actions
#On créé un tableau numpy 3D pour contenir les Q-vakues actuelles pour chaque paire d'état-action
#La valeur de chaque paire (etat,action) est initialisée à 0.
#La formule est la suivante:
q_values = np.zeros((environment_rows, environment_columns, 4))


#definition des 17 actions différentes que l'attaquant peut exécuter
#code numérique correspondant à chaque action : 0 = up, 1 = down, 2 = = left, 3 = rigth
actions = ['Up', 'Right','Down', 'Left'] 


#On créé un tableau numpy 2D qui contient les récompense pour chaque état-action
#Le tableau contient 4 lignes et 17 colonnes (qui correspondent à notre envir), 
#et chaque valeur de récompense est initialisée à -5 qui marque la pénalité
rewards = np.full((environment_rows, environment_columns), -10.)
rewards[2, 2] = 10.


#definir les emplacements des éllées pour les lignes 0 à 3
# On construit un dictionnaire qui va définir les valeurs qui correspondent à l'automate des états
aisles = {} #store location in the dictionary
aisles[1] = [i for i in range(1, 3)]
aisles[2] = [1]
#aisles[2] = [1]
#aisles[3] = [1, 2] 


#Définition des récompenses pour tous les emplacements se trouvaant dans l'intervalle 1 et 2.


for row_index in range(1, 3):
    for column_index in aisles[row_index]:
        rewards[row_index, column_index] = -1.



        
        

        
        
#Affiche la matrice des récompenses
for row in rewards: 
    print (row)        
    
    #print('Training terminé!')
    
    
    
       
# Fonction qui déttermine si le prochain état est un état terminal
def is_terminal_state(current_row_index, current_column_index):
    #Si la récompense pour cette état est 0 alors il ne s'agit pas de l'état terminal
    if rewards[current_row_index, current_column_index] == -1.:
        return False
    else:
        return True
    

#Fonction qui va choisir de manière aléatoire un état initial
def get_starting_location():
    #Choisir de manière aléatoire un index de ligne et colonne
    current_row_index = np.random.randint(environment_rows)
    current_column_index = np.random.randint(environment_columns)
    
    #on continue de choisir des index de ligne et colonne jusqu'a ce qu'on etteigne l'étt final
    while is_terminal_state(current_row_index, current_column_index):
        current_row_index = np.random.randint(environment_rows)
        current_column_index = np.random.randint(environment_columns)
    return current_row_index, current_column_index    


#Fonction qui implémente le epsilon greedy qui va choisir de manière aléatoire l'action qui sera exécutée parmi toutes les actions possibles 
def get_next_action(current_row_index, current_column_index, epsilon):
    #si la valeur choisie de mmanière aléatoire entre 0 et 1 est inférieure à epsilon,
    #alors on choisit la plus grande valeur de la Q-table qui correspond à cet état
    if np.random.random() < epsilon:
        return np.argmax(q_values[current_row_index, current_column_index])
    else: #choisir une action aléatoire
        return np.random.randint(4)
    
    

#Fonction qui choisit l'état suivant à partir de l'action effectuée par l'attaquant
def get_next_location(current_row_index, current_column_index, action_index):
    new_row_index = current_row_index
    new_column_index = current_column_index
    if actions[action_index] == 'Up' and current_row_index > 0 :
        new_row_index -= 1
    elif actions[action_index] == 'Right' and current_column_index < environment_columns -1:
         new_row_index += 1
    elif actions[action_index] == 'Down' and current_row_index < environment_rows -1:
       
        new_column_index += 1
    
    elif actions[action_index] == 'Left' and current_column_index > 0 :
        new_column_index -= 1
    return new_row_index, new_column_index




#fonction qui dfinit le plus court chemin que l'attaquant doit prendre pour arnaquer sa victime
def get_shortest_path(start_row_index, start_column_index):
    #renvoie s'il s'agit d'un etat initial invalide
    if is_terminal_state(start_row_index, start_column_index):
        return []
    else:
        current_row_index, current_column_index = start_row_index, start_column_index
        shortest_path = []
        shortest_path.append([current_row_index, current_column_index])
        #continuer d'évoluer état apres etat jusqu'à ce qu'on atteigne l'état final
        while not is_terminal_state(current_row_index, current_column_index):
            #renvoie la meilleure action a prendre
            action_index = get_next_action(current_row_index, current_column_index, 1.)
            #Se déplace a l'état suivant et ajoute un nouvel état à la liste
            current_row_index, current_column_index = get_next_location(current_row_index, current_column_index, action_index)
            shortest_path.append([current_row_index, current_column_index])
        return shortest_path




#On entraine l'agent qui est l'attaquant en utilisant le Q-learning

#definir les parametres de training
epsilon = 0.9 # pourcentage de tps que nous pouvons prendre pour effectuer la meilleure action
discount_factor = 0.9 #facteur de remise pour les prochaines récompenses
learning_rate = 0.9 # taux d'apprentissage qui est la vitesse a laquelle l'agent devrait apprendre

#exécuter sur 1000 épisodes de training
#print('Début du training!')
for episode in range(1000):
    #renvoie l'état initial pour cet épisode
    row_index, column_index = get_starting_location()
    
    
    #continuer de choisir les actions jusqu'à arriver à l'état final
    
    while not is_terminal_state(row_index, column_index):
        #choisir quelle action prendre pour passer à l'état suivant
        action_index = get_next_action(row_index, column_index, epsilon)
        
        #effectuer l'action choisie pour aller à l'état suivant
        old_row_index, old_column_index = row_index, column_index #stocker les anciens index de ligne et de colonne
        row_index, column_index = get_next_location(row_index, column_index, action_index)
        
        #Recoit la récompense qui renvoie à l'état suivant et calcule la différene temporelle
        reward = rewards[row_index, column_index]
        old_q_value = q_values[old_row_index, old_column_index, action_index]
        temporal_difference = reward + (discount_factor * np.max(q_values[row_index, column_index])) - old_q_value
        
        
        #Mettre à jour la q-value qui correspond à la paire etat-action précédente
        new_q_value = old_q_value + (learning_rate * temporal_difference)
        q_values[old_row_index, old_column_index, action_index] = new_q_value


        
print('Training terminé!')


# afficher quelques plus courts chemins
print(get_shortest_path(2, 1)) #Point de départ à la ligne 2 et colonne 1
print(get_shortest_path(1, 1)) #Point de départ à la ligne 1 et colonne 1








        
        
        
        
        
        
        
        
        
        
        
        
        
        













        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        






























        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    