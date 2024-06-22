from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
from models import Estudiante, Libro, Prestamo 

app = Flask(__name__)

# Datos simulados para estudiantes, libros y préstamos
students = []
books = []
loans = []

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
    return render_template('list_students.html', students=students)

@app.route('/students/new', methods=['GET', 'POST'])
def new_student():
    if request.method == 'POST':
        # Procesar datos del formulario para crear un nuevo estudiante
        nombre_completo = request.form['nombre_completo']
        documento_identificacion = request.form['documento_identificacion']
        programa = request.form['programa']
        student = Estudiante(nombre_completo, documento_identificacion, programa)
        students.append(student)
        return redirect(url_for('list_students'))
    return render_template('new_student.html')

@app.route('/students/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = next((student for student in students if student.id == id), None)
    if student is None:
        return 'Estudiante no encontrado', 404

    if request.method == 'POST':
        student.nombre_completo = request.form['nombre_completo']
        student.documento_identificacion = request.form['documento_identificacion']
        student.programa = request.form['programa']
        return redirect(url_for('list_students'))

    return render_template('edit_student.html', student=student)

@app.route('/students/delete/<int:id>')
def delete_student(id):
    global students
    students = [student for student in students if student.id != id]   
    return redirect(url_for('list_students'))

# Rutas CRUD para libros
@app.route('/books')
def list_books():
    return render_template('list_books.html', books=books)

@app.route('/books/new', methods=['GET', 'POST'])
def new_book():
    if request.method == 'POST':
        nombre_autor = request.form['nombre_autor']
        fecha_nacimiento_autor = request.form['fecha_nacimiento_autor']
        lugar_nacimiento_autor = request.form['lugar_nacimiento_autor']
        nombre_libro = request.form['nombre_libro']
        fecha_publicacion = request.form['fecha_publicacion']
        book = Libro(nombre_autor, fecha_nacimiento_autor, lugar_nacimiento_autor, nombre_libro, fecha_publicacion)
        books.append(book)
        return redirect(url_for('list_books'))
    return render_template('new_book.html')

@app.route('/books/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = next((book for book in books if book.id == id), None)
    if book is None:
        return 'Libro no encontrado', 404

    if request.method == 'POST':
        book.nombre_autor = request.form['nombre_autor']
        book.fecha_nacimiento_autor = datetime.strptime(request.form['fecha_nacimiento_autor'], '%Y-%m-%d')
        book.lugar_nacimiento_autor = request.form['lugar_nacimiento_autor']
        book.nombre_libro = request.form['nombre_libro']
        book.fecha_publicacion = datetime.strptime(request.form['fecha_publicacion'], '%Y-%m-%d')
        return redirect(url_for('list_books'))

    return render_template('edit_book.html', book=book)

@app.route('/books/delete/<int:id>')
def delete_book(id):
    global books
    books = [book for book in books if book.id != id]
    return redirect(url_for('list_books'))

# Rutas CRUD para préstamos

@app.route('/loans')
def list_loans():
    return render_template('list_loans.html', loans=loans)

@app.route('/loans/new', methods=['GET', 'POST'])
def new_loan():
    if request.method == 'POST':
        # Procesar datos del formulario para crear un nuevo préstamo
        student_id = int(request.form['student_id'])
        book_id = int(request.form['book_id'])
        loan_date = request.form['loan_date']
        due_date = request.form['due_date']

        # Obtener el objeto Estudiante y Libro correspondientes
        student = next((s for s in students if s.id == student_id), None)
        book = next((b for b in books if b.id == book_id), None)

        if student and book:
            # Crear instancia de Prestamo y agregarlo a la lista de préstamos
            loan = {
                'id': len(loans) + 1,  # Generar un ID único para el préstamo
                'student': student,
                'book': book,
                'loan_date': loan_date,
                'due_date': due_date
            }
            loans.append(loan)

            return redirect(url_for('list_loans'))

    # Obtener datos necesarios para el formulario (estudiantes y libros disponibles)
    return render_template('new_loan.html', students=students, books=books, loans=loans)


if __name__ == "__main__":
    app.run(debug=True)