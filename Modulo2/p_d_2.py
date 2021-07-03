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
    prom=(no1+no2+no3)/3
    contar=0
    desa=0
    if prom>=4:
        contar+=contar
    else:
        desa+=desa

print('Total de estudiantes aprobados: {}'.format(contar))
print('Total de estudiantes desaprobados: {}'.format(desa))