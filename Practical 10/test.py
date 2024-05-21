import numpy as np
import matplotlib.pyplot as plt

# Set the initial data
population = 10000
vaccination_rate = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
beta = 0.3
gamma = 0.05
time_steps = 1000

# Create a dictionary to store the infection lists for different vaccination rates
infected_under_different_vaccination_list = {}

# Loop through each vaccination rate
for rate in vaccination_rate:
    # Initialize the variables for each vaccination rate
    infected = 1
    recovered = 0
    vaccination = population * rate
    susceptible = population - vaccination - infected - recovered

    # Initialize the list to record the number of infected individuals
    infected_list = [infected]

    for _ in range(time_steps):
        if population - vaccination <= 0:
            infection_probability = 0  # Avoid division by zero
        else:
            infection_probability = beta * (infected / (population - vaccination))

        # Ensure the probability is between 0 and 1
        infection_probability = min(max(infection_probability, 0), 1)

        # Convert susceptible to integer for np.random.choice
        susceptible = int(susceptible)
        new_infected = int(sum(np.random.choice([0, 1], susceptible, p=[1 - infection_probability, infection_probability])))
        new_recovered = int(sum(np.random.choice([0, 1], infected, p=[1 - gamma, gamma])))

        susceptible = max(0, susceptible - new_infected)  # Ensure susceptible does not go below 0
        infected = max(0, infected + new_infected - new_recovered)  # Ensure infected does not go below 0
        recovered = min(population, recovered + new_recovered)  # Ensure recovered does not exceed population

        infected_list.append(infected)

    # Store the infected list for this vaccination rate
    infected_under_different_vaccination_list[rate] = infected_list

# Plot the results for all vaccination rates
plt.figure(figsize=(10, 6), dpi=150)
for rate, infected_list in infected_under_different_vaccination_list.items():
    plt.plot(infected_list, label=f'Vaccination rate {rate}')
plt.xlabel('Time Steps')
plt.ylabel('Number of Infected People')
plt.title('SIR Vaccination Model - Infected Population Over Time')
plt.legend()
plt.show()
