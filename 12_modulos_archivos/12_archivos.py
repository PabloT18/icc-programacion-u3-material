# %% [markdown]
# # 12. Paquetes, Módulos e Importación de Múltiples Archivos en Python
# ### Universidad Politécnica Salesiana
# ### Ingeniería en Ciencias de la Computación
# ### Programación
# 
# <img src="../assets/ups-icc.png" alt="Logo Carrera" style="height:75px;"/>

# %% [markdown]
# ---
# 
# ## Autores del Material
# - **Instructor**: Ing. Pablo Torres
# - **Contacto**: ptorresp@ups.edu.ec
# 
# ---
# 
# ## A. Tema: Paquetes, Módulos e Importación de Múltiples Archivos en Python
# 
# ### Descripción General
# En este tema, aprenderemos sobre **paquetes** y **módulos** en Python, así como cómo **importar** y **utilizar** múltiples archivos `.py` en nuestros proyectos. Exploraremos la creación de módulos personalizados, la organización de código en paquetes, y las diferentes formas de importar y utilizar funciones, clases y variables definidas en otros archivos. Además, veremos cómo estructurar proyectos de Python de manera eficiente y aplicar buenas prácticas para la reutilización de código.

# %% [markdown]
# ### Objetivos de Aprendizaje
# - Comprender qué son los módulos y paquetes en Python y su importancia.
# - Aprender a crear y utilizar módulos personalizados.
# - Conocer las diferentes formas de importar módulos y sus componentes.
# - Organizar código en paquetes para mejorar la mantenibilidad y reutilización.
# - Manejar rutas de importación y resolver conflictos de nombres.
# - Aplicar buenas prácticas en la creación y uso de módulos y paquetes.
# - Realizar ejercicios prácticos que involucren la creación y uso de múltiples archivos `.py`.

# %% [markdown]
# ---
# 
# ## 1. Introducción a Módulos y Paquetes
# 
# ### 1.1. ¿Qué es un Módulo?
# 
# Un **módulo** en Python es simplemente un archivo que contiene definiciones y declaraciones de Python, como funciones, clases y variables. Los módulos permiten organizar el código en componentes reutilizables y facilitan la colaboración en proyectos grandes.
# 
# ### 1.2. ¿Qué es un Paquete?
# 
# Un **paquete** es una colección de módulos organizados en directorios. Los paquetes permiten estructurar el espacio de nombres de manera jerárquica y facilitan la distribución y gestión de módulos relacionados.

# %% [markdown]
# ## 2. Creación y Uso de Módulos
# 
# ### 2.1. Crear un Módulo Personalizado
# 
# Para crear un módulo personalizado, simplemente crea un archivo `.py` con las definiciones que deseas incluir. Por ejemplo, crea un archivo llamado `mimodulo.py` con el siguiente contenido:
# 
# ```python
# # mimodulo.py
# 
# def saludar(nombre):
#     """
#     Función para saludar a una persona.
#     """
#     return f"Hola, {nombre}!"
# 
# def sumar(a, b):
#     """
#     Función para sumar dos números.
#     """
#     return a + b
# 
# PI = 3.1416
# ```

# %% [markdown]
# ### 2.2. Importar un Módulo
# 
# Puedes importar un módulo utilizando la palabra clave `import` o utilizando `from ... import ...`. A continuación, se muestran diferentes formas de importar y utilizar el módulo `mimodulo`.
# 
# ```python
# # Importar todo el módulo
# import mimodulo
# 
# print(mimodulo.saludar("Ana"))  # Output: Hola, Ana!
# print(mimodulo.sumar(5, 7))     # Output: 12
# print(mimodulo.PI)              # Output: 3.1416
# ```
# 
# ```python
# # Importar funciones específicas del módulo
# from mimodulo import saludar, sumar
# 
# print(saludar("Juan"))  # Output: Hola, Juan!
# print(sumar(10, 15))    # Output: 25
# ```
# 
# ```python
# # Importar todo el contenido del módulo directamente
# from mimodulo import *
# 
# print(saludar("Luis"))  # Output: Hola, Luis!
# print(sumar(3, 4))      # Output: 7
# print(PI)               # Output: 3.1416
# ```

# %% 
# Importar todo el módulo
import mimodulo

print(mimodulo.saludar("Ana"))  # Output: Hola, Ana!
print(mimodulo.sumar(5, 7))     # Output: 12
print(mimodulo.PI)              # Output: 3.1416

