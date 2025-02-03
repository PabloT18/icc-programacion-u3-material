
def obtener_ventas_iniciales():
    ventas = [10,110,200,140,89]
    return ventas

def agregar_venta(ventas, monto):
    if monto >0:
        ventas.append(monto)
        return True
    else:
        return False