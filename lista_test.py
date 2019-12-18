lista=['Dogo', 'Pupo', 'Miel']
lista2=['Kiko', 'Pito']
lista3=[]

lista.append('Soso')
lista.insert(1,'Tito')
lista.extend(['pipo', 'jijo'])

indice= lista.index('pipo')
print(indice)

esta='Pupo' in lista
print(esta)

lista.remove(lista[0])
lista.remove('Soso')

lista.pop()

print(lista)

lista3=lista+ lista2
print(lista3)
lista3= lista3*3
print(lista3)


