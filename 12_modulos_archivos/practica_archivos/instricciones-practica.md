

## **Ejercicio 1: Gestión de Contactos**

### **Descripción**
Crea un sistema sencillo de gestión de contactos utilizando diccionarios en Python. La práctica consiste en dividir la funcionalidad en tres archivos diferentes:

1. **`acciones.py`**: Contendrá una función para agregar un nuevo contacto al diccionario.
2. **`metodos.py`**: Incluirá una función para eliminar un contacto existente.
3. **`principal.py`**: Será el archivo principal que importará y utilizará las funciones de los otros dos archivos para interactuar con el usuario a través de un menú.

### **Objetivos**
- **`acciones.py`**: Implementar una función `agregar_contacto` que reciba el diccionario de contactos, el nombre del contacto y su número de teléfono, y añada esta información al diccionario.
  
- **`metodos.py`**: Implementar una función `eliminar_contacto` que reciba el diccionario de contactos y el nombre del contacto a eliminar. Si el contacto existe, lo eliminará; de lo contrario, mostrará un mensaje de error.
  
- **`principal.py`**: Crear un menú interactivo que permita al usuario elegir entre agregar un contacto, eliminar un contacto, mostrar todos los contactos o salir del programa. Este archivo utilizará las funciones definidas en `acciones.py` y `metodos.py`.

### **Instrucciones**
1. **Crear los Archivos**:
   - `acciones.py`
   - `metodos.py`
   - `principal.py`

2. **Implementar las Funciones**:
   - Define las funciones mencionadas en cada archivo según la descripción.
   
3. **Ejecutar el Programa**:
   - Ejecuta `principal.py` y utiliza el menú para agregar, eliminar y visualizar contactos.

### **Consideraciones**
- Asegúrate de manejar casos donde el usuario intente eliminar un contacto que no existe.
- Implementa validaciones básicas para las entradas del usuario.

---

## **Ejercicio 2: Inventario de Productos**

### **Descripción**
Desarrolla un sistema de inventario de productos utilizando diccionarios en Python, distribuido en tres archivos `.py`:

1. **`acciones.py`**: Contendrá una función para añadir o actualizar la cantidad de un producto en el inventario.
2. **`metodos.py`**: Incluirá una función para mostrar todos los productos en el inventario de manera ordenada.
3. **`principal.py`**: Será el archivo principal que permitirá al usuario interactuar con el inventario a través de un menú, utilizando las funciones de los otros dos archivos. 

### **Objetivos**
- **`acciones.py`**: Implementar una función `añadir_producto` que reciba el diccionario de inventario, el nombre del producto y la cantidad. Si el producto ya existe, actualizará su cantidad; de lo contrario, lo añadirá al inventario.
  
- **`metodos.py`**: Implementar una función `mostrar_inventario` que reciba el diccionario de inventario y lo muestre en un formato legible, listando cada producto y su cantidad correspondiente.
  
- **`principal.py`**: Crear un menú interactivo que permita al usuario elegir entre añadir/actualizar un producto, mostrar el inventario o salir del programa. Este archivo utilizará las funciones definidas en `acciones.py` y `metodos.py`. 

### **Instrucciones**
1. **Crear los Archivos**:
   - `acciones.py`
   - `metodos.py`
   - `principal.py`

2. **Implementar las Funciones**:
   - Define las funciones mencionadas en cada archivo según la descripción.
   
3. **Ejecutar el Programa**:
   - Ejecuta `principal.py` y utiliza el menú para gestionar el inventario de productos.

### **Consideraciones**
- Maneja correctamente la actualización de la cantidad de productos existentes.
- Asegúrate de que las cantidades ingresadas sean números válidos.
