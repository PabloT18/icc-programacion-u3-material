


# Lenguanje de Programación

### Universidad Politécnica Salesiana  
### Ingeniería en Ciencias de la Computación  


<img src="assets/ups-icc.png" alt="Logo Carrera" style="height:75px;"/>

## Autores del Material
- **Instructor**: Ing. Pablo Torres
- **Contacto**: ptorresp@ups.edu.ec

---
### Programación Python


Este repositorio contiene el material del curso de Programación con Python. Está organizado en módulos que abordan diversos conceptos fundamentales de la programación, desde la introducción hasta el uso avanzado de estructuras de datos y programación orientada a objetos. Cada módulo incluye material teórico y ejercicios prácticos para reforzar el aprendizaje.

---

## Uso - Crear un Entorno Virtual

Para mantener las dependencias del proyecto organizadas y evitar conflictos con otros proyectos, se recomienda crear un entorno virtual llamado `env-pro`. Sigue estos pasos para crear el entorno virtual y instalar las dependencias necesarias.

### 1. Crear el Entorno Virtual

Abre una terminal en el directorio de tu proyecto y ejecuta el siguiente comando para crear el entorno virtual:

```bash
python3 -m venv env-pro
```
o 

```bash
python -m venv env-pro
```

Este comando creará un entorno virtual llamado `env-pro` en el directorio actual.

### 2. Activar el Entorno Virtual

Para activar el entorno virtual, usa el siguiente comando dependiendo de tu sistema operativo:

- **En Windows**:
  ```bash
  .\env-pro\Scripts\activate
  ```

- **En macOS/Linux**:
  ```bash
  source env-pro/bin/activate
  ```

Verás que el prompt de la terminal cambia, indicando que ahora estás trabajando dentro del entorno virtual.

### 3. Instalar Jupyter

Con el entorno virtual activado, instala Jupyter ejecutando el siguiente comando:

```bash
pip install jupyter
```

### 4. Instalar Numpy

Para trabajar con arrays y matrices en Python, puedes instalar Numpy ejecutando:

```bash
pip install numpy
```


---

## Módulos

### 01 Introducción
Este módulo introduce al lenguaje de programación Python, su instalación y configuración en el entorno de desarrollo. Se presentan los primeros conceptos básicos, como las variables, tipos de datos y operaciones simples.  
- **Archivos:**  
  - `01_intro.ipynb`: Contenido teórico sobre introducción a Python. 
  - `01_intro.pdf`, `01_intro.html`: Contenido en diversos formatos


### 02 Entradas y Salidas
En este módulo se cubre cómo interactuar con el usuario mediante entradas y salidas de datos en Python. Se exploran los métodos de entrada como `input()` y la función `print()` para mostrar información.  
- **Archivos:**  
  - `02_entradas_salidas.ipynb`: Introducción a las funciones de entrada y salida.  
  - `02_entradas_salidas.pdf`, `02_entradas_salidas.html`: Contenido en diversos formatos


### 03 Estructuras de Control
Este módulo cubre las estructuras de control de flujo en Python, como las sentencias `if`, `else`, y `elif`.

- **Archivos:**  
  - `03_estructuras_de_control.ipynb`: Teoría sobre estructuras de control, con ejercicios ejemplo.    
  - `03_estructuras_de_control.pdf`, `03_estructuras_de_control.html`: Contenido en diversos formatos
  - `03_estructuras_de_control-ejercicios.ipynb`: Ejercicios para practicar las estructuras de control.  


### 04 Estructuras de Iteración
En este módulo se profundiza en las estructuras de iteración, cubriendo bucles y su uso para la repetición de instrucciones, así como el control de flujo dentro de los bucles.  
- **Archivos:**  
  - `04_estructuras_de_iteracion.ipynb`: Introducción a las estructuras de iteración, con ejercicios ejemplo.  
  - `04_estructuras_de_iteracion.pdf`, `04_estructuras_de_iteracion.html`: Contenido en diversos formatos
  - `04_estructuras_iteracion_ejercicios.ipynb`: Ejercicios sobre el uso de bucles.  
  - `04_estructuras_iteracion_ejercicios-solv.ipynb`: Soluciones detalladas.

