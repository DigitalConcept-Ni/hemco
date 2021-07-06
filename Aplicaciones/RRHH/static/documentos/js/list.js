// Funcion para mostrar el model informativo de la tabla consulta expediente

$(function () {
    $('.table').DataTable({
        deferRender: true,
        responsive: true,
        autoWidth: false,
        destroy: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_data'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "nombre"},
            {"data": "seccion"},
            {"data": "seccion"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                //orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/panelcentral/documentos/add/" type="button" class="btn btn-primary"><i class="fas fa-edit"></i></a>';
                    buttons += '<a href="/panelcentral/documentos/delete/'+row.id+'/" type="button" class="btn btn-danger"><i class="fas fa-trash"></i></a>';
                    return buttons;
                },
            },
        ],
        initComplete: function (settings, json) {
        }
    });

});