# %% 
# Importar funciones específicas del módulo
from mimodulo import saludar, sumar

print(saludar("Juan"))  # Output: Hola, Juan!
print(sumar(10, 15))    # Output: 25

# %%
# Importar todo el contenido del módulo directamente
from mimodulo import *

print(saludar("Luis"))  # Output: Hola, Luis!
print(sumar(3, 4))      # Output: 7
print(PI)               # Output: 3.1416

# %% [markdown]
# ---
# 
# ## 3. Organización de Código en Paquetes
# 
# ### 3.1. Crear un Paquete
# 
# Para crear un paquete, simplemente crea un directorio con un archivo `__init__.py`. Por ejemplo, crea una estructura de directorios como la siguiente:
# 
# ```
# mi_paquete/
# ├── __init__.py
# ├── modulo1.py
# └── modulo2.py
# ```
# 
# - **`__init__.py`**: Archivo que indica a Python que este directorio debe ser tratado como un paquete. Puede estar vacío o contener inicializaciones de paquete.
# - **`modulo1.py`** y **`modulo2.py`**: Módulos dentro del paquete.
# 
# ### 3.2. Ejemplo de Paquete
# 
# **Contenido de `modulo1.py`:**
# 
# ```python
# # modulo1.py
# 
# def funcion1():
#     return "Función 1 del Módulo 1"
# ```
# 
# **Contenido de `modulo2.py`:**
# 
# ```python
# # modulo2.py
# 
# def funcion2():
#     return "Función 2 del Módulo 2"
# ```
# 
# **Contenido de `__init__.py`:**
# 
# ```python
# # __init__.py
# 
# from .modulo1 import funcion1
# from .modulo2 import funcion2
# ```

# %% [markdown]
# ### 3.3. Importar Módulos desde un Paquete
# 
# Puedes importar módulos o funciones desde un paquete de diferentes maneras.
# 
# ```python
# # Importar todo el paquete
import mi_paquete
print(mi_paquete.funcion1())  # Output: Función 1 del Módulo 1
print(mi_paquete.funcion2())  # Output: Función 2 del Módulo 2
# ```
# 
# ```python
# # Importar funciones específicas
from mi_paquete import funcion1
print(funcion1())  # Output: Función 1 del Módulo 1
# ```
# 
# ```python
# # Importar con alias
from mi_paquete import funcion2 as f2
print(f2())  # Output: Función 2 del Módulo 2
# ```

# %% 
# Importar todo el paquete
import mi_paquete
print(mi_paquete.funcion1())  # Output: Función 1 del Módulo 1
print(mi_paquete.funcion2())  # Output: Función 2 del Módulo 2

# %%
# Importar funciones específicas
from mi_paquete import funcion1
print(funcion1())  # Output: Función 1 del Módulo 1

# %%
# Importar con alias
from mi_paquete import funcion2 as f2
print(f2())  # Output: Función 2 del Módulo 2

# %% [markdown]
# ---
# 
# ## 4. Manejo de Rutas de Importación y Conflictos de Nombres
# 
# ### 4.1. Rutas Relativas y Absolutas
# 
# - **Rutas Absolutas**: Especifican la ruta completa desde la raíz del proyecto.
# - **Rutas Relativas**: Especifican la ruta relativa al archivo actual.
# 
# ```python
# # Ruta absoluta
import mi_paquete.modulo1
print(mi_paquete.modulo1.funcion1())
# 
# # Ruta relativa (dentro de un paquete)
from .modulo2 import funcion2
print(funcion2())
# ```
# 
# ### 4.2. Resolver Conflictos de Nombres
# 
# Si tienes módulos con el mismo nombre en diferentes paquetes, puedes resolver los conflictos utilizando alias.
# 
# ```python
# import paquete1.modulo as mod1
# import paquete2.modulo as mod2
# 
# print(mod1.funcion())
# print(mod2.funcion())
# ```

# %% [markdown]
# ---
# 
# ## 5. Buenas Prácticas en la Creación y Uso de Módulos y Paquetes
# 
# - **Nombres Descriptivos**: Usa nombres claros y descriptivos para módulos y paquetes.
# - **Evita Nombres Confusos**: Evita usar nombres de módulos que puedan confundirse con módulos estándar de Python.
# - **Organiza el Código Lógicamente**: Agrupa módulos relacionados dentro de paquetes.
# - **Documenta tus Módulos**: Añade docstrings para describir la funcionalidad de módulos, clases y funciones.
# - **Mantén la Simplicidad**: No sobrecargues los módulos con demasiadas funcionalidades; divide el código en módulos coherentes.

