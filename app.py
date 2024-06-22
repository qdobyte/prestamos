import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
from models import db, Estudiante, Libro, Prestamo  # Importa db desde models.py

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la extensión SQLAlchemy con la aplicación Flask
db.init_app(app)

# Crea las tablas en la base de datos (si no existen)
with app.app_context():
    db.create_all()

# Rutas de la aplicación

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Rutas CRUD para estudiantes
@app.route('/students')
def list_students():
    students = Estudiante.query.all()
    return render_template('list_students.html', students=students)

@app.route('/students/new', methods=['GET', 'POST'])
def new_student():
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        documento_identificacion = request.form['documento_identificacion']
        programa = request.form['programa']
        student = Estudiante(nombre_completo=nombre_completo, documento_identificacion=documento_identificacion, programa=programa)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('list_students'))
    return render_template('new_student.html')

@app.route('/students/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Estudiante.query.get(id)
    if student is None:
        return 'Estudiante no encontrado', 404

    if request.method == 'POST':
        student.nombre_completo = request.form['nombre_completo']
        student.documento_identificacion = request.form['documento_identificacion']
        student.programa = request.form['programa']
        db.session.commit()
        return redirect(url_for('list_students'))

    return render_template('edit_student.html', student=student)

@app.route('/students/delete/<int:id>')
def delete_student(id):
    student = Estudiante.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
    return redirect(url_for('list_students'))

# Rutas CRUD para libros
@app.route('/books')
def list_books():
    books = Libro.query.all()
    return render_template('list_books.html', books=books)

@app.route('/books/new', methods=['GET', 'POST'])
def new_book():
    if request.method == 'POST':
        nombre_autor = request.form['nombre_autor']
        fecha_nacimiento_autor = request.form['fecha_nacimiento_autor']
        lugar_nacimiento_autor = request.form['lugar_nacimiento_autor']
        nombre_libro = request.form['nombre_libro']
        fecha_publicacion = request.form['fecha_publicacion']
        book = Libro(
            nombre_autor=nombre_autor,
            fecha_nacimiento_autor=datetime.strptime(fecha_nacimiento_autor, '%Y-%m-%d'),
            lugar_nacimiento_autor=lugar_nacimiento_autor,
            nombre_libro=nombre_libro,
            fecha_publicacion=datetime.strptime(fecha_publicacion, '%Y-%m-%d')
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('list_books'))
    return render_template('new_book.html')

@app.route('/books/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Libro.query.get(id)
    if book is None:
        return 'Libro no encontrado', 404

    if request.method == 'POST':
        book.nombre_autor = request.form['nombre_autor']
        book.fecha_nacimiento_autor = datetime.strptime(request.form['fecha_nacimiento_autor'], '%Y-%m-%d')
        book.lugar_nacimiento_autor = request.form['lugar_nacimiento_autor']
        book.nombre_libro = request.form['nombre_libro']
        book.fecha_publicacion = datetime.strptime(request.form['fecha_publicacion'], '%Y-%m-%d')
        db.session.commit()
        return redirect(url_for('list_books'))

    return render_template('edit_book.html', book=book)

@app.route('/books/delete/<int:id>')
def delete_book(id):
    book = Libro.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('list_books'))

# Rutas CRUD para préstamos

@app.route('/loans')
def list_loans():
    loans = Prestamo.query.all()
    return render_template('list_loans.html', loans=loans)

@app.route('/loans/new', methods=['GET', 'POST'])
def new_loan():
    if request.method == 'POST':
        student_id = int(request.form['student_id'])
        book_id = int(request.form['book_id'])
        loan_date = request.form['loan_date']
        due_date = request.form['due_date']

        student = Estudiante.query.get(student_id)
        book = Libro.query.get(book_id)

        if student and book:
            loan = Prestamo(
                estudiante_id=student_id,
                libro_id=book_id,
                fecha_prestamo=datetime.strptime(loan_date, '%Y-%m-%d'),
                fecha_devolucion=datetime.strptime(due_date, '%Y-%m-%d')
            )
            db.session.add(loan)
            db.session.commit()
            return redirect(url_for('list_loans'))

    students = Estudiante.query.all()
    books = Libro.query.all()
    return render_template('new_loan.html', students=students, books=books)

@app.route('/loans/edit/<int:id>', methods=['GET', 'POST'])
def edit_loan(id):
    loan = Prestamo.query.get_or_404(id)
    if request.method == 'POST':
        loan.estudiante_id = int(request.form['student_id'])
        loan.libro_id = int(request.form['book_id'])
        loan.fecha_prestamo = datetime.strptime(request.form['loan_date'], '%Y-%m-%d')
        loan.fecha_devolucion = datetime.strptime(request.form['due_date'], '%Y-%m-%d')

        db.session.commit()
        return redirect(url_for('list_loans'))
    
    students = Estudiante.query.all()
    books = Libro.query.all()
    return render_template('edit_loan.html', loan=loan, students=students, books=books)

@app.route('/loans/delete/<int:id>', methods=['POST'])
def delete_loan(id):
    loan = Prestamo.query.get_or_404(id)
    db.session.delete(loan)
    db.session.commit()
    return redirect(url_for('list_loans'))

if __name__ == "__main__":
    app.run(debug=True)