#imort necessary models first
import numpy as np
import matplotlib.pyplot as plt
#creating the dataset-two lists
UK_cities=[0.56,0.62,0.04,9.7]
CN_cities=[0.58,8.4,29.9,22.2]
#output it
print (UK_cities)
print(CN_cities)
#Create the list of city names
UK_cities_names=['Edinburgh','Glasgow','Stirling','London']
China_cities_names=['Haining','Hangzhou','Beijing','Shanghai']


#the following is to set and to create the plot figure
#set the data for the figure
names = UK_cities_names
population = UK_cities
#the lines following is the set and customizing of figure 
fig = plt.figure(figsize = (5, 5))
plt.bar(names, population, color ='blue', width = 0.23)
plt.xlabel("Names of UK cities")
plt.ylabel("Population")
plt.title("population sizes for the UK")
#output the figure
plt.show()

#repeat the same scheme for the CN cities
#BUT A PROBLEM IS THAT I cannot show two figures respectively. 
#only after closing the first figure can the second figure be shown. 
#I am sorry for that.
namesCN = China_cities_names
populationCN = CN_cities
fig = plt.figure(figsize = (5, 5))

plt.bar(namesCN, populationCN, color ='blue', width = 0.23)

plt.xlabel("Names of China cities")
plt.ylabel("Population")
plt.title("population sizes for the China cities")
plt.show()
