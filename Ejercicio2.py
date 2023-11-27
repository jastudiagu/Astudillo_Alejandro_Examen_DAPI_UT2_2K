base_datos= {}
cont = 0

while True:
    entrada = input('Escoja la opción del siguiente menú: (1) Añadir alumno, (2) Número de aprobados, (3) Mostrar todo el alumnado: ')
    if entrada == '1':
        nombre_alumno = input('Escriba el nombre del alumn@: ')
        nota = input('Escriba "0" si suspendido o "1" si aprobado: ')

        if nota == '1':
            nota = True

        elif nota == '0':
            nota = False

        base_datos[nombre_alumno] = nota

    elif entrada == '2':
        for i in base_datos:
            if base_datos[i] == True:
                cont = cont + 1
        print('El número de aprobados es:', cont)
        cont = 0
    
    elif entrada == '3':
        print('Lista de alumnos:')
        for i in base_datos:
            print(i)