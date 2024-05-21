def famous_james_bond(birth_year):
    bond_actors={'Roger Moore':(1973,1986),
                 'Timothy Dalton':(1987,1994),	
                 'Pierce Brosnan':(1995,2005),	
                 'Daniel Craig':(2006,2021)}
    #set a category for the function
    for i, (j,k) in bond_actors.items():
        if j<=int(birth_year)+18<=k:
    # check where the birth_year are in, then output the corresponding year
            print(i)
        return i
    #end the function

# add a input as an example
birth_year=input('please input your birthyear(1965~2003)')
famous_james_bond(birth_year)


#create an example for a fixed year
Birth_yearexample=2002
famous_james_bond(Birth_yearexample)
