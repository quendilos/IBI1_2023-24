#Firstly extract the sequence in different fa.file
with open('SLC6A4_HUMAN.fa') as human_fa:
    sequence_human=''
    for line in human_fa:
        if line.startswith('>'):
            gene_name=line
        
        else:
                sequence_human=sequence_human+line
                sequence_human= sequence_human.replace('\n', '') #this code is to put all sequence in one line
                sequence_human= sequence_human+'\n'
with open('SLC6A4_MOUSE.fa') as mouse_fa:
     sequence_mouse=''
     for line in mouse_fa:
          
        if line.startswith('>'):
            gene_name=line
        
        else:
                sequence_mouse=sequence_mouse+line
                sequence_mouse= sequence_mouse.replace('\n', '') 
with open('SLC6A4_RAT.fa') as rat_fa:
     sequence_rat=''
     for line in rat_fa:
          
        if line.startswith('>'):
            gene_name=line
        
        else:
                sequence_rat=sequence_rat+line
                sequence_rat= sequence_rat.replace('\n', '') 
#Then compare them to achieve the alignment  score and identical rate
distance_socre=0
for	i	in	range(len(sequence_mouse)):	#compare	each	amino	acid	
    if	sequence_human[i]!=sequence_mouse[i]:				
            	distance_socre +=	1	#add	1	if	amino	acids	are	different
identical_rate=(1-distance_socre/len(sequence_human)) * 100  # caculate the identical rate
text3 = 'the identical rate in this case is {}%'
text4 = text3.format(identical_rate)
text1='the difference score between human and mouse is {}'
text2=text1.format(distance_socre)
print(text2)
print(text4)

# repeat it in the case of rat too.
distance_socre=0
for	i	in	range(len(sequence_rat)):	
    if	sequence_human[i]!=sequence_rat[i]:				
            	distance_socre +=	1	
identical_rate=(1-distance_socre/len(sequence_human)) * 100  # caculate the identical rate
text3 = 'the identical rate in this case is {}%'
text4 = text3.format(identical_rate)
text1='the difference score between human and rat is {}'
text2=text1.format(distance_socre)
print(text2)
print(text4)

#repeat it for the case of rat and mouse too.
distance_socre=0
for	i	in	range(len(sequence_rat)):	
    if	sequence_mouse[i]!=sequence_rat[i]:				
            	distance_socre +=	1	
identical_rate=(1-distance_socre/len(sequence_rat)) * 100  # caculate the identical rate
text3 = 'the identical rate in this case is {}%'
text4 = text3.format(identical_rate)
text1='the difference score between mouse and rat is {}'
text2=text1.format(distance_socre)
print(text2)
print(text4)
           
print('see the statements in the text file called statement')
