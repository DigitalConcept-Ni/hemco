// Funcion para mostrar el model informativo de la tabla consulta expediente

$(function () {
    $('#btn_query').on('click', function (e) {
        var cedula = $('select[name="Cedula"]').val()
        var seccion = $('select[name="Secciones"]').val()

        if (cedula === '') {
            alert('Seleccione un colaborador')
        } else if (seccion === '') {
            alert('Selecciones una seccion')
        } else {
            $('#tableInfoIndexado').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                deferRender: true,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'query',
                        'cedula': cedula,
                        'seccion': seccion
                    },
                    dataSrc: ""
                },
                columns: [
                    {"data": "cedula"},
                    {"data": "seccion.nombre"},
                    {"data": "seccion.tipo_documento"},
                    {"data": "documento.nombre"},
                    {"data": "fecha_documento"},
                    {"data": "cedula.departamento"},//Referencia al departamento
                    {"data": "cedula.contrato"},//Referencia al tipo de contrato
                    {"data": "cedula.estado"},//Referencia al estado del personal
                    {"data": "archivo"},
                ],
                columnDefs: [
                    {
                        targets: [-9],//Cedula
                        class: 'text-center',
                        //orderable: false,
                        render: function (data, type, row) {
                            var datos = data.primer_nombre + ' ' + data.segundo_nombre + ' ' + data.apellido_paterno + ' ' + data.apellido_materno;
                            return datos;
                        }
                    },
                    {
                        targets: [-8, -7, -6, -5, -4, -3, -2],
                        class: 'text-center',
                        orderable: false,

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

        }

    });


});
