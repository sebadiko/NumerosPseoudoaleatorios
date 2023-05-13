from datetime import datetime

#Función que recibe por parámtro la semilla, las dos constantes y la cantidad de números aleatorios que deseamos.
def lehmer(pSemilla, pA, pM, pN):
    sequence = []  # Se crea una lista vacía para almacenar los números generados.
    for i in range(pN):  
        pSemilla = (pA * pSemilla) % pM  
        sequence.append(pSemilla) 
    return sequence  # Se retorna la lista de números pseudoaleatorios generada.


a = int(input("Valor de a: "))  # Se solicita al usuario ingresar el valor de a.
m = int(input("Valor de m: "))  # Se solicita al usuario ingresar el valor de m.
n = int(input("Cantidad de numeros aleatorios: "))

#Se asigna a la semilla el valor transcurrido en segundos desde el 1 de enero de 1970 hasta la actualidad, por lo tanto, siempre cambia.
semilla = datetime.now().timestamp()
#datetime.now().timestamp()
# Se llama a la función lehmer enviando los valores ingresados por el usuario y la semilla generada a partir de la marca de tiempo.
generator = lehmer(semilla, a, m, n)

print("Tabla de números pseudoaleatorios generados:")
print("------------------------------")
print("|       Índice      |  Valor  |")
print("------------------------------")
for i in range(len(generator)):
    print(f"|        {i+1}         |  {format(generator[i], '.3f')}  |")
print("------------------------------")
