$(function () {
    $('.table').DataTable({
        responsive: true,
        autoWidth: false,
        detroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_user',
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "usuario"},
            {"data": "colaborador"},
            {"data": "correo"},
            {"data": "date_joined"},
            {"data": "date_joined"},
        ],
        columnDefs: [
            {
                targets: [-1],
                //class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/user/update/' + row.id + '/" type="button" class="btn btn-primary"><i class="fas fa-edit"></i></a>';
                    buttons += '<a href="/user/delete/' + row.id + '/" type="button" class="btn btn-danger"><i class="fas fa-trash"></i></a>';
                    return buttons;
                },
            },
        ],
        initComplete: function (settings, json) {
        }
    });

})
