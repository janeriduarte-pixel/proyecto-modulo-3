# Credenciales de acceso básicas
USUARIO = "admin"
PASSWORD = "1234"

# Cursos disponibles: { ID: (Nombre, Cupos) }
cursos = {
    1: ("Python", 2),
    2: ("SQL", 2),
    3: ("Desarrollo Web", 2),
    4: ("JavaScript", 4)
}

# Lista para guardar las inscripciones en formato (Alumno, Curso)
inscripciones = []

# Conjunto (set) para mantener los nombres únicos de los alumnos
alumnos = set()
