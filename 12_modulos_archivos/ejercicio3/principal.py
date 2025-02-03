import acciones as acc

def mostrar_menu():
    print("===== Sistema de Registro de Estudiantes =====")
    print("1. Agregar Estudiante")
    print("2. Actualizar Información del Estudiante")
    print("3. Eliminar Estudiante")
    print("4. Listar Todos los Estudiantes")
    print("5. Salir")
    print("=============================================")

def main():
    estudiantes = {}

    while True:
        mostrar_menu()
        opc = int(input("Ingrese la opcion"))

        if opc == 1:
            print("--Agregar estudiante--")
            id_estudiante = input("Ingrese el ID del estudiante: ").strip()
            nombre = input("Ingrese el nombre del estudiante: ").strip()
            carrera = input("Ingrese la carrera del estudiante: ").strip()
            estudiantes = acc.agregar_estudiante(estudiantes, id_estudiante, nombre, carrera)
        elif opc == 2:
            print("--Actualizar estudiante--")
        elif opc == 3:
            print("--Eliminar estudiante--")
        elif opc == 4:
            print("--Listar estudiante--")
        elif opc ==5:
            print("Adios ")
            break
        else:
            print("Opcion invalada ingresa de nuevo")
        

if __name__ == "__main__":
    main()


