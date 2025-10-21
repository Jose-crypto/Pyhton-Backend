'''
set o conjuntos se utiliza para almacenar items en una sola variable

Un conjunto es una colección desordenada , inmutable* y no indexada .


'''

#forma convencional
my_set= {'Barcelona',"Real Madrid","Bayer Munich"}


other_set= set()
other_set.add('value 2')
other_set.add('value 3')
print(other_set)

for c in my_set:
    print(c[6])

#ad item into the set with set methods

my_set.add('Jose')
my_set.add('Jose')

print(my_set)


#remove
my_set.remove('Jose')
print(my_set)
my_set.remove('Real Madrid')

print(f"set removed: ",my_set)