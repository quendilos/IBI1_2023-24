import matplotlib.pyplot as plt # still python is 3.12.2 rather than 3.12.3
import numpy as np
import datetime

#import dom part
# start the datatime
start_time = datetime.datetime.now()
import xml.dom.minidom
# use dom to read the xml file
#create the list of term elements ( as slides show)
DOM_tree = xml.dom.minidom.parse('go_obo.xml')
collection = DOM_tree.documentElement
terms = DOM_tree.getElementsByTagName('term')
# caculate the number of terms
molecular=0
biological=0
cellular=0
for term in terms:
#get the frequency of each term names selected by tag_name
        term_name = term.getElementsByTagName('namespace')[0].childNodes[0].data
        if term_name == 'molecular_function':
            molecular += 1
        else:
             if term_name == 'biological_process':
              biological += 1
             else:
                    if term_name == 'cellular_component':
                        cellular += 1
#output
text1='molecular_function:{}'
text2='biological_process:{}'
text3='cellular_component:{}'
print(text1.format(molecular))
print(text2.format(biological))
print(text3.format(cellular))
# end the datatime caculator
time1 = datetime.datetime.now() - start_time
print('datatime_for_DOM',time1)


#then is the sax method
import xml.sax
#similiarly, start the timer
start_time = datetime.datetime.now()
# read the file by sax
class GOHandler(xml.sax.ContentHandler):
# set how to deal with the sax( as the lecture slides show)
    def __init__(self):
        self.molecular=0
        self.cellular=0
        self.biological=0
        self.currentname=''



    
    def startElement(self, name, attributes):
        if name == 'namespace':

            self.currentname = ''
    
    def characters(self, content):
        self.currentname += content
    
            
    def endElement(self, name):
        if name == 'namespace':
            
# again caculate the frequency
            if self.currentname == 'molecular_function':
                self.molecular += 1
            else:
                if self.currentname== 'biological_process':
                    self.biological += 1
                else:
                    if self.currentname == 'cellular_component':
                            self.cellular += 1

#for the sax dealing
handler = GOHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('go_obo.xml')
#Output
print("Molecular Function:", handler.molecular)
print("Biological Process:", handler.biological)
print("Cellular Component:", handler.cellular)

time2= datetime.datetime.now()- start_time
print('datatime_for_SAX',time2)


if time1<time2:
     print('DOM is quicker than SAX')
else:
     if time1 == time2:
          print('both methods share same effeciency')
     else:
          print('SAX is quicker than DOM')
#ACCORDING to the results, SAX is the quicker method


# below is the set of pie chart 
# create a list consist of the name
GO_frequency=['Molecular Function','Biological Process','Cellular Component']
# create a list corresponding to the frequency
frequency=[handler.molecular, handler.biological, handler.cellular]
# below is the process to show the figure
plt.figure()
# set the pie figure
plt.pie(frequency, labels=GO_frequency)
plt.show()
# below is a bar chart
GO_frequency = ['Molecular Function', 'Biological Process', 'Cellular Component']
frequency = [handler.molecular, handler.biological, handler.cellular]
plt.bar(GO_frequency, frequency, color=['red', 'blue', 'orange'])
plt.xlabel('GO name')
plt.ylabel('Frequency')
plt.title('GO  Frequencies')
plt.show()