# set the initialized data and figure about susceptible and infect outbreak as guide
import numpy as np 
import matplotlib . pyplot as plt 
population = np. zeros ( (100 , 100) ) 


outbreak = np. random . choice (range(100) ,2) 
population [ outbreak [0] , outbreak [ 1 ] ] = 1
# set the diesease spread data 
beta = 0.3  
gamma = 0.05  
time_steps = 100 
neighbours=[]
new_infected=[]
new_recovery=[]
# below is to output the initiative figure(i=0)
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('times:0')
plt.show()
#repeat the spread process for 101 times! the '1'more is for the 100th figure!
for i in range(time_steps+1):
#put all neighbours in a list
    new_infected=[]
    new_recovery=[]
    for a in range(100):
        for b in range(100):
            neighbours = []
            if population[a,b] == 1: # prevent the point out of 100
# list all neighbour and add them  
# if code ensure that the corner point will be included while the point out of 100 will be excluded
               
                    if a + 1 < 100: 
                         neighbours.append((a + 1, b))
                    if a - 1 >= 0: 
                         neighbours.append((a - 1, b))
                    if b + 1 < 100: 
                         neighbours.append((a, b + 1))
                    if b - 1 >= 0: 
                         neighbours.append((a, b - 1))
                    if a + 1 < 100 and b + 1 < 100: 
                         neighbours.append((a + 1, b + 1))
                    if a - 1 >= 0 and b + 1 < 100: 
                         neighbours.append((a - 1, b + 1))
                    if a + 1 < 100 and b - 1 >= 0: 
                         neighbours.append((a + 1, b - 1))
                    if a - 1 >= 0 and b - 1 >= 0:
                        neighbours.append((a - 1, b - 1))
                
            for (r, q) in neighbours:
# use an random probility code to imititate the infectqion ==0 means suspectitive audience
                    if population[r, q] == 0 and np.random.rand() <=beta:
                    
                            new_infected.append((r, q))
# then use same method toq imitate the recovery for each point
            
                    if np.random.rand() < gamma:
                        new_recovery.append((a, b))
# add them in the list to change its colour
# set infected as 1, recovery as 2
    for (r, q) in new_infected:
        population[r, q] = 1
    for (a, b) in new_recovery:
        population[a, b] = 2

#output the figure at 10 50 100 time points(i=0 has been outout below)

    if i in [10, 50, 100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title('Looking at disease spread in 2D')
        plt.show()
