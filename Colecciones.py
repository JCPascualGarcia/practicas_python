
"""
--------------------------- COLECCIONES ---------------------------
En este taller aprenderás a manipular coleccciones de datos: Listas, diccionarios, tuplas y sets.
"""
"""
 --- LISTAS ---
Las listas son ordenadas y mutables.
Pueden contener elementos duplicados.
Puedes modificar, añadir y eliminar elementos.
"""
"""
--- Ejercicio 1 Listas ---
Crea una variable "mascotas" que almacene una lista con los siguientes elementos: 'perro', 'gato', 'loro'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
# Escribe el código para saber la cantidad de elementos que tiene la lista, imprimir por consola
Mi_Lista = ["perro", "gato", "loro"]
print(Mi_Lista)
print("Númeor de elementos de la lista:", len(Mi_Lista))

# Escribe el código para acceder al valor de la posición 2, imprimir por consola
print("El elemento 2 es el: ", Mi_Lista[1])

# Escribe el código para agregar una elemento a la lista, imprimir por consola la lista
Mi_Lista.append("rana")
print("Hemos añadido un nuevo elemento y esta es la nueva lista", Mi_Lista)

# Escribe el código para modificar un elemento de la lista, imprimir por consola la lista
Mi_Lista[0]  = "serpiente"
print("hemos modificado un nueo elemento:", Mi_Lista)

# Escribe el código para eliminar un elemento de la lista, imprimir por consola la lista
Mi_Lista.remove("loro")
print("Hemos quitado el loro de mi lista. Esta es la nueva lista", Mi_Lista)

"""
 --- TUPLAS ---
Las tuplas son ordenadas e inmutables.
Pueden contener elementos duplicados.
No puedes modificar, añadir o eliminar elementos después de la creación.
"""
"""
--- Ejercicio 2 Tuplas ---
Crea una variable "plantas" que almacene una tupla con los siguientes elementos: 'cactus', 'orquidea', 'rosas'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
# Escribe tu código aquí
Plantas = ("cactus", "orquidea", "rosas")
print(Plantas)

# Escribe el código para saber la cantidad de elementos que tiene la tupla, imprimir por consola
print("Numero de elementos de la tupla", len(Plantas))

# Escribe el código para acceder al valor de la posición 2, imprimir por consola
print("La segunda planta es:", Plantas[1])

# Intentar modificar una tupla
# Plantas[1]="cactus"

# plantas[1] = 'hoja rota'  # Descomenta esta línea para ver qué sucede
# Escribe tu análisís acá acerca de qué sucede
"""
 --- SETS ---
Los sets son desordenados y mutables.
No pueden contener elementos duplicados.
Puedes añadir y eliminar elementos, pero no puedes modificar los elementos existentes.
"""
"""
--- Ejercicio 3 Sets ---
Crea una variable "nombres" que almacene un set con los siguientes elementos: 'María', 'Cris', 'Cris', 'Alex'
Imprime por la terminal dicha variable
Haz los pasos pedidos
"""
nombres = {"María", "Chris", "Chris", "Alex"}
print(nombres)
print("Este set de plantas tiene este número de elementos:", len(nombres))

# Explica qué sucede cuándo imprimes el valor que almacena "nombres"
# Escribe el código para saber la cantidad de elementos que tiene el set, imprimir por consola
# Escribe el código para acceder al valor de la posición 3, imprimir por consola
# Escribe el código para agregar una elemento al set, imprimir por consola el set
# Escribe el código para eliminar un elemento del set, imprimir por consola el set
"""
 --- DICCIONARIOS ---
Los diccionarios son desordenados y mutables.
Contienen pares clave-valor.
Puedes añadir, modificar y eliminar pares clave-valor.
"""
"""
--- Ejercicio 4 Diccionarios ---
Crea un diccionario llamado "ciudad" con las claves 'nombre' y 'pais' y los valores 'Barcelona' y 'España' respectivamente.
Imprime el diccionario
"""
# Escribe el código aqui para acceder y ver por consola el valor de 'nombre'
# Escribe el código aqui para añadir un nuevo par clave-valor y ver por consola el valor de 'ciudad'
# Escribe el código aqui para modificar el valor de un par clave-valor de 'ciudad' y verlo por consola
# Escribe el código aqui para eliminar un par clave-valor de 'ciudad' y verlo por consola