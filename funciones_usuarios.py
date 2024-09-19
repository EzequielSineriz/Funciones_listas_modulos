from main import *
def ingreso_nombres(cant_pedidas:int):
    lista_nombres = []
    for i in range(cant_pedidas):
        nombre = input("Ingresa un nombre: ")
        lista_nombres.append(nombre)
        
    return lista_nombres

def lista_diez():
    lista_numeros = [0] * 10
    corte = "s"
    while corte == "s":
        numero = int (input("Ingrese un numero para agregar a la lista: "))
        posicion = int(input("Ingrese en la posicion que desar cambiarla: "))
        while posicion > 10:
            posicion = int(input("Error. Ingrese una posicion valida: "))
        lista_numeros[posicion] = numero
        corte = input("Desea seguir ingresando s/n: ")
    return lista_numeros

def input_min_max(minimo:int, maximo: int, cant_pedidos:int):
    lista_numeros = []
    for i in range(cant_pedidos):
        numero = int(input(f"Ingrese un numero entre ({minimo}) y ({maximo}) : "))
        while numero < minimo or numero > maximo:
            numero = int(input(f"Error ingrese dentro de los rangos validos min({minimo}) y max({maximo}) : "))
        lista_numeros.append(numero)
    return lista_numeros

def buscar_datos(lista:list, numero:int)->bool:
    retorno = False
    for i in range(len(lista)):
        if lista[i] == numero:
            retorno = True
    return retorno

def buscar_menores(nombres:list, edades:list)->list:
    # Encontrar la edad mínima
    edad_minima = min(edades)
    
    # Buscar las personas con esa edad mínima
    for i in range(len(edades)):
        if edades[i] == edad_minima:
         menores = [nombres[i], edades[i]]
    
    return menores

def mostrar_lista(nombres:list)->list:
    print (nombres)

def listar_usuarios_mexico():
    "Función para listar datos de usuarios de México"
    for i in range(len(paises)):
        if paises[i] == "México":
            print(f'Nombre: {nombres[i]}, Email: {emails[i]}, Teléfono: {telefonos[i]}, Edad: {edades[i]}, Código Postal: {codigos_postales[i]}')


def listar_datos_brasil():
    "Función para listar nombre, mail y teléfono de los usuarios de Brasil"
    for i in range(len(paises)):
        if paises[i] == "Brasil":
            print(f'Nombre: {nombres[i]}, Email: {emails[i]}, Teléfono: {telefonos[i]}')

def listar_usuario_mas_joven():
    "Función para listar el usuario más joven"
    edad_minima = min(edades)
    for i in range(len(edades)):
        if edades[i] == edad_minima:
            print(f'Nombre: {nombres[i]}, Email: {emails[i]}, Teléfono: {telefonos[i]}, Edad: {edades[i]}, País: {paises[i]}, Código Postal: {codigos_postales[i]}')


def promedio_edad():
    "Función para obtener el promedio de edad de los usuarios"
    promedio = sum(edades) / len(edades)
    print(f'El promedio de edad es: {promedio} años')


def mayor_edad_brasil():
    "Función para listar el usuario de mayor edad en Brasil"
    mayor_edad = -1
    indice_mayor = -1
    for i in range(len(paises)):
        if paises[i] == "Brasil" and edades[i] > mayor_edad:
            mayor_edad = edades[i]
            indice_mayor = i
    if indice_mayor != -1:
        print(f'Nombre: {nombres[indice_mayor]}, Email: {emails[indice_mayor]}, Teléfono: {telefonos[indice_mayor]}, Edad: {edades[indice_mayor]}, Código Postal: {codigos_postales[indice_mayor]}')


def listar_usuarios_mexico_brasil_cp_mayor_8000():
    "Función para listar usuarios de México y Brasil cuyo código postal sea mayor a 8000"
    for i in range(len(paises)):
        if paises[i] in ["México", "Brasil"] and codigos_postales[i] > 8000:
            print(f'Nombre: {nombres[i]}, Email: {emails[i]}, Teléfono: {telefonos[i]}, Código Postal: {codigos_postales[i]}')

def listar_italianos_mayores_40():
    "Función para listar nombre, mail y teléfono de los usuarios italianos mayores de 40 años "
    for i in range(len(paises)):
        if paises[i] == "Italia" and edades[i] > 40:
            print(f'Nombre: {nombres[i]}, Email: {emails[i]}, Teléfono: {telefonos[i]}')

def importar_listas():
    nombres = ["Juan Pérez", "Ana Silva", "Carlos Rossi", "Lucía Gómez", "Mario López", "Sofía García"]
    emails = ["juan.perez@gmail.com", "ana.silva@brasil.com", "carlos.rossi@italia.com", 
    "lucia.gomez@brasil.com", "mario.lopez@italia.com", "sofia.garcia@mexico.com"]
    telefonos = ["555-1234", "555-2345", "555-3456", "555-4567", "555-5678", "555-6789"]
    edades = [30, 25, 45, 35, 42, 22]
    paises = ["México", "Brasil", "Italia", "Brasil", "Italia", "México"]
    codigos_postales = [7500, 8200, 9010, 7999, 8500, 8600]


def menu():
    "Menu de opciones"
    while True:
        print("\nMenú de Opciones:")
        print("1- Listar los datos de los usuarios de México")
        print("2- Listar los nombre, mail y teléfono de los usuarios de Brasil")
        print("3- Listar los datos del/los usuario/s más joven/es")
        print("4- Obtener un promedio de edad de los usuarios")
        print("5- De los usuarios de Brasil, listar los datos del usuario de mayor edad")
        print("6- Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
        print("7- Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años")
        print("8- Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            listar_usuarios_mexico()
        elif opcion == "2":
            listar_datos_brasil()
        elif opcion == "3":
            listar_usuario_mas_joven()
        elif opcion == "4":
            promedio_edad()
        elif opcion == "5":
            mayor_edad_brasil()
        elif opcion == "6":
            listar_usuarios_mexico_brasil_cp_mayor_8000()
        elif opcion == "7":
            listar_italianos_mayores_40()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")
