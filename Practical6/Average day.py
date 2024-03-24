#set a property which combined activity and time(one corresponding to another)
average_activity_time = {'Sleeping':8,'Classes':6,'Studying':3.5,'TV':2,'Music':1,'Other':3.5}
#the following script is to print the certain element in the property, changing this variable can print other elements 
print (average_activity_time['Classes'])
#import necessary model
import matplotlib.pyplot as plt
#set the labels and time
class_labels=['Sleeping','Classes','Studying','TV','Music','Other']
time=[8,6,3.5,2,1,3.5]
#the following code is to show the figure
plt.figure()
plt.pie(time, labels=time)
plt.show()
