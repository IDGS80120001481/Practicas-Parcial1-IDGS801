from io import open

class Files:
    def __init__(self, español = None, ingles = None, traductor = None, buscar = None):
        self.español = español
        self.ingles = ingles
        self.traductor = traductor
        self.buscar = buscar

    def agregarDiccionario(self, español, ingles):
        if español is not None and ingles is not None:
            # Agregamos las palabras en el diccionario
            archivo = open('Traductor.txt','a')
            archivo.write(f'\n {español.upper()}')
            archivo.write(f'\n {ingles.upper()}')
            archivo.close()
            return True
        else:
            return False

    def traducir(self, language, buscar):
        archivo = open('Traductor.txt','r')
        traductor = []
        for datos in archivo.readlines():
            traductor.append(datos.rstrip().strip())    
            
        try:
            index = traductor.index(buscar.upper())

            if language == 'esp':
                return traductor[index-1]
            else:
                return traductor[index+1]
        except Exception as e:
            print(f'Existe un error al intentar encontrar la palabra a través de su índice. {e}')
            return None