###Gestion de base de datos de un alumno
### 1 Añadir alumno
### 2 Numero de aprobados 
### 3 Mostrar todo el alumnado
terminar = False
Notas = {}
def añadir_alumno():
    Nombre = input('Introduzca el nombre del alumno')
    Nota = float(input('Introduzca la nota de la asignatura'))
    if Nota < 5:
        Nota_Asignatura = False
    else:
        Nota_Asignatura = True
    Alumno = {Nombre: Nota}
    Notas = Alumno
    print (Notas)
"""Añadir alumno al diccionario"""
def Numero_de_aprobados():
    Numero_aprobados = 0
    for valor in Notas.items():
        if valor['Nota'] == True:
            Numero_aprobados = Numero_aprobados =+ 1
        else:
            Numero_aprobados = Numero_aprobados =+ 0
            
    print (Numero_aprobados)
"""Numero de aprobados dentro del diccionario"""      

def Mostrar_todo_el_alumnado():
    print (Notas)
"""Muestra todos los alumonos del diccionario"""
while terminar == False:
    Numero_seleccionado = input('Introduzca uno de estos numeros: 1: Añadir alumno, 2: Numero de aprobados, 3: Mostrar todo el alumno')

    if Numero_seleccionado == '1':
        añadir_alumno()
    if Numero_seleccionado == '2':
        Numero_de_aprobados()
    if Numero_seleccionado == '3':
        Mostrar_todo_el_alumnado()
    