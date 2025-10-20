my_string="Strings"

my_other_string="strings"

print(my_string,my_other_string)



#Salto de linea
my_tab_strings="This is a string with \ncon salto de linea"
print(my_tab_strings)

#operators
name , surname , age = "Jose", "Antonio",25
print("My name is %s %s and my age is %d" %(name,surname,age))
print("My name is {} {} and my age is {}" .format(name,surname,age))
print(f"My name is {name} {surname} and my age is {age}") #best pratice


#desempaquetado de caracteres
language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#division
language_slice= language[1:4]
print("Lenguaje cortado: ", language_slice)