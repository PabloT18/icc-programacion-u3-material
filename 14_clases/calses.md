
# Introducción a las Clases en Python  
Universidad Politécnica Salesiana  
Ingeniería en Ciencias de la Computación  
Programación Orientada a Objetos

<img src="../assets/ups-icc.png" alt="Logo Carrera" style="height:75px;"/>

---

## Autores del Material  
- **Instructor**: Ing. Pablo Torres  
- **Contacto**: ptorresp@ups.edu.ec

---

## A. Tema: Clases en Python

### Descripción General  
En este tema se introduce el concepto de **clases** en Python, la base de la Programación Orientada a Objetos (POO). Se aprenderá a definir clases, crear objetos (instancias) y utilizar atributos y métodos para modelar entidades del mundo real. Este enfoque facilita la organización, reutilización y mantenimiento del código en programas más complejos.

### Objetivos de Aprendizaje  
- Comprender qué es una clase y su importancia en la POO.  
- Aprender a definir clases y crear objetos en Python.  
- Utilizar atributos (variables de clase y de instancia) para almacenar datos.  
- Implementar métodos (funciones dentro de una clase) para definir comportamientos.  
- Conocer el método especial `__init__` para inicializar objetos.  
- Introducir conceptos básicos de herencia y polimorfismo.

---

## 1. Conceptos Básicos de las Clases

### 1.1. ¿Qué es una Clase?  
Una **clase** es una plantilla o modelo que define atributos y métodos para crear objetos. Los atributos pueden ser de instancia (propios de cada objeto) o de clase (compartidos por todas las instancias). El método `__init__` es el constructor de la clase, invocado al crear una nueva instancia; el primer parámetro de cualquier método de instancia es `self`, que hace referencia al objeto actual.

### 1.2. Definición de una Clase en Python

La sintaxis básica para definir una clase es la siguiente:

```python
class NombreDeLaClase:
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1
        self.atributo2 = parametro2
    
    def metodo_ejemplo(self):
        # Código del método
        return f"Los atributos son {self.atributo1} y {self.atributo2}"
```

---

## 2. Ejemplos Prácticos

### Ejemplo 1: Definir una Clase Básica  
Definiremos una clase `Estudiante` con atributos para el nombre, edad y carrera, y un método para mostrar su información.

```python
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}"

# Crear una instancia de Estudiante
est1 = Estudiante("Juan Pérez", 21, "Ingeniería en Sistemas")
print(est1.mostrar_informacion())
# Salida esperada: "Nombre: Juan Pérez, Edad: 21, Carrera: Ingeniería en Sistemas"
```

### Ejemplo 2: Métodos Adicionales y Uso de Atributos  
Extendamos la clase `Estudiante` para incluir un método que actualice la carrera del estudiante.

```python
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}"

    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera
        print(f"Carrera actualizada a: {self.carrera}")

# Crear una instancia de Estudiante y actualizar la carrera
est2 = Estudiante("María López", 20, "Ingeniería en Computación")
print(est2.mostrar_informacion())
est2.actualizar_carrera("Ingeniería Industrial")
print(est2.mostrar_informacion())
```


---

## 3. Buenas Prácticas y Recomendaciones  
- Documenta tus clases y métodos utilizando docstrings y comentarios para explicar su propósito y funcionamiento.  
- Utiliza atributos y métodos privados (por convención, usando un guión bajo) cuando sea necesario para proteger los datos.  
- Organiza tus clases en módulos y paquetes para mejorar la mantenibilidad del código.  
- Crea instancias y prueba cada método para asegurarte de que el comportamiento es el esperado.

---

## 4. Conclusión  
Las **clases** en Python son esenciales para organizar el código de manera orientada a objetos, permitiendo modelar entidades del mundo real, agrupar datos y comportamientos en una sola estructura y facilitar la reutilización y el mantenimiento del código. Se recomienda a los estudiantes explorar, experimentar y seguir practicando para dominar estos conceptos y aplicarlos en proyectos más complejos.

