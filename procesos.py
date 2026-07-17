#archivo para gestionar y revisar los aficionados de F1

# Estructuras de datos
AFICIONADOS_REGISTRADOS = []  # Lista para los diccionarios
ALIAS_UNICOS = set()            # Conjunto para evitar duplicados

def inscribir_aficionado():
    """Inscribe a un fan pidiendo datos básicos."""
    print("\n--- NUEVA INSCRIPCIÓN ---")
    
    alias = input("Ingrese Alias: ").strip().upper()
    if not alias:
        print("⚠️ El alias no puede estar vacío.")
        return
        
# Validar duplicados
    if alias in ALIAS_UNICOS:
        print("⚠️ Este Alias ya se encuentra en uso.")
        return

    nombre = input("Nombre completo: ").strip().title()
    escuderia = input("Escudería favorita: ").strip().title()
    piloto = input("Piloto favorito: ").strip().title()

# Guardar información estructurada 
    aficionado = {
        "alias": alias,
        "nombre": nombre,
        "escuderia": escuderia,
        "piloto": piloto
    }

# Insertar en las estructuras
    AFICIONADOS_REGISTRADOS.append(aficionado)
    ALIAS_UNICOS.add(alias)
    
    print(f"\n✅ ¡Felicidades {nombre}! Inscripción registrada con éxito con el alias. {alias}.")

def revisar_inscritos():
# aqui se muestra la lista de todos los aficionados inscritos.
    print("\n--- REVISIÓN DE INSCRITOS ---")
    
    if not AFICIONADOS_REGISTRADOS:
        print("🛞 No hay aficionados inscritos todavía.")
        return

    print(f"Total de fans registrados: {len(AFICIONADOS_REGISTRADOS)}")
    print("=" * 55)
    # Bucle for para iterar de forma eficiente
    for i, fan in enumerate(AFICIONADOS_REGISTRADOS, 1):
        print(f"{i}. [{fan['alias']}] {fan['nombre']} | Team: {fan['escuderia']} | Piloto: {fan['piloto']}")
    print("=" * 55)
