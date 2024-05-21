import re

with open ('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as input, open('duplicate_genes','w') as output:#set two files for input and output
    for line in input:
        if line.startswith('>Y'): #all gene name line start with'>'
                y=re.search(r'(\S+)_(\S+)',line)  #all gene name shares the same format of XXXX_xxxx, so we can use _ to select them
                gene_name=str(y[0]+'\n') # since gene name always appear in the first few words of each line, y{0},which select the first element in the list,  can select it
                output.write(gene_name)
               
        else:
            output.write(line)   # writing these seperate parts in the outputfile is the final step

     



    