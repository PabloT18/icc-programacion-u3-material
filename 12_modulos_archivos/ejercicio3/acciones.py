
def agregar_estudiante(estudiantes,
                        id_estudiante ,
                          nombre,
                            carrera):
    """
    Actualiza la información de un estudiante existente.
    
    Parámetros:
    estudiantes (dict): Diccionario que almacena los estudiantes.
    id_estudiante (str): Identificador único del estudiante.
    nombre (str): Nuevo nombre del estudiante.
    carrera (str): Nueva carrera del estudiante.
    
    Retorna:
    dict: El diccionario de estudiantes actualizado.
    """
    if id_estudiante in estudiantes:
        print(f"Error: El ID {id_estudiante} ya está registrado.")
    else:
        estudiantes[id_estudiante] = {
            "nombre": nombre,
            "carrera": carrera
        }
        print(f"Estudiante agregado: {nombre} (ID: {id_estudiante}, Carrera: {carrera}).")

    return estudiantes

def actualizar_estudiante(estudiantes,
                           id_estudiante,
                          nombre=None,
                            carrera=None):
    """
    Actualiza la información de un estudiante existente.
    
    Parámetros:
    estudiantes (dict): Diccionario que almacena los estudiantes.
    id_estudiante (str): Identificador único del estudiante.
    nombre (str, opcional): Nuevo nombre del estudiante.
    carrera (str, opcional): Nueva carrera del estudiante.
    
    Retorna:
    dict: El diccionario de estudiantes actualizado.
    """
    if id_estudiante not in estudiantes:
        print(f"Error: No se encontró un estudiante con ID {id_estudiante}.")
    else:
        if nombre:
            estudiantes[id_estudiante]["nombre"] = nombre
            print(f"Nombre actualizado a: {nombre}.")
        if carrera:
            estudiantes[id_estudiante]["carrera"] = carrera
            print(f"Carrera actualizada a: {carrera}.")
        if not nombre and not carrera:
            print("No se proporcionaron nuevos datos para actualizar.")
    return estudiantes

