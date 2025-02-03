class Estudiante:
    def __init__(self, nombre, edad, carrera, telefono):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.telefono = telefono
    
    def mostrar_datos(self):
        return f"Nombre: {self.nombre} - Edad:{self.edad} -  Telefono:{self.telefono}"
    
    def get_pares_edad(self):
        listado = []
        for i in range(0, self.edad, 2):
            listado.append(i)
        return listado

    def get_contacto(self):
        return (self.telefono, self.nombre)

    def get_dicc_letras(self):
        dicc ={}
        for letra in self.nombre.lower():
            if letra != ' ':
                if letra in dicc:
                    dicc[letra] +=1
                else:
                    dicc[letra] =1
        return dicc

    def add_notas(self, notas_nuevas):
        self.notas = notas_nuevas

    def get_promedio(self):
        if(self.notas == None):
            print("ERROD: aun no agrega notas ")
        else:
            self.notas
            return promedio