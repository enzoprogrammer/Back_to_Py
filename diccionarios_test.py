diccionario={'Argentina': 'Bs As', 'Peru':'Lima', 'España': 'Madrid'}
diccionario['Italia']= 'Roma'
print(diccionario)
print(diccionario['Argentina'])
del diccionario['Peru']
print(diccionario)


lista=['Bolivia', 'Uruguay', 'Paraguay']
diccionario2= {lista[0]:'La Paz', lista[1]: 'Montevideo', lista[2]: 'Asuncion'}
print(diccionario2)
print(diccionario.keys())
print(diccionario.values())

diccionario3= {'Nombre':'Enzo', 'Apellido':'?', 'Nacimiento':[13 , '01','2000']}
print(diccionario3)