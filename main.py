#conectar los dos archivos a este
import seguridad
import procesos

def ejecutar_sistema():
# Primero se valida la seguridad (Login)
    if not seguridad.login():
        print("Cerrando aplicación por seguridad. 🏁")
        return

# Bucle principal si el login fue exitoso
    while True:
        print("\n🏎️  SISTEMA F1 - AFICIONADOS 🏎️")
        print("1. Inscribir Aficionado")
        print("2. Revisar Inscritos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            procesos.inscribir_aficionado()
        elif opcion == "2":
            procesos.revisar_inscritos()
        elif opcion == "3":
            print("\n🏁 Cerrando sesión. ¡Nos vemos en los Boxes!")
            break  
# Break para controlar el flujo
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_sistema()
