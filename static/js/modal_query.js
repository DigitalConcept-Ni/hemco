// Funcion para mostrar el model informativo de la tabla consulta expediente
$(function () {
    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameter = $(this).serializeArray();
        console.log(parameter);

        $('#tableInfoIndexado').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: parameter,
                dataSrc: ""
            },
            columns: [
                {"data": "cedula"},
                {"data": "seccion"},
                {"data": "documento"},
                {"data": "fecha_documento"},
                {"data": "cedula"},//Referencia al departamento
                {"data": "cedula"},//Referencia al tipo de contrato
                {"data": "cedula"},//Referencia al estado del personal
                {"data": "archivo"},
            ],
            columnDefs: [
                {
                    targets: [-8],//Cedula
                    class: 'text-center',
                    //orderable: false,
                    render: function (data, type, row) {
                        var datos = data.primer_nombre + ' ' + data.segundo_nombre + ' ' + data.apellido_paterno + ' ' + data.apellido_materno;
                        return datos;
                    }
                },
                {
                    targets: [-7],//Seccion
                    class: 'text-center',
                    //orderable: false,
                    render: function (data, type, row) {
                        var datos = data.nombre
                        return datos;

                    }
                },
                {
                    targets: [-6],//Documento
                    class: 'text-center',
                    //orderable: false,
                    render: function (data, type, row) {
                        var datos = data.nombre
                        return datos;

                    }
                },

                {
                    targets: [-4],//Estado del personal(Activo - Inactivo)
                    class: 'text-center',
                    //orderable: false,
                    render: function (data, type, row) {
                        var datos = data.departamento
                        return datos;
                    }
                },
                {
                    targets: [-3],//Estado del departamento
                    class: 'text-center',
                    //orderable: false,
                    render: function (data, type, row) {
                        var datos = data.contrato
                        return datos;
                    }
                },
                {
                    targets: [-2],//Estado del personal(Activo - Inactivo)
                    class: 'text-center',
                    //orderable: false,
                    render: function (data, type, row) {
                        var datos = data.estado
                        return datos;
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="/media/' + data + '" >' + data + '</a> ';
                        // var buttons = '<embed href="' + row.archivo + '" type="application/pdf" width="600" height="500" >';
                        return buttons;
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });
        $('#modalInfo').modal('show');

    });


});
