# import necessary l i b r a r i e s   
#in my case the version is python 3.12.2(not python 3.12.3)
import numpy as np 
import matplotlib . pyplot as plt 
#set the initiate data
population=10000
susceptible=population-1
infected=1
recovered=0
beta=0.3
gamma=0.05

#create lists to record value of infected, recovered,suspective and their changes
susceptible

susceptible_list=[susceptible]
infected_list=[infected]
recovered_list=[recovered]

# set the time course
time_step=1000
for i in range(time_step):
#multiplying beta by the proportion of infected people in the population to achieve infection probiblity
    infection_probility=beta*(infected/population)
# upgrade the infected with np.random.choice to imitate the probility model, so does the recovered
# but be careful that infected should also minus the new recovered number, that's why I introduce this new variable
    
    new_recovered=int(sum(np.random.choice([0, 1], infected, p=[1 - gamma, gamma])))
    infected=infected+int(sum(np.random.choice([0,1],int(susceptible),p=[1-infection_probility,infection_probility])))-new_recovered
    recovered=recovered+new_recovered
    susceptible=population-infected-recovered
# then append them in the list
    susceptible_list.append(susceptible)
    recovered_list.append(recovered)
    infected_list.append(infected)
#plot the results
plt.figure( figsize =(6 ,4) , dpi=150) 
plt.plot(susceptible_list, label='susceptible')
plt.plot(infected_list, label='infected')
plt.plot(recovered_list, label='recovered')
plt.xlabel('Time Steps')
plt.ylabel('Number of people')
plt.title('SIR Model')
plt.legend()# keep this line blank or that will disturb the whole figure
plt.show()
