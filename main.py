from datos import *
from funciones import *

def main():
    # Primero se valida el acceso con las variables traídas de datos.py
    if not login(USUARIO, PASSWORD):
        return
    
    # Menú principal interactivo
    while True:
        print("""
##############################
    INSCRIPCIÓN DE CURSOS
##############################
1.- Inscribir alumno
2.- Resumen de inscripciones
3.- Salir
        """)
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            inscribir_alumno(cursos, inscripciones, alumnos)
            
        elif opcion == "2":
            mostrar_resumen(inscripciones, alumnos)
            
        elif opcion == "3":
            print("Programa finalizado. ¡Gracias!")
            break
            
        else:
            print("Oposición inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
