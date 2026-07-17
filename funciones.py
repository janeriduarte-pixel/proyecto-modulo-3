# Función para validar el ingreso al sistema (máximo 3 intentos)
def login(usuario_correcto, contrasena_correcta):
    intentos = 0
    max_intentos = 3
    
    while intentos < max_intentos:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        
        if usuario == usuario_correcto and contrasena == contrasena_correcta:
            print("\nAcceso concedido.\n")
            return True
        
        intentos += 1
        print(f"Usuario o contraseña incorrectos. Intento {intentos} de {max_intentos}")
    
    print("\nSe alcanzó el máximo de intentos. Programa finalizado.")
    return False


# Función simple para mostrar los cursos recorriendo el diccionario
def mostrar_cursos(cursos_disponibles):
    print("\n--- CURSOS DISPONIBLES ---")
    for codigo, curso in cursos_disponibles.items():
        nombre, cupos = curso
        print(f"{codigo}. {nombre} | Cupos: {cupos}")


# Función para realizar el proceso de inscripción
def inscribir_alumno(cursos_disponibles, lista_inscripciones, conjunto_alumnos):
    mostrar_cursos(cursos_disponibles)
    
    asignatura = input("\nSeleccione el número del curso (0 para salir): ")
    
    if asignatura == "0":
        return
        
# Validación por si el usuario ingresa letras en vez de números
    if not asignatura.isdigit():
# Acà utilice el isdigit, para romper el programa no se crashee, por si se coloca letras en vez de numeros del menù o codigos del curso.
        print("X Error: Debe ingresar solamente números.")
        return
        
    asignatura = int(asignatura)
    
# Validación de si el curso existe en nuestro diccionario
    if asignatura not in cursos_disponibles:
        print("X Error: Curso no encontrado.")
        return
        
    nombre_curso, cupos = cursos_disponibles[asignatura]
    
    # Validación de cupos disponibles
    if cupos == 0:
        print("X Error: No quedan cupos disponibles para este curso.")
        return
        
# Si todo está bien, pedimos el nombre del alumno
    nombre = input("Ingrese el nombre del alumno: ").capitalize()
    
# Guardamos los datos en las estructuras correspondientes
    lista_inscripciones.append((nombre, nombre_curso))
    conjunto_alumnos.add(nombre)
    
# Restamos un cupo actualizando el diccionario
    cursos_disponibles[asignatura] = (nombre_curso, cupos - 1)
    
    print(f"¡{nombre} inscrito correctamente en {nombre_curso}!")


# Función para mostrar los resultados de lo que se ha registrado
def mostrar_resumen(lista_inscripciones, conjunto_alumnos):
    print("\n==========================================")
    print("RESUMEN DE INSCRIPCIONES")
    print("==========================================")
    
    if len(lista_inscripciones) == 0:
        print("No existen inscripciones registradas.")
        return
        
    print(f"Cantidad total de inscripciones: {len(lista_inscripciones)}")
    for alumno, curso in lista_inscripciones:
        print(f" - {alumno} inscrito en: {curso}")
        
    print(f"\nCantidad de alumnos únicos registrados: {len(conjunto_alumnos)}")
    for alumno in conjunto_alumnos:
        print(f" - {alumno}")