# %% [markdown]
# ---
# 
# ## 6. Ejemplos Prácticos
# 
# ### 6.1. Crear y Utilizar Módulos en Múltiples Archivos
# 
# **Archivo 1: `calculadora.py`**
# 
# ```python
# # calculadora.py
# 
# def sumar(a, b):
#     return a + b
# 
# def restar(a, b):
#     return a - b
# 
# def multiplicar(a, b):
#     return a * b
# 
# def dividir(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error: División por cero"
# ```
# 
# **Archivo 2: `principal.py`**
# 
# ```python
# # principal.py
# 
# import calculadora
# 
# def main():
#     print("Suma:", calculadora.sumar(10, 5))          # Output: Suma: 15
#     print("Resta:", calculadora.restar(10, 5))        # Output: Resta: 5
#     print("Multiplicación:", calculadora.multiplicar(10, 5))  # Output: Multiplicación: 50
#     print("División:", calculadora.dividir(10, 5))    # Output: División: 2.0
#     print("División por cero:", calculadora.dividir(10, 0))  # Output: Error: División por cero
# 
# if __name__ == "__main__":
#     main()
# ```
# 
# **Ejecución:**
# 
# Al ejecutar `principal.py`, obtendrás:
# ```
# Suma: 15
# Resta: 5
# Multiplicación: 50
# División: 2.0
# División por cero: Error: División por cero
# ```

# %% [markdown]
# ### 6.2. Crear un Paquete con Múltiples Módulos
# 
# **Estructura del Paquete `geometria`:**
# 
# ```
# geometria/
# ├── __init__.py
# ├── area.py
# └── perimetro.py
# ```
# 
# **Contenido de `area.py`:**
# 
# ```python
# # area.py
# 
# def area_cuadrado(lado):
#     return lado * lado
# 
# def area_circulo(radio):
#     PI = 3.1416
#     return PI * radio * radio
# ```
# 
# **Contenido de `perimetro.py`:**
# 
# ```python
# # perimetro.py
# 
# def perimetro_cuadrado(lado):
#     return 4 * lado
# 
# def perimetro_circulo(radio):
#     PI = 3.1416
#     return 2 * PI * radio
# ```
# 
# **Contenido de `__init__.py`:**
# 
# ```python
# # __init__.py
# 
# from .area import area_cuadrado, area_circulo
# from .perimetro import perimetro_cuadrado, perimetro_circulo
# ```
# 
# **Archivo Principal: `main_geometria.py`**
# 
# ```python
# # main_geometria.py
# 
# import geometria
# 
# def main():
#     lado = 5
#     radio = 3
#     
#     print("Área del Cuadrado:", geometria.area_cuadrado(lado))          # Output: Área del Cuadrado: 25
#     print("Perímetro del Cuadrado:", geometria.perimetro_cuadrado(lado))  # Output: Perímetro del Cuadrado: 20
#     
#     print("Área del Círculo:", geometria.area_circulo(radio))          # Output: Área del Círculo: 28.2744
#     print("Perímetro del Círculo:", geometria.perimetro_circulo(radio))  # Output: Perímetro del Círculo: 18.8496
# 
# if __name__ == "__main__":
#     main()
# ```
# 
# **Ejecución:**
# 
# Al ejecutar `main_geometria.py`, obtendrás:
# ```
# Área del Cuadrado: 25
# Perímetro del Cuadrado: 20
# Área del Círculo: 28.2744
# Perímetro del Círculo: 18.8496
# ```

