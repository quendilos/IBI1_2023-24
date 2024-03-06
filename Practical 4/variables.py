a=40
b=36
c=30
d=a-b
e=b-c
f=d>=e
print(f)
#since f is false, so d<e, which means running and strength training is regime is a better regime.

X=1==1
Y=1!=1
W= (X or Y) and not (X==Y)

print(W)
#W is True, 
#If both X and Y are false, W is false, otherwise W is true.

#Truth table show as below

#X Y W
#T T F
#T F T
#F T T
#F F F

