import re

cadena = "hola a todos los itcs de este grupo"

lista = cadena.split()
print(lista)

lista2 = cadena.split('o')
print(lista2)

#Usando Regex
lista3 = re.search(r'todos', cadena)
print(lista3)