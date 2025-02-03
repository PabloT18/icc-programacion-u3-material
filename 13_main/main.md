### **Explicación detallada de `if __name__ == "__main__": main()`**

Esta línea de código es un **patrón estándar en Python** que se utiliza para definir el punto de entrada de un programa. Permite que un script sea usado tanto como un **programa ejecutable** como un **módulo importable** en otro código.

---

## **1. Entendiendo `__name__` en Python**
En Python, cada archivo (script) tiene un **atributo especial** llamado `__name__`.  
Este atributo tiene diferentes valores dependiendo de cómo se ejecuta el archivo:

1. **Si el archivo se ejecuta directamente como un programa**, Python asigna a `__name__` el valor `"__main__"`.
2. **Si el archivo se importa como un módulo en otro script**, `__name__` tomará el nombre del archivo sin la extensión `.py`.

Ejemplo para entender `__name__`:

```python
# archivo: ejemplo.py
print("El valor de __name__ es:", __name__)
```

### **Caso 1: Ejecutando el archivo directamente**
```bash
python main.py
```
**Salida en consola:**
```plaintext
El valor de __name__ es: __main__
```

### **Caso 2: Importando el archivo en otro script**
```python
# archivo: otro_script.py
import main
```
**Salida en consola:**
```plaintext
El valor de __name__ es: main
```
Aquí `__name__` tiene el valor `"ejemplo"`, es decir, el nombre del archivo.

---

## **2. ¿Por qué usamos `if __name__ == "__main__":`?**

El uso de `if __name__ == "__main__":` permite que ciertas partes del código **solo se ejecuten cuando el script es ejecutado directamente**, pero no cuando se importa en otro archivo.

Ejemplo:

```python
# archivo: main.py
def main():
    print("Este es el punto de entrada del programa.")

if __name__ == "__main__":
    main()
```

### **Caso 1: Ejecutando `mi_script.py` directamente**
```bash
python mi_script.py
```
**Salida en consola:**
```plaintext
Este es el punto de entrada del programa.
```

### **Caso 2: Importando `mi_script.py` en otro script**
```python
# archivo: otro_archivo.py
import mi_script
print("Este es otro script que usa mi_script.py")
```
**Salida en consola:**
```plaintext
Este es otro script que usa mi_script.py
```
Aquí la función `main()` **NO se ejecutó automáticamente**, porque el archivo fue **importado** en lugar de ejecutado directamente.

---

## **3. ¿Qué hace exactamente `if __name__ == "__main__": main()`?**
Cuando un archivo Python es ejecutado:

1. Python asigna a `__name__` el valor `"__main__"` si el archivo se ejecuta directamente.
2. La condición `if __name__ == "__main__":` evalúa si `__name__` es `"__main__"`.
3. Si la condición es **verdadera**, ejecuta la función `main()`.
4. Si el script se importa en otro archivo, **la condición no se cumple** y la función `main()` **NO se ejecuta automáticamente**.

---

## **4. ¿Qué pasaría si no usamos `if __name__ == "__main__":`?**
Si no usamos esta estructura, el código en `main.py` se ejecutaría **cada vez que se importe** en otro script, lo cual puede no ser deseado.

Ejemplo sin `if __name__ == "__main__":`:
```python
# archivo: sin_main.py
def main():
    print("Este es el punto de entrada del programa.")

main()  # Se ejecuta sin importar cómo se use el archivo
```

Si ejecutamos:
```bash
python sin_main.py
```
**Salida en consola:**
```plaintext
Este es el punto de entrada del programa.
```

Pero si importamos `sin_main.py` en otro archivo:
```python
import sin_main
```
**Salida en consola (indeseada en muchos casos):**
```plaintext
Este es el punto de entrada del programa.
```
Aquí `main()` se ejecutó **automáticamente al importar el módulo**, lo cual no suele ser el comportamiento esperado.

Por eso usamos `if __name__ == "__main__":`, para evitar ejecuciones no deseadas.

---

## **5. Resumen**
✅ `if __name__ == "__main__": main()` asegura que el código dentro **solo se ejecute cuando el script es ejecutado directamente**.  
✅ Si el archivo se **importa en otro código**, la función `main()` **NO se ejecuta automáticamente**.  
✅ Esto ayuda a mantener el código modular y reutilizable en diferentes contextos.

---

## **6. Aplicación en `main.py` del ejercicio**
En el ejercicio que te di:

```python
# main.py

import operaciones

def main():
    print("=== INICIO DEL PROGRAMA ===\n")
    
    ventas = operaciones.obtener_ventas_iniciales()
    print("Ventas iniciales:", ventas)

    # Otras operaciones...

    print("\n=== FIN DEL PROGRAMA ===")

if __name__ == "__main__":
    main()
```

🔹 Si ejecutas **`python main.py`**, la función `main()` se ejecutará.  
🔹 Si importas `main.py` en otro archivo, su contenido **no se ejecutará automáticamente**.

Esto permite que `operaciones.py` pueda ser reutilizado en otros programas sin ejecutar `main.py` innecesariamente.

---

### **Conclusión**
El uso de `if __name__ == "__main__": main()` es una **buena práctica** en Python para escribir código modular, reutilizable y evitar ejecuciones no deseadas al importar módulos. 🚀


## **Ejercicio: "Gestión de Ventas y Cálculos"**

El objetivo es gestionar una lista de ventas y realizar diversas operaciones como:

1. **Obtener una lista inicial de ventas.**  
2. **Agregar una nueva venta a la lista.**  
3. **Calcular el total de ventas.**  
4. **Obtener la venta más alta y la más baja.**  
5. **Filtrar ventas superiores a un umbral.**  
6. **Determinar si todas las ventas superan un mínimo.**

---

### **Explicación de funciones**

1. **`obtener_ventas_iniciales()`**  
   - Devuelve una lista solo de valores con 5 ventas predefinidas.  Ejm [100,120]

2. **`agregar_venta(ventas, monto)`**  
   - Agrega una venta nueva si es positiva.
   - Lanza `ValueError` si el monto es menor o igual a 0.
   - Retorna True o False segun sea el caso
   - en `main` si es True imprime las ventas; si es False imprime Error al ingresar monto

3. **`calcular_total_ventas(ventas)`**  
   - Suma todas las ventas y devuelve el total.

4. **`obtener_venta_max_min(ventas)`**  
   - Retorna la venta más alta y la más baja, como tupla.

5. **`filtrar_ventas_mayores_a(ventas, umbral)`**  
   - Devuelve una lista con las ventas que superan un umbral dado.

6. **`todas_superan(ventas, minimo)`**  
   - Retorna `True` si todas las ventas son mayores o iguales a un mínimo.


7. **Método que Devuelve un Diccionario: `clasificar_montos(lista)`**
- **Descripción**: Recibe una lista de números y los clasifica en un **diccionario con claves definidas**:
  - `"pares"`: Todos los números pares.
  - `"impares"`: Todos los números impares.
  - `"divisibles_por_2"`: Números divisibles entre 2.
  - `"divisibles_por_3"`: Números divisibles entre 3.

  **Salida esperada:**
  ```plaintext
  {
      'pares': [10, 20, 30, 40],
      'impares': [15, 25, 35, 45],
      'divisibles_por_2': [10, 20, 30, 40],
      'divisibles_por_3': [15, 30, 45]
  }
  ```
---