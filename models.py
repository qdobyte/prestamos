from datetime import datetime, timedelta

class Estudiante:
    contador_id = 1  # Atributo de clase para llevar el contador de IDs

    def __init__(self, nombre_completo, documento_identificacion, programa):
        self.id = Estudiante.contador_id  # Asignación de ID único
        Estudiante.contador_id += 1  # Incremento del contador para el próximo ID
        self.nombre_completo = nombre_completo
        self.documento_identificacion = documento_identificacion
        self.programa = programa

    def __repr__(self):
        return f'Estudiante(id={self.id}, nombre_completo={self.nombre_completo}, documento_identificacion={self.documento_identificacion}, programa={self.programa})'

class Libro:
    contador_id = 1  # Atributo de clase para llevar el contador de IDs

    def __init__(self, nombre_autor, fecha_nacimiento_autor, lugar_nacimiento_autor, nombre_libro, fecha_publicacion):
        self.id = Libro.contador_id  # Asignación de ID único
        Libro.contador_id += 1  # Incremento del contador para el próximo ID
        self.nombre_autor = nombre_autor
        self.fecha_nacimiento_autor = datetime.strptime(fecha_nacimiento_autor, '%Y-%m-%d')
        self.lugar_nacimiento_autor = lugar_nacimiento_autor
        self.nombre_libro = nombre_libro
        self.fecha_publicacion = datetime.strptime(fecha_publicacion, '%Y-%m-%d')

    def __str__(self):
        return f'Libro: {self.nombre_libro} por {self.nombre_autor}, Publicado: {self.fecha_publicacion.date()}, Lugar de nacimiento del autor: {self.lugar_nacimiento_autor}, ID: {self.id}'

class Prestamo:
    contador_id = 1  # Atributo de clase para llevar el contador de IDs

    def __init__(self, estudiante, libro, fecha_prestamo, dias_devolucion):
        self.id = Prestamo.contador_id  # Asignación de ID único
        Prestamo.contador_id += 1  # Incremento del contador para el próximo ID
        self.estudiante = estudiante
        self.libro = libro
        self.fecha_prestamo = datetime.strptime(fecha_prestamo, '%Y-%m-%d')
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=dias_devolucion)

    def __str__(self):
        return (f'Prestamo:\nID: {self.id}\nEstudiante: {self.estudiante.nombre_completo}\nLibro: {self.libro.nombre_libro}\n'
                f'Fecha de Prestamo: {self.fecha_prestamo.date()}\nFecha de Devolución: {self.fecha_devolucion.date()}')
