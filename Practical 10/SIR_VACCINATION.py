#Copy the SIR codes


# import necessary l i b r a r i e s   
#in my case the version is python 3.12.2(not python 3.12.3)
import numpy as np 
import matplotlib . pyplot as plt 
#set the initiate data
population=10000

vaccination_rate = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9] #initialize the vaccination rate

infected=1
new_infected=0
new_recovered=0
recovered=0
beta=0.3
gamma=0.05
# create an vaccination list for store different vaccination rate
infected_under_different_vaccination_list={}
infected_list=[]
# what vaccination do = to reduce the susceptible population (change to population like recovered but not categorized as recovered population)
for rate in vaccination_rate:
#initialize the data for each rate

    infected=1
    new_infected=0
    new_recovered=0
    recovered=0
    vaccination=population*rate
    susceptible=population-vaccination-recovered-infected
#create lists to record value of infected, recovered,suspective and their changes


    
    infected_list=[infected]
    

# set the time course
    time_step=1000
    for i in range(time_step):
#multiplying beta by the proportion of infected people in the population to achieve infection probiblity
        infection_probility=beta*(infected/(population-vaccination))
# in real code test, sometimes negatibe dimensions occured, so add the if code to avoid it
        if population - vaccination <= 0:
            infection_probability = 0  # Avoid division by zero
        else:
            infection_probability = beta * (infected / (population - vaccination))
       
# upgrade the infected with np.random.choice to imitate the probility model, so does the recovered
#the below few lines are for debugging...since sometimes these two values will be below 0
        susceptible = max(0, susceptible-new_infected)  
        infected = max(0, infected+new_infected-new_recovered)
        recovered = min(population, recovered+new_recovered) 
        infection_probability = min(max(infection_probability, 0), 1)

        new_recovered=int(sum(np.random.choice([0, 1], infected, p=[1 - gamma, gamma])))
        new_infected=int(sum(np.random.choice([0,1],int(susceptible),p=[1-infection_probility,infection_probility])))


        recovered=recovered+new_recovered
        infected=infected+new_infected-new_recovered
        suseptible=susceptible-new_infected


# then append them in the list

        infected_list.append(infected)
        infected_under_different_vaccination_list[rate] = infected_list
#plot the results
plt.figure( figsize =(6 ,4) , dpi=150) 
# to add different vaccination rate in the figure
for rate, infected_list in infected_under_different_vaccination_list.items():
    plt.plot(infected_list, label=f'Vaccination rate {rate}')



plt.xlabel('Time Steps')
plt.ylabel('Number of people')
plt.title('SIR Vaccination Model')
plt.legend()# keep this line blank or that will disturb the whole figure
plt.show()

