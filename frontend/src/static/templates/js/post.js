$(document).ready(function() {
    // When page is loaded then replace \n with \r\n -> new line
    var body = document.getElementById('validationBody').value;
    body = body.replace(/\\n/g, '\r\n');
    document.getElementById("validationBody").value = body;
});

// https://getbootstrap.com/docs/5.0/forms/validation/?
(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                   event.preventDefault()
                   event.stopPropagation()
                }

            form.classList.add('was-validated')
        }, false)
    })
})()
