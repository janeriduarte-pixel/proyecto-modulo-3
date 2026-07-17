# autenticación de usuario

def login() -> bool:
    """Verifica credenciales del administrador. Retorna True si es correcto."""
    print("\n🔒 CONTROL DE ACCESO AL SISTEMA")
    usuario_correcto = "admin"
    clave_correcta = "1234"
    
# Intentos ilimitados o controlados por while
    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ").strip()
        clave = input("Contraseña: ").strip()
        
        if usuario == usuario_correcto and clave == clave_correcta:
            print("\n🔓 Acceso concedido. ¡Bienvenido al panel de F1!")
            return True
        else:
            intentos -= 1
            print(f"❌ Credenciales incorrectas. Intentos restantes: {intentos}")
            print("-" * 30)
            
    print("\n🚨 Demasiados intentos fallidos. Sistema bloqueado.")
    return False