# %% [markdown]
# ---
# 
# ## 7. Ejercicios Prácticos
# 
# ### 7.1. Crear y Utilizar Módulos en Múltiples Archivos
# 
# **Descripción:** Crea dos archivos Python: `operaciones.py` y `principal.py`. En `operaciones.py`, define funciones para sumar, restar, multiplicar y dividir dos números. En `principal.py`, importa estas funciones y crea un menú interactivo que permita al usuario seleccionar una operación y realizarla con los números ingresados.
# 
# **Instrucciones:**
# 1. **Crear `operaciones.py`:**
# 
# ```python
# # operaciones.py
# 
# def sumar(a, b):
#     return a + b
# 
# def restar(a, b):
#     return a - b
# 
# def multiplicar(a, b):
#     return a * b
# 
# def dividir(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error: División por cero"
# ```
# 
# 2. **Crear `principal.py`:**
# 
# ```python
# # principal.py
# 
# from operaciones import sumar, restar, multiplicar, dividir
# 
# def main():
#     while True:
#         print("\n--- Calculadora ---")
#         print("1. Sumar")
#         print("2. Restar")
#         print("3. Multiplicar")
#         print("4. Dividir")
#         print("5. Salir")
#         opcion = input("Selecciona una opción (1-5): ")
#         
#         if opcion == '5':
#             print("¡Hasta luego!")
#             break
#         
#         if opcion in ['1', '2', '3', '4']:
#             try:
#                 num1 = float(input("Ingresa el primer número: "))
#                 num2 = float(input("Ingresa el segundo número: "))
#             except ValueError:
#                 print("Error: Por favor, ingresa números válidos.")
#                 continue
#             
#             if opcion == '1':
#                 resultado = sumar(num1, num2)
#                 operacion = "Suma"
#             elif opcion == '2':
#                 resultado = restar(num1, num2)
#                 operacion = "Resta"
#             elif opcion == '3':
#                 resultado = multiplicar(num1, num2)
#                 operacion = "Multiplicación"
#             elif opcion == '4':
#                 resultado = dividir(num1, num2)
#                 operacion = "División"
#             
#             print(f"{operacion} de {num1} y {num2}: {resultado}")
#         else:
#             print("Opción inválida. Por favor, selecciona una opción entre 1 y 5.")
# 
# if __name__ == "__main__":
#     main()
# ```
# 
# **Ejecución:**
# 
# Al ejecutar `principal.py`, el usuario verá un menú interactivo para realizar operaciones matemáticas básicas.

# %% [markdown]
# ### 7.2. Crear un Paquete y Utilizar sus Módulos
# 
# **Descripción:** Crea un paquete llamado `utilidades` que contenga dos módulos: `texto.py` y `matematicas.py`. En `texto.py`, define funciones para convertir cadenas a mayúsculas y minúsculas. En `matematicas.py`, define funciones para calcular el factorial y la potencia de un número. Luego, crea un archivo `principal_paquete.py` que importe y utilice estas funciones.
# 
# **Instrucciones:**
# 1. **Crear la estructura del paquete `utilidades`:**
# 
# ```
# utilidades/
# ├── __init__.py
# ├── texto.py
# └── matematicas.py
# ```
# 
# 2. **Contenido de `texto.py`:**
# 
# ```python
# # texto.py
# 
# def a_mayusculas(texto):
#     return texto.upper()
# 
# def a_minusculas(texto):
#     return texto.lower()
# ```
# 
# 3. **Contenido de `matematicas.py`:**
# 
# ```python
# # matematicas.py
# 
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# 
# def potencia(base, exponente):
#     return base ** exponente
# ```
# 
# 4. **Contenido de `__init__.py`:**
# 
# ```python
# # __init__.py
# 
# from .texto import a_mayusculas, a_minusculas
# from .matematicas import factorial, potencia
# ```
# 
# 5. **Crear `principal_paquete.py`:**
# 
# ```python
# # principal_paquete.py
# 
# import utilidades
# 
# def main():
#     texto = "Hola Mundo"
#     print("Original:", texto)
#     print("Mayúsculas:", utilidades.a_mayusculas(texto))
#     print("Minúsculas:", utilidades.a_minusculas(texto))
#     
#     numero = 5
#     print(f"\nFactorial de {numero}:", utilidades.factorial(numero))  # Output: 120
#     base = 2
#     exponente = 3
#     print(f"Potencia de {base} elevado a {exponente}:", utilidades.potencia(base, exponente))  # Output: 8
# 
# if __name__ == "__main__":
#     main()
# ```
# 
# **Ejecución:**
# 
# Al ejecutar `principal_paquete.py`, obtendrás:
# ```
# Original: Hola Mundo
# Mayúsculas: HOLA MUNDO
# Minúsculas: hola mundo
# 
# Factorial de 5: 120
# Potencia de 2 elevado a 3: 8
# ```

# %% [markdown]
# ### 7.3. Crear y Utilizar Métodos en Múltiples Archivos
# 
# **Descripción:** Crea dos archivos Python: `operaciones_multiples.py` y `principal_multiples.py`. En `operaciones_multiples.py`, define una clase `Operaciones` con métodos para sumar y restar. En `principal_multiples.py`, importa la clase `Operaciones`, crea una instancia y utiliza sus métodos.
# 
# **Instrucciones:**
# 1. **Crear `operaciones_multiples.py`:**
# 
# ```python
# # operaciones_multiples.py
# 
# class Operaciones:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     
#     def sumar(self):
#         return self.a + self.b
#     
#     def restar(self):
#         return self.a - self.b
# ```
# 
# 2. **Crear `principal_multiples.py`:**
# 
# ```python
# # principal_multiples.py
# 
# from operaciones_multiples import Operaciones
# 
# def main():
#     op = Operaciones(15, 5)
#     print("Suma:", op.sumar())     # Output: Suma: 20
#     print("Resta:", op.restar())   # Output: Resta: 10
# 
# if __name__ == "__main__":
#     main()
# ```
# 
# **Ejecución:**
# 
# Al ejecutar `principal_multiples.py`, obtendrás:
# ```
# Suma: 20
# Resta: 10
# ```

# %% [markdown]
# ---
# 
# ## 8. Resumen de Conceptos Clave
# 
# 1. **Módulos en Python**:
#    - Archivos `.py` que contienen definiciones y declaraciones de Python.
#    - Permiten organizar y reutilizar código de manera eficiente.
#    - Se importan usando `import` o `from ... import ...`.
# 
# 2. **Paquetes en Python**:
#    - Directorios que contienen múltiples módulos y un archivo `__init__.py`.
#    - Facilitan la organización jerárquica del código.
#    - Se importan de manera similar a los módulos.
# 
# 3. **Importación de Módulos y Paquetes**:
#    - **Importar todo el módulo/paquete**: `import modulo` o `import paquete`.
#    - **Importar funciones, clases o variables específicas**: `from modulo import funcion`.
#    - **Usar alias** para evitar conflictos de nombres: `import modulo as mod`.
# 
# 4. **Buenas Prácticas**:
#    - **Organizar el Código**: Agrupar módulos relacionados en paquetes.
#    - **Nombres Claros y Descriptivos**: Facilitan la comprensión y el mantenimiento.
#    - **Documentar Módulos y Funciones**: Añadir docstrings para describir funcionalidades.
#    - **Evitar Importaciones Circulares**: Diseñar la estructura de módulos para evitar dependencias recursivas.
# 
# 5. **Manejo de Rutas de Importación**:
#    - **Rutas Absolutas**: Importaciones basadas en la estructura completa del proyecto.
#    - **Rutas Relativas**: Importaciones basadas en la ubicación del módulo actual dentro del paquete.
# 
# 6. **Reutilización de Código**:
#    - Crear módulos y paquetes facilita la reutilización de código en diferentes proyectos.
#    - Promueve la modularidad y la mantenibilidad del código.

# %% [markdown]
# ---
# 
# ## 9. Recomendaciones para los Estudiantes
# 
# - **Practicar la Creación de Módulos y Paquetes**: Intenta organizar tus proyectos en módulos y paquetes para mejorar la estructura y la mantenibilidad.
# 
# - **Documentar tu Código**: Añade docstrings y comentarios para describir la funcionalidad de tus módulos, clases y funciones.
# 
# - **Explorar la Biblioteca Estándar de Python**: Familiarízate con los módulos y paquetes incluidos en la biblioteca estándar de Python para aprovechar sus funcionalidades.
# 
# - **Evitar Importaciones Innecesarias**: Importa solo lo que necesitas para mantener el código limpio y eficiente.
# 
# - **Resolver Conflictos de Nombres**: Usa alias cuando importes módulos con nombres similares para evitar confusiones.
# 
# - **Leer la Documentación Oficial**: Consulta la [documentación oficial de Python sobre módulos](https://docs.python.org/3/tutorial/modules.html) y [paquetes](https://docs.python.org/3/tutorial/modules.html#packages) para profundizar en sus características y funcionalidades.
# 
# - **Participar en Proyectos Reales**: Aplica tus conocimientos en proyectos reales para entender mejor cómo organizar y reutilizar código de manera efectiva.
# 
# ---

# %% [markdown]
# ## 10. Conclusión
# 
# La comprensión de **paquetes** y **módulos** es esencial para cualquier programador de Python que desee desarrollar proyectos escalables y mantenibles. Al organizar el código en módulos y paquetes, no solo facilitas la reutilización y la colaboración, sino que también mejoras la legibilidad y la eficiencia de tus programas. Además, el manejo adecuado de la **importación** de múltiples archivos `.py` es crucial para evitar conflictos de nombres y garantizar un flujo de trabajo fluido en tus proyectos.
# 
# **¡Continúa practicando y fortaleciendo tus habilidades en Python!** La habilidad de organizar y reutilizar código mediante módulos y paquetes es una de las competencias clave para desarrolladores exitosos en el mundo de la programación.

