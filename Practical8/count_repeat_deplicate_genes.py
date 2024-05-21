import re

repetitive_genes=str(input("'GTGTGT'or'GTCTGT'"))
file_name=f"{repetitive_genes}_duplicate_genes.fa" #use f""command to set up the correct file name
sequence=''
with open ('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as input, open('temporory_fa_file.fa','w') as output: 
#I prefer to create a fa. file as in 'duplicate_gene'task for future codes to avoid confusion.
     for line in input:
        if line.startswith('>Y'):
                y=re.search(r'(\S+)_(\S+)',line) 
                gene_name=str(y[0]+'\n') 
                output.write(gene_name)
               
        else:
            
            output.write(line)  
# below is the same as task 2

# the rest is to add the number into the fa.file

with open ('temporory_fa_file.fa', 'r') as input2, open(file_name, 'w') as output2:
     count=0
     sequence2=''
     for line in input2:
       
        count=count+1
# generally, the idea behind the rest code is to write the file with the former gene, sequence and number of repetition parts
# The former gene is finished once read the next gene name, that's why I write the file when find the gene name
# However, an exception is the first line, that's why I introduce the line.count code
        if line.startswith('>') and count!=1:
              output2.write(gene_name_with_number)
              output2.write(sequence2)
              # DO NOT forget to reset the sequence and number
              sequence2=''
              number=0
        if line.startswith('>'):
               gene_name2=line
               
              
        else:
               sequence2=sequence2+line
               sequence2 = sequence2.replace('\n', '') #this code is to put all sequence in one line
               sequence2 = sequence2+'\n'
               # once we extract the full sequence, we can count the repetitive gene parts within it, and store it for further writing
               number=sequence2.count(repetitive_genes)
               number= str(number)
               gene_name_with_number=gene_name2+number+'\n'
    #the rest lines are for writing the last gene
     output2.write(gene_name_with_number)
     output2.write(sequence2)
