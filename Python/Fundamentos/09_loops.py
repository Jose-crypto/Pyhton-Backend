
# adivina la letra , tienes 3 intentos



def adivina_letra():

    iterador = 1
    while iterador<=3:
        letra= input(' Ingrese la letra: ')
        if letra== 'D':
            print('has acertado')
            break
        else:
            print('intentelo de nuevo!')
            iterador+=1
    
    if iterador== 4:
        print('finalizado')
    
        



#adivina_letra()





## forr loop

# print a square with numerals

for _ in range(6):
    print('*' * 6)