# %% [markdown]
# ---
# 
# ## 11. Instrucciones para Convertir el Script de Python a Jupyter Notebook
# 
# 1. **Guardar el Script como Archivo `.py`**:
#    - Abre un editor de texto (como **VSCode**, **Sublime Text** o **Notepad++**).
#    - Copia el contenido proporcionado anteriormente.
#    - Guarda el archivo con un nombre descriptivo y la extensión `.py`, por ejemplo, `12_paquetes_modulos.py`.
# 
# 2. **Abrir el Archivo en VSCode (Recomendado)**:
#    - Si no tienes **Visual Studio Code (VSCode)**, descárgalo e instálalo desde [aquí](https://code.visualstudio.com/).
#    - Instala la extensión **Python** y la extensión **Jupyter** desde el marketplace de VSCode.
#    - Abre VSCode y abre el archivo `12_paquetes_modulos.py`.
# 
# 3. **Convertir el Script a Jupyter Notebook**:
#    - Una vez que el archivo está abierto en VSCode, verás que las marcas de celda (`# %% [markdown]` y `# %%`) están presentes.
#    - Haz clic en el ícono de "Convertir a Notebook" que aparece arriba de las celdas de código o markdown.
#    - VSCode generará un archivo de Jupyter Notebook (`.ipynb`) automáticamente.
# 
# 4. **Guardar el Notebook**:
#    - Después de la conversión, guarda el notebook en la ubicación deseada.
#    - Puedes renombrarlo si lo deseas, por ejemplo, `12_paquetes_modulos.ipynb`.
# 
# 5. **Abrir el Notebook en Jupyter Notebook o JupyterLab**:
#    - Abre **Jupyter Notebook** o **JupyterLab** desde tu terminal o a través de tu entorno de desarrollo.
#    - Navega hasta la ubicación donde guardaste `12_paquetes_modulos.ipynb` y ábrelo.
#    - Ahora podrás ver y ejecutar las celdas de markdown y código de manera interactiva.
# 
# 6. **Verificar y Ejecutar las Celdas**:
#    - Asegúrate de que todas las celdas se hayan importado correctamente.
#    - Ejecuta las celdas de código para probar los ejemplos y ejercicios.
#    - Edita el contenido si necesitas añadir, eliminar o modificar alguna sección o ejercicio.
# 
# 7. **Compartir el Notebook**:
#    - Una vez que hayas verificado el contenido, puedes compartir el archivo `.ipynb` con tus estudiantes a través de plataformas como **GitHub**, **Google Classroom**, **Moodle**, **Blackboard**, **correo electrónico**, etc.
# 
# ---
# 
# ## 12. Conclusión Final
# 
# El manejo adecuado de **paquetes** y **módulos** es una habilidad fundamental para cualquier desarrollador de Python. Te permite organizar tu código de manera lógica, reutilizar funcionalidades, y colaborar de manera más efectiva en proyectos grandes. Además, la capacidad de importar y utilizar múltiples archivos `.py` facilita la gestión y el mantenimiento de tus proyectos a medida que crecen en complejidad.
# 
# **¡Sigue practicando y perfeccionando tus habilidades en Python!** La estructuración eficiente de tu código mediante módulos y paquetes te permitirá desarrollar aplicaciones más robustas, escalables y fáciles de mantener.

# %% [markdown]
# ```

