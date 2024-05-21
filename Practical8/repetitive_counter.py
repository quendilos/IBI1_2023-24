seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA' 
#import the seq
count=seq.find('GTGTGT')
#use find() method to find if a string matches a particular expression
txt='GTGTGT:{}'
print(txt.format(count))
#output the result

count2=seq.find('GTCTGT')
#Similarly apply it to another expression
txt2='GTCTGT:{}'
print(txt2.format(count2))