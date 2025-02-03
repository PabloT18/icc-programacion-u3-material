# principal.py

from acciones import agregar_estudiante, actualizar_estudiante
from metodos import eliminar_estudiante, listar_estudiantes

def mostrar_menu():
    print("===== Sistema de Registro de Estudiantes =====")
    print("1. Agregar Estudiante")
    print("2. Actualizar Información del Estudiante")
    print("3. Eliminar Estudiante")
    print("4. Listar Todos los Estudiantes")
    print("5. Salir")
    print("=============================================")

def main():
    estudiantes = {}  # Diccionario para almacenar estudiantes
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            print("\n--- Agregar Estudiante ---")
            id_estudiante = input("Ingrese el ID del estudiante: ").strip()
            nombre = input("Ingrese el nombre del estudiante: ").strip()
            carrera = input("Ingrese la carrera del estudiante: ").strip()
            estudiantes = agregar_estudiante(estudiantes, id_estudiante, nombre, carrera)
        
        elif opcion == '2':
            print("\n--- Actualizar Información del Estudiante ---")
            id_estudiante = input("Ingrese el ID del estudiante a actualizar: ").strip()
            print("Ingrese los nuevos datos (deje en blanco para no modificar):")
            nombre = input("Nuevo nombre: ").strip()
            carrera = input("Nueva carrera: ").strip()
            # Solo pasar argumentos si se proporcionan
            nombre = nombre if nombre else None
            carrera = carrera if carrera else None
            estudiantes = actualizar_estudiante(estudiantes, id_estudiante, nombre, carrera)
        
        elif opcion == '3':
            print("\n--- Eliminar Estudiante ---")
            id_estudiante = input("Ingrese el ID del estudiante a eliminar: ").strip()
            estudiantes = eliminar_estudiante(estudiantes, id_estudiante)
        
        elif opcion == '4':
            print("\n--- Listar Todos los Estudiantes ---")
            listar_estudiantes(estudiantes)
        
        elif opcion == '5':
            print("Saliendo del sistema de registro de estudiantes. ¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción entre 1 y 5.")
        
        print("\n")  # Línea en blanco para separar operaciones

if __name__ == "__main__":
    main()
