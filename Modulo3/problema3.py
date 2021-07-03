cantidad=int(input('Ingrese la cantidad de alumnos: '))
nombres=[]
notas=[]
suma=0
for x in range(cantidad):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
    no1=int(input("Ingrese la primer nota:"))
    no2=int(input("Ingrese la segunda nota:"))
    no3=int(input("Ingrese la tercera nota:"))
    notas.append([no1,no2,no3])
    prom=(no1+no2+no3)/3
    suma=suma+prom

for x in range(cantidad):
    print(nombres[x],notas[x][0],notas[x][1],notas[x][2])
promtotal=suma/cantidad
print('El promedio total del salon es: {}'.format(promtotal))