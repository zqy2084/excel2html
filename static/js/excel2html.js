$(document).ready(function() {
    $('#table_test').DataTable( {
        processing: true,
        serverSide: false,
        ordering: true,
        searching: true,
        bFilter: true,
        paging: false,
        ajax: {
        url: "/data",
        dataSrc: "datas",
        columns: [
            { data: 0 },
            { data: 1 },
            { data: 2 },
            { data: 3 }
            ]
        }
    } );
} );
