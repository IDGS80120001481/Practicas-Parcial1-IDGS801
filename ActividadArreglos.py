class Arrays:
    
    def __init__(self):
        self.array = []

    def getArrays(self):
        numero = int(input("Ingresa la cantidad de datos que requieres ingresar: "))

        for x in range(numero):
            self.array.append(int(input("Ingresa un numero: ")))

def main():
    arrays = Arrays()
    arrays.getArrays()

    # Ordena los arreglos en numeros pares
    array_pares = []
    array_inpares = []
    array_repetidos = []

    for x in arrays.array:
        if x % 2 == 1:
            array_inpares.append(x)
        else:
            array_pares.append(x)
   

    for i in range(len(arrays.array)):
        for j in range(i + 1, len(arrays.array)):
            if arrays.array[i] == arrays.array[j]:
                array_repetidos.append(arrays.array[i])
        
                

    print("Array original:", arrays.array)
    print("Array de números pares:", array_pares)
    print("Array de números impares:", array_inpares)
    print("Array de números repetidos:", array_repetidos)

if __name__ == "__main__":
    main()

    # Ordenar el arrglo, PARES, INPARES, REPETIDOS