## CLASES ###


class Persona:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad = edad
        
    def greeting(self):
        print(f'Hola soy {self.nombre}, tengo {self.edad} anios')
        
        

object_person= Persona('Jose Espinoza',25)
object_person.greeting()



# Create a class using the pokeapi and fet Pokemon

import requests

class Pokemon:
    def __init__(self, nombre):
        self.nombre= nombre.lower()
        self.url = f'https://pokeapi.co/api/v2/pokemon/{self.nombre}'
        
    def get_info(self):
        try:
            response = requests.get(self.url)
            data = response.json()
            print(data['abilities'])
            for abilitis in data['abilities']:
                name= abilitis['ability']['name']
                print(name)
            
        except requests.exceptions.RequestException as error:
            print(f'No se pudo obtener el Pokemón: {error}')


pikachu = Pokemon('pikachu')
pikachu.get_info()







pikachu = Pokemon('pikachu')