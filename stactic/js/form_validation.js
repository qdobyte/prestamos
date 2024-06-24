document.addEventListener('DOMContentLoaded', function () {
    function validateForm(event, formId, validations) {
        const form = document.getElementById(formId);
        let isValid = true;

        validations.forEach(validation => {
            const field = form.querySelector(`#${validation.id}`);
            const pattern = validation.pattern;
            const message = validation.message;

            if (!pattern.test(field.value)) {
                alert(message);
                isValid = false;
                event.preventDefault();
            }
        });

        return isValid;
    }

    const studentForm = document.getElementById('studentForm');
    if (studentForm) {
        studentForm.addEventListener('submit', function (event) {
            validateForm(event, 'studentForm', [
                {
                    id: 'nombre_completo',
                    pattern: /^[A-Za-zÀ-ÿ\s]+$/,
                    message: 'El nombre completo solo puede contener letras y espacios, incluidas las tildes.'
                },
                {
                    id: 'documento_identificacion',
                    pattern: /^\d+$/,
                    message: 'El documento de identificación solo puede contener números.'
                },
                {
                    id: 'programa',
                    pattern: /^[A-Za-zÀ-ÿ\s]+$/,
                    message: 'El programa solo puede contener letras y espacios, incluidas las tildes.'
                }
            ]);
        });
    }

    const bookForm = document.getElementById('bookForm');
    if (bookForm) {
        bookForm.addEventListener('submit', function (event) {
            validateForm(event, 'bookForm', [
                {
                    id: 'nombre_autor',
                    pattern: /^[A-Za-zÀ-ÿ\s]+$/,
                    message: 'El nombre del autor solo puede contener letras y espacios, incluidas las tildes.'
                },
                {
                    id: 'lugar_nacimiento_autor',
                    pattern: /^[A-Za-zÀ-ÿ\s]+$/,
                    message: 'El lugar de nacimiento solo puede contener letras y espacios, incluidas las tildes.'
                },
                {
                    id: 'nombre_libro',
                    pattern: /^[A-Za-zÀ-ÿ\s0-9]+$/,
                    message: 'El nombre del libro solo puede contener letras, números y espacios, incluidas las tildes.'
                }
            ]);
        });
    }
});