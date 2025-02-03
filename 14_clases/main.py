
# import estudiante as est 
from estudiante import Estudiante

estudiante  = Estudiante('Pablo Andres Torres', 29, 'ICC', '12345')
datos = estudiante.mostrar_datos()
print(datos)

# contacto = estudiante.get_contacto()
telefono, nombre, = estudiante.get_contacto()
print(f"Nombre = {nombre}\nTelefono = {telefono}")


# Metodo en clase estudiante que retorne un
# listado con los numeros pares desde 0 
# hasta su esdad
# NOTA: el listado sera impreso en main.py
# get_pares_edad()

# Metodo en clase estudiante que retorne una 
# tupla con el numero de telefono y nombre 
# en este oreden
# En Main imprimiero 
#    Nombre = nombre_del_estudiante
#    Telefono = telefono_del_estudiante
# get_contacto()

# Metodo que me DEVUELVE un DICCIONARIO, donde las claves sean
# las letras del nombre y el valor la canitdad de las mismas 
# Para Pablop
# Main se imprime:
#    {
#       "p":2,
#       "a":1,
#       "b":1,
#     }
#  get_dicc_letras()
dicc = estudiante.get_dicc_letras()
for letra in dicc.items():
    print(letra)


# 1. crea un metodo add_notas(notas)
#    donde notas sea un listado de 10 notas hasta 100
# 2 Crea un metodo que devuelva la nota mas alta
# 3 Crea un metodo que devuelva el promedio 
# 4 Metodo que devuelva un listado de notas menores a un parametro
#   se lamama get_notas_bajas(minimo)
#   minimo sera 70
estudiante.add_notas([99,98,65,34,50,78,90])
