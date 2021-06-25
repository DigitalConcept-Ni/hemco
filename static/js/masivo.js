// Funcion para mostrar el model informativo de la tabla consulta expediente

$(function () {
    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameter = $(this).serializeArray();
        console.log(parameter);

    });


});

