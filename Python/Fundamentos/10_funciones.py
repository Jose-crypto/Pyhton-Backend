# create a function to get a products of Fake store API

import requests

def get_fake_store_products(code_product:int):
    try:
        response =requests.get(url=f'https://fakestoreapi.com/products/{code_product}')
        print(response.json())
    except:
        raise ("Error this response")
  
  
  


code_product= input('Ingrese el codigo del producto: ')  
    
get_fake_store_products(code_product)