# %% [markdown]
# ## **Instrucciones para Utilizar el Contenido del Archivo 12 en Jupyter Notebook**
# 
# 1. **Guardar el Script como Archivo `.py`**:
#    - Abre un editor de texto (como **VSCode**, **Sublime Text** o **Notepad++**).
#    - Copia el contenido proporcionado anteriormente.
#    - Guarda el archivo con un nombre descriptivo y la extensión `.py`, por ejemplo, `12_paquetes_modulos.py`.
# 
# 2. **Abrir el Archivo en VSCode (Recomendado)**:
#    - Si no tienes **Visual Studio Code (VSCode)**, descárgalo e instálalo desde [aquí](https://code.visualstudio.com/).
#    - Instala la extensión **Python** y la extensión **Jupyter** desde el marketplace de VSCode.
#    - Abre VSCode y abre el archivo `12_paquetes_modulos.py`.
# 
# 3. **Convertir el Script a Jupyter Notebook**:
#    - Una vez que el archivo está abierto en VSCode, verás que las marcas de celda (`# %% [markdown]` y `# %%`) están presentes.
#    - Haz clic en el ícono de "Convertir a Notebook" que aparece arriba de las celdas de código o markdown.
#    - VSCode generará un archivo de Jupyter Notebook (`.ipynb`) automáticamente.
# 
# 4. **Guardar el Notebook**:
#    - Después de la conversión, guarda el notebook en la ubicación deseada.
#    - Puedes renombrarlo si lo deseas, por ejemplo, `12_paquetes_modulos.ipynb`.
# 
# 5. **Abrir el Notebook en Jupyter Notebook o JupyterLab**:
#    - Abre **Jupyter Notebook** o **JupyterLab** desde tu terminal o a través de tu entorno de desarrollo.
#    - Navega hasta la ubicación donde guardaste `12_paquetes_modulos.ipynb` y ábrelo.
#    - Ahora podrás ver y ejecutar las celdas de markdown y código de manera interactiva.
# 
# 6. **Verificar y Ejecutar las Celdas**:
#    - Asegúrate de que todas las celdas se hayan importado correctamente.
#    - Ejecuta las celdas de código para probar los ejemplos y ejercicios.
#    - Edita el contenido si necesitas añadir, eliminar o modificar alguna sección o ejercicio.
# 
# 7. **Compartir el Notebook**:
#    - Una vez que hayas verificado el contenido, guarda el notebook.
#    - Comparte el archivo `.ipynb` con tus estudiantes a través de plataformas como **GitHub**, **Google Classroom**, **Moodle**, **Blackboard**, **correo electrónico**, etc.
# 
# ---
# 
# ## **Conclusión**
# 
# Los **paquetes** y **módulos** son componentes esenciales para la organización y reutilización del código en Python. Dominar su creación y uso te permitirá desarrollar proyectos más estructurados, mantener un código limpio y eficiente, y facilitar la colaboración en equipos de desarrollo. Además, entender cómo importar y utilizar múltiples archivos `.py` es crucial para gestionar proyectos de cualquier tamaño y complejidad.
# 
# **¡Continúa practicando y fortaleciendo tus habilidades en Python!** La habilidad de organizar y reutilizar código mediante módulos y paquetes es una de las competencias clave para desarrolladores exitosos en el mundo de la programación.
# ```

# %% [markdown]
# ## **Instrucciones para Convertir el Script de Python a Jupyter Notebook**
# 
# 1. **Guardar el Script como Archivo `.py`**:
#    - Abre un editor de texto (como **VSCode**, **Sublime Text** o **Notepad++**).
#    - Copia el contenido proporcionado anteriormente.
#    - Guarda el archivo con un nombre descriptivo y la extensión `.py`, por ejemplo, `12_paquetes_modulos.py`.
# 
# 2. **Abrir el Archivo en VSCode (Recomendado)**:
#    - Si no tienes **Visual Studio Code (VSCode)**, descárgalo e instálalo desde [aquí](https://code.visualstudio.com/).
#    - Instala la extensión **Python** y la extensión **Jupyter** desde el marketplace de VSCode.
#    - Abre VSCode y abre el archivo `12_paquetes_modulos.py`.
# 
# 3. **Convertir el Script a Jupyter Notebook**:
#    - Una vez que el archivo está abierto en VSCode, verás que las marcas de celda (`# %% [markdown]` y `# %%`) están presentes.
#    - Haz clic en el ícono de "Convertir a Notebook" que aparece arriba de las celdas de código o markdown.
#    - VSCode generará un archivo de Jupyter Notebook (`.ipynb`) automáticamente.
# 
# 4. **Guardar el Notebook**:
#    - Después de la conversión, guarda el notebook en la ubicación deseada.
#    - Puedes renombrarlo si lo deseas, por ejemplo, `12_paquetes_modulos.ipynb`.
# 
# 5. **Abrir el Notebook en Jupyter Notebook o JupyterLab**:
#    - Abre **Jupyter Notebook** o **JupyterLab** desde tu terminal o a través de tu entorno de desarrollo.
#    - Navega hasta la ubicación donde guardaste `12_paquetes_modulos.ipynb` y ábrelo.
#    - Ahora podrás ver y ejecutar las celdas de markdown y código de manera interactiva.
# 
# 6. **Verificar y Ejecutar las Celdas**:
#    - Asegúrate de que todas las celdas se hayan importado correctamente.
#    - Ejecuta las celdas de código para probar los ejemplos y ejercicios.
#    - Edita el contenido si necesitas añadir, eliminar o modificar alguna sección o ejercicio.
# 
# 7. **Compartir el Notebook**:
#    - Una vez que hayas verificado el contenido, guarda el notebook.
#    - Comparte el archivo `.ipynb` con tus estudiantes a través de plataformas como **GitHub**, **Google Classroom**, **Moodle**, **Blackboard**, **correo electrónico**, etc.
# 
# ---
# 
# ## **Conclusión Final**
# 
# El manejo adecuado de **paquetes**, **módulos** y la **importación** de múltiples archivos `.py` es una habilidad fundamental para cualquier desarrollador de Python que aspire a crear proyectos organizados, mantenibles y escalables. Al dominar estos conceptos, podrás estructurar tus proyectos de manera lógica, reutilizar código de manera eficiente y colaborar más efectivamente en equipos de desarrollo. Además, aplicar buenas prácticas en la creación y uso de módulos y paquetes te permitirá escribir código limpio, legible y fácil de mantener.
# 
# **¡Sigue practicando y perfeccionando tus habilidades en Python!** La capacidad de organizar y reutilizar código mediante módulos y paquetes es una de las competencias clave para desarrolladores exitosos en el mundo de la programación.
# ```

