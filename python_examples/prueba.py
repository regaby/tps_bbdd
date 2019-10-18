import psycopg2


print ("mi primer programa")

x = 1
x -= 1


# print (x)


lista = ['nico', 'nahuel']

# print (lista[0])

alumno = []
dicc = {
	'nombre': 'nico',
	'edad': 25,
}
alumno.append(dicc)
dicc = {
	'nombre': 'nahuel',
	'edad': 21,
}
alumno.append(dicc)

print (alumno)
print (type(alumno[0]))