### 05 Funciones
Este módulo presenta el concepto de funciones en Python, su declaración y cómo pueden ser utilizadas para organizar el código y evitar la repetición.  
- **Archivos:**  
  - `05_funciones_python.ipynb`: Introducción a las funciones en Python.  
  - `05_funciones_python.pdf`, `05_funciones_python.html`: Contenido en diversos formatos
  - `05_funciones_ejercicios.ipynb`: Ejercicios para entender el uso de funciones.  
  - `05_funciones_ejercicios-sol.ipynb`: Soluciones a los ejercicios.
   - `05_funciones_ejercicios_A.ipynb`: Ejercicios para entender el uso de funciones.  
  - `05_funciones_ejercicios_A_solv.ipynb`: Soluciones a los ejercicios.

### 06 Cadenas
Se cubren las cadenas de texto en Python, incluyendo su manipulación, slicing, y funciones útiles como `split()`, `join()`, y otros métodos de cadena.  
- **Archivos:**  
  - `06_cadenas.ipynb`: Teoría sobre cadenas en Python, Soluciones detalladas.
  - `06_cadenas_strings_ejercicios.ipynb`: Ejercicios para practicar con cadenas. 

### 07 Arreglos
En este módulo se abordan las listas en Python, su creación, manipulación y las operaciones básicas como agregar, eliminar y acceder a elementos.  
- **Archivos:**  
  - `07_arreglos.ipynb`: Introducción a los arreglos (listas), Soluciones detalladas.
  - `07_arreglos-solucion.ipynb`: Ejercicios prácticos con listas.  


### 08 Ejercicios con Loops y Arreglos
Este módulo se centra en ejercicios que combinan bucles y arreglos, para mejorar la comprensión del trabajo con ambas estructuras.  
- **Archivos:**  
  - `08_ejercicons_loops_arreglos.ipynb`: Ejercicios que combinan loops y arreglos.  
  - `08_ejercicons_loops_arreglos-sol.ipynb`: Soluciones detalladas.

### 09 Matrices
Se introduce el concepto de matrices (listas de listas) en Python, con ejemplos de cómo manipularlas y realizar operaciones básicas.  
- **Archivos:**  
  - `09_matrices.ipynb`: Introducción a matrices en Python.  
  - `09_matrices-ejer.ipynb`: Ejercicios con matrices.  
  - `9_matrices_ejer_sol.ipynb`: Soluciones detalladas.

### 10 Tuplas
Este módulo explica el uso de tuplas en Python, una estructura de datos inmutable, y las diferencias clave con las listas.  
- **Archivos:**  
  - `10_tuplas.ipynb`: Teoría sobre tuplas.  

### 11 Diccionarios
Se abordan los diccionarios en Python, explicando cómo se crean, manipulan y acceden a sus elementos.  
- **Archivos:**  
  - `11_diccionarios.ipynb`: Introducción a diccionarios y sets.  
  

### 12 Módulos y Archivos
Este módulo cubre cómo trabajar con módulos y archivos en Python, incluyendo la importación de módulos y la lectura/escritura de archivos.  
- **Archivos:**  
  - `12_modulos_archivos.ipynb`: Introducción a módulos y archivos en Python.  
  - Directorio `practica_archivos`: Carpeta con instrucciones y arcvhivos de solucion.
  - Directorio `ejericio3`: Carpeta con instrucciones y arcvhivos de solucion. 

### 13 Main
Este módulo organiza el flujo principal del programa, mostrando cómo estructurar un programa con Python para una ejecución limpia y organizada.  
- **Archivos:**  
  - `main.md`: Teoría y ejemplo de cómo organizar un programa.  
  - `main.py`: Ejemplo de uso de estrucutra main en python
  

### 14 Clases
En este módulo se introduce la programación orientada a objetos, cubriendo conceptos clave como clases, objetos, métodos y atributos.  
- **Archivos:**  
  - `clses.md`: Teoría y ejemplo de clases en python.
  - `main.py`: Ejemplo de uso de estrucutra main en python donde se instancia una clase Estudiante
  - `estudiante.py`: Archivo con ejemplo de una `Clase` en python

---

## Recursos Adicionales

- [Python Documentation](https://docs.python.org/3/)
- [Tutoriales de Python en Español](https://python.org/es/)

## Referencias

1. Van Rossum, G. (1991). *Python Tutorial*. Python Software Foundation.
2. Lutz, M. (2013). *Learning Python*. O'Reilly Media.
3. Sweigart, A. (2015). *Automate the Boring Stuff with Python*. No Starch Press.

---