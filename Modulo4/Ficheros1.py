n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = f'tabla-{n}.txt'
with open(file_name,mode='w') as f:
    
    for i in range(1,13):
        f.write(f'{n} x {i} = {n * i}\n')