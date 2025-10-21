'''
/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 */
'''

import requests

ip_adress= "5.237.45.48"
api_url=f"https://free.freeipapi.com/api/json/{ip_adress}"

try:
    response = requests.get(api_url)
    response.raise_for_status()
    
    data = response.json()
    print('Data from API')
    print(data)
except requests.exceptions.HTTPError as errh:
    print(f'HTTP error: {errh}')
except requests.exceptions.ConnectionError as errcon:
    print(f'Connection error: {errcon}')
    
except requests.exceptions.Timeout as tmerror:
    print(f'Error en tiempo de espera de solicitud: {tmerror}')
    
except requests.exceptions.RequestException as reqerror:
    print(f'Error of request: {reqerror}')