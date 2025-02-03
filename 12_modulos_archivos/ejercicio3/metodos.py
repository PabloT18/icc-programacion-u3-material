def eliminar_estudiante(estudiantes, id_estudiante):
    if id_estudiante in estudiantes:
        eliminado = estudiantes[id_estudiante]
        print(f"Estudiante eliminado: {eliminado['nombre']} 
              (ID: {id_estudiante}).")
        del estudiantes[id_estudiante]
    else:
        print(f"Error: No se encontró un estudiante con ID {id_estudiante}.")
    return estudiantes

def listar_estudiantes(estudiantes):
    # if len(estudiantes) ==0:
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\n=== Lista de Estudiantes Registrados ===")
        print(f"{'ID':<10} {'Nombre':<25} {'Carrera'}")
        print("-" * 50)
        for id_estudiante, info in estudiantes.items():
            print(f"{id_estudiante:<10} {info['nombre']:<25} {info['carrera']}")
        print("-" * 50 + "\n")