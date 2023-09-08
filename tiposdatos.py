#Esto es una lista
dias_semana = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']

#Imprimir los datos de una lista con un for
print("Dias de la semana")
for dia in dias_semana:
    print(dia)

#Esto es un diccionario de alumnos cons sus calificaciones
calificaciones = {"Pepe":[4,4,5],"Juan":[3,4,4],"Moises":[4,5,3]}
print("Lista de alumnos")
for c in calificaciones:
    print(c)

print("Lista de alumnos con sus calificaciones")
for c in calificaciones:
    print(c,' : ',calificaciones[c])

print("Lista de alumnos y su promedio de calificaciones")
for c in calificaciones:
    print(c)
    suma = 0
    for i in calificaciones[c]:
        suma +=i
    print('prom: {0}'.format((suma/len(calificaciones[c]))))

#Tuplas, semejante a las listas pero inmutables
print('Meses del año')
meses = ('Enero','Febrero','Marzo','Abril','Mayo')
for mes in meses:
    print(mes)

#Otra lista, y los metodos de las lista
precios = [4500,1200,3600,8000]
print(precios)
#Agregar elementos a la lista
precios.append(900)
print(precios)
#quitar elementos segun posicion
precios.remove(1200)
print(precios)
#Quitar el ultimo elemento
print(precios.pop())
print(precios)
