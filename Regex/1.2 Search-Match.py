import re

cadena = "hola a todos los itc de este grupo"

#La R sirve para definirlo como string de tipo raw
#Esto le quita el trato especial a la \
search = re.search(r'itc', cadena)

#print(search)
if search:
    print(search.span()) #regresa el indice donde empieza y donde termina
    print(search.string) #regresa todo el string donde se encuentre ka palabra o caracter
    print(search.group()) #regresa la palabra buscada
else:
    print(search)


#Match, va a salir NONE, a menos de que el valor sea el del inico
search = re.match(r'HOLA', cadena, re.IGNORECASE | re.ASCII)

if search:
    print(search.span())
    print(search.string)
    print(search.group())
else:
    print(search)

print(cadena.split())

for palabra in re.finditer(r'[a-z]+', cadena, re.IGNORECASE):
    print(palabra.group(0))