from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(100), nullable=False)
    documento_identificacion = db.Column(db.String(20), nullable=False)
    programa = db.Column(db.String(100), nullable=False)
    prestamos = db.relationship('Prestamo', backref='estudiante', lazy=True)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_autor = db.Column(db.String(100), nullable=False)
    fecha_nacimiento_autor = db.Column(db.Date, nullable=False)
    lugar_nacimiento_autor = db.Column(db.String(100), nullable=False)
    nombre_libro = db.Column(db.String(100), nullable=False)
    fecha_publicacion = db.Column(db.Date, nullable=False)
    prestamos = db.relationship('Prestamo', backref='libro', lazy=True)

class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.id'), nullable=False)
    libro_id = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    fecha_prestamo = db.Column(db.Date, nullable=False)
    fecha_devolucion = db.Column(db.Date, nullable=False)