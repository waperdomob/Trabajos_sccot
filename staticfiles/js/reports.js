var date_range= null;
var autor = null;
var curso = null;
var institucion = null;
var tipoTrabajo = null;

var select_autor = null;
var select_curso = null;
var select_institucion = null;
var select_tipoTrabajo = null;

let button = document.querySelector("#botonEnviar");

var date_now = new moment().format('YYYY-MM-DD');


function generarReporte() {
    select_autor = $('select[name="autor"]').val();
    select_curso = $('select[name="curso"]').val();
    select_institucion = $('select[name="institucion"]').val();
    select_tipoTrabajo = $('select[name="tipoTrabajo"]').val();

        
    console.log(select_curso)
    var parameters = {
        'action' : 'search_report',
        'autor':autor,
        'curso':curso,
        'institucion':institucion,
        'tipoTrabajo':tipoTrabajo,

    }
    
    parameters['autor'] = select_autor;
    parameters['curso'] = select_curso;
    parameters['institucion'] = select_institucion;
    parameters['tipoTrabajo'] = select_tipoTrabajo;
       
    console.log(parameters)

    tblSale = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        scrollX: true,        
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: parameters,
            dataSrc: ""
        },
        searching: false,
        /* order : false,
        paging: false,
        ordering: false,
        info: false,
        searching: false, */
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                text: 'Descargar Excel <i class="fas fa-file-excel"></i>',
                titleAttr: 'Excel',
                className: 'btn btn-success btn-flat btn-xs'
            },
            {
                extend: 'pdfHtml5',
                text: 'Descargar Pdf&nbsp;&nbsp;&nbsp; <i class="fas fa-file-pdf"></i>',
                titleAttr: 'PDF',
                className: 'btn btn-danger btn-flat btn-xs',
                download: 'open',
                orientation: 'landscape',
                pageSize: 'LEGAL',
                customize: function (doc) {
                    doc.styles = {
                        header: {
                            fontSize: 18,
                            bold: true,
                            alignment: 'center'
                        },
                        subheader: {
                            fontSize: 13,
                            bold: true
                        },
                        quote: {
                            italics: true
                        },
                        small: {
                            fontSize: 8
                        },
                        tableHeader: {
                            bold: true,
                            fontSize: 11,
                            color: 'white',
                            fillColor: '#2d4154',
                            alignment: 'center'
                        }
                    };
                    doc.content[1].margin = [0, 35, 0, 0];
                    doc.content[1].layout = {};
                    doc['footer'] = (function (page, pages) {
                        return {
                            columns: [
                                {
                                    alignment: 'left',
                                    text: ['Fecha de creación: ', {text: date_now}]
                                },
                                {
                                    alignment: 'right',
                                    text: ['página ', {text: page.toString()}, ' de ', {text: pages.toString()}]
                                }
                            ],
                            margin: 20
                        }
                    });

                }
            },
        ],

        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return  parseFloat(data).toFixed(2);
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}

$(function () {

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es',
    });
    $('select[name="autor"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_autor'
                }
                return queryParameters;
            },
            processResults: function (data) {
                //console.log(data);
                return {                        
                    results: data
                };
            },
        },
        placeholder: 'Ingrese un Nombre o apellido',
        minimumInputLength: 1,
    });
    $('select[name="curso"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_curso'
                }
                return queryParameters;
            },
            processResults: function (data) {
                //console.log(data);
                return {                        
                    results: data
                };
            },
        },
        placeholder: 'Ingrese un curso',
        minimumInputLength: 1,
    });
    $('select[name="institucion"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_inst'
                }
                return queryParameters;
            },
            processResults: function (data) {
                //console.log(data);
                return {                        
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una institución',
        minimumInputLength: 1,
    });

    $('#botonEnviar').click(function(){
        generarReporte();
        });
});

