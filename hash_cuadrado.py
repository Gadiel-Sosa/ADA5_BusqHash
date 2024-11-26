class TablaHash:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]  # Inicializa la tabla con listas vacías

    def funcion_hash(self, clave):
        # Calcula el cuadrado de la clave y toma los dos últimos dígitos
        cuadrado = clave ** 2
        indice = cuadrado % (10 ** len(str(self.tamaño)))  # Toma los últimos dígitos según el tamaño de la tabla
        return indice % self.tamaño  # Asegura que el índice esté dentro del rango de la tabla

    def insertar(self, clave):
        indice = self.funcion_hash(clave)
        if clave not in self.tabla[indice]:
            self.tabla[indice].append(clave)  # Inserta la clave si no está en la lista

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        if clave in self.tabla[indice]:
            return f"El elemento {clave} está en la tabla en el índice {indice}."
        else:
            return f"El elemento {clave} no está en la tabla."

    def mostrar(self):
        for i, lista in enumerate(self.tabla):
            print(f"Índice {i}: {lista}")


# Solicitar el tamaño de la tabla hash
tamaño = int(input("Introduce el tamaño de la tabla hash: "))
tabla_hash = TablaHash(tamaño)

# Llenar la tabla con un bucle for
print(f"\nIntroduce {tamaño} elementos para llenar la tabla hash:")
for i in range(tamaño):
    try:
        elemento = int(input(f"Elemento {i+1}: "))
        tabla_hash.insertar(elemento)
    except ValueError:
        print("Por favor, introduce un número entero.")

# Mostrar la tabla hash
print("\nTabla Hash:")
tabla_hash.mostrar()

# Solicitar al usuario el elemento a buscar
elemento_a_buscar = int(input("\nIntroduce el elemento a buscar: "))
print(tabla_hash.buscar(elemento_a_buscar))
