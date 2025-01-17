### Escribe una funcion llamada OrdenarListta() que reciba una lista de numeros enteros y los escribe en un fichero llamado ListaOrdenada.txt. La funcion debe escribir la lista de numeros que recibe ordenada de mayor a menor en el archivo. La funcion no devuelve nada
### Escribe otra funcion (NumeroPar()) que abra un fichero que contiene una lista ordenada de numeros, lo lea y escriba en otro fichero llamado lista de pares.txt
def OrdenarLista():
    Lista = list[2, 9, 3, 4, 5, 6, 7, 8]
    Lista.sort()
    Lista.reverse()
    with open ('ListaOrdenada.txt.', 'w') as file:
        file.write(Lista)
   
    
    
OrdenarLista()
def NumeroPar():
    Lista = list['1','2','3','4','5','6','7']
    
    with open('ListaDePares.txt', 'w') as file:
        file.write(Lista.sort())
NumeroPar()

    