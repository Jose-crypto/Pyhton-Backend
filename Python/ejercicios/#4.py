
def area_poligono(poligono):
    if poligono=="cuadrado":
        lado_1=int(input("ingrese primer lado: "))
        lado_2=int(input("ingrese segundo lado: "))
        print(f"El area es {lado_1*lado_2}")
    elif poligono=="rectangulo":
        base = float(input("ingrese base: "))
        altura = float(input("ingrese altura: "))
        print(f"El are del rectangulo es {base*altura}")
    else:
        base = float(input("ingrese base: "))
        altura = float(input("ingrese altura: "))
        print(f"El are del Triangulo es {(base*altura)/2}")






area_poligono('triangulo')
