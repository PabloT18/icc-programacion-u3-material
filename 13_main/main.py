import operaciones 
def inicio():
    ventas = operaciones.obtener_ventas_iniciales()
    print(ventas)

    respuesta = operaciones.agregar_venta(ventas, 10)
    show_message(respuesta, ventas,"Error al ingresar monto" )
    respuesta = operaciones.agregar_venta(ventas, -15)
    show_message(respuesta, ventas,"Error al ingresar monto" )

def show_message(condicion, valor, mensaje_error):
    if condicion:
        print(valor)
    else:
        print(mensaje_error)



if __name__ == "__main__":
    inicio()