# %% [markdown]
# ```

# %% [markdown]
# ## **Instrucciones para Utilizar el Contenido del Archivo 12 en Jupyter Notebook**
# 
# 1. **Guardar el Script como Archivo `.py`**:
#    - Abre un editor de texto (como **VSCode**, **Sublime Text** o **Notepad++**).
#    - Copia el contenido proporcionado anteriormente.
#    - Guarda el archivo con un nombre descriptivo y la extensión `.py`, por ejemplo, `12_paquetes_modulos.py`.
# 
# 2. **Abrir el Archivo en VSCode (Recomendado)**:
#    - Si no tienes **Visual Studio Code (VSCode)**, descárgalo e instálalo desde [aquí](https://code.visualstudio.com/).
#    - Instala la extensión **Python** y la extensión **Jupyter** desde el marketplace de VSCode.
#    - Abre VSCode y abre el archivo `12_paquetes_modulos.py`.
# 
# 3. **Convertir el Script a Jupyter Notebook**:
#    - Una vez que el archivo está abierto en VSCode, verás que las marcas de celda (`# %% [markdown]` y `# %%`) están presentes.
#    - Haz clic en el ícono de "Convertir a Notebook" que aparece arriba de las celdas de código o markdown.
#    - VSCode generará un archivo de Jupyter Notebook (`.ipynb`) automáticamente.
# 
# 4. **Guardar el Notebook**:
#    - Después de la conversión, guarda el notebook en la ubicación deseada.
#    - Puedes renombrarlo si lo deseas, por ejemplo, `12_paquetes_modulos.ipynb`.
# 
# 5. **Abrir el Notebook en Jupyter Notebook o JupyterLab**:
#    - Abre **Jupyter Notebook** o **JupyterLab** desde tu terminal o a través de tu entorno de desarrollo.
#    - Navega hasta la ubicación donde guardaste `12_paquetes_modulos.ipynb` y ábrelo.
#    - Ahora podrás ver y ejecutar las celdas de markdown y código de manera interactiva.
# 
# 6. **Verificar y Ejecutar las Celdas**:
#    - Asegúrate de que todas las celdas se hayan importado correctamente.
#    - Ejecuta las celdas de código para probar los ejemplos y ejercicios.
#    - Edita el contenido si necesitas añadir, eliminar o modificar alguna sección o ejercicio.
# 
# 7. **Compartir el Notebook**:
#    - Una vez que hayas verificado el contenido, guarda el notebook.
#    - Comparte el archivo `.ipynb` con tus estudiantes a través de plataformas como **GitHub**, **Google Classroom**, **Moodle**, **Blackboard**, **correo electrónico**, etc.
# 
# ---
# 
# ## **Conclusión**
# 
# Los **paquetes**, **módulos** y la **importación** de múltiples archivos `.py` son componentes esenciales para la organización y reutilización del código en Python. Dominar su creación y uso te permitirá desarrollar proyectos más estructurados, mantener un código limpio y eficiente, y facilitar la colaboración en equipos de desarrollo. Además, entender cómo importar y utilizar múltiples archivos `.py` es crucial para gestionar proyectos de cualquier tamaño y complejidad.
# 
