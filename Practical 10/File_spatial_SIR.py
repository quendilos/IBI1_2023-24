# import the necessary moudel
import numpy as np
import matplotlib.pyplot as plt

# intialize the suspectible/population
population = np.zeros((100, 100))

# randomize a point for the otbreak point
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1 
# intialize the data
beta = 0.3  
gamma = 0.05  
time_steps = 100 

#check the neighbours infected or not
def get_neighbours(x, y, size):
    neighbours = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i != 0 or j != 0) and (0 <= x + i < size) and (0 <= y + j < size):
                neighbours.append((x + i, y + j))
    return neighbours

#Then operate the outbreak model in the time_steps...
for _ in range(time_steps):
# set the intiative variables lists
    new_infected = []
    new_recovery = []
    for i in range(100):
        for j in range(100):
            if population[i, j] == 1:
                neighbours = get_neighbours(i, j, 100)
# for the outbreak and determine its neigbours
# and then determine if their neibours are infected
                for (x, y) in neighbours:
                    if population[x, y] == 0 and np.random.rand() < beta:
                        new_infected.append((x, y))
# Check RECOVERY OR NOT
                if np.random.rand() < gamma:
                    new_recovery.append((i, j))
    
#NOW that log the infected and recovert data in the set
    for (x, y) in new_infected:
        population[x, y] = 1
    for (x, y) in new_recovery:
        population[x, y] = 2
    # output the figure
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title('title')
    plt.show()