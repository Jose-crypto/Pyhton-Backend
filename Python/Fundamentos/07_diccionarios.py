'''
DICCIONARIO

creacion de JSON 
'''


diccionario={
        'brand': 'Ford',
        'model': 'Mustang',
        'year': 1964,
        'color':{'Red','Black','White'}

}

other_dictionaty= dict()


##add item
diccionario['company']='Ford S.A'
diccionario.update({'year publication':'2025'})
print(diccionario.items())


#fromkeys
new_dictionary= dict.fromkeys(('Nombre',1,'Apellido'))
print(new_dictionary)