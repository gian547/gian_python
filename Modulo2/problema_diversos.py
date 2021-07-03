cantidad=int(input('Ingrese la cantidad de alumnos: '))
nombres=[]
notas=[]
for x in range(cantidad):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
    no1=int(input("Ingrese la primer nota:"))
    no2=int(input("Ingrese la segunda nota:"))
    no3=int(input("Ingrese la tercera nota:"))
    notas.append([no1,no2,no3])

for x in range(cantidad):
    print(nombres[x],notas[x][0],notas[x][1],notas[x][2])