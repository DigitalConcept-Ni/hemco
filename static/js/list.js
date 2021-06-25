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
                        // {"data": "cedula"},
                        {"data": "seccion"},
                        {"data": "documento"},
                        // {"data": "departamento"},
                        // {"data": "contrato"},
                        // {"data": "estado"},
                        {"data": "archivo"},
                    ],
                    columnDefs: [
                        {
                            targets: [-5],
                            class: 'text-center',
                            //orderable: false,
                            render: function (data, type, row) {
                                var datos = data.primer_nombre+' '+ data.segundo_nombre+' '+ data.apellido_paterno+' '+ data.apellido_materno;
                                return type;
                            }
                        },
                        {
                            targets: [-4],
                            class: 'text-center',
                            //orderable: false,
                            render: function (data, type, row) {
                                var datos = data.nombre
                                return datos;

                            }
                        },

                        {
                            targets: [-3],
                            class: 'text-center',
                            //orderable: false,
                            render: function (data, type, row) {
                                var datos = data.nombre
                                return datos;
                            }
                        },
                        {
                            targets: [-1],
                            class: 'text-center',
                            orderable: false,
                            render: function (data, type, row) {
                                var buttons = '<a href="/media/' + data + '" >' + data + '</a> ';
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
