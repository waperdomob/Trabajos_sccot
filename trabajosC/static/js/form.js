var select_autor = $('select[name="Autor_correspondencia"]');
var select_autores = $('select[name="otros_autores"]');
let opciones = document.getElementById('id_tipo_trabajo')
let cajaTexto = document.getElementById("tabla")

const MAXIMO_TAMANIO_BYTES = 2000000; // 1MB = 1 millón de bytes

var trabajo={
    items : {
        tipo_trabajo: '',
        titulo : '',
        Autor_correspondencia:'',
        otros_autores :[],
        observaciones : '',
        institucion_principal: '',
        otras_instituciones : [],
        resumen_esp : '',
        palabras_claves: '',
        resumen_ingles : '',
        keywords: '',
        curso: '',
        manuscritos : [],
        tablas : []
    },
}
function submit_with_ajax(url, title, content, parameters, callback) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url: url, //window.location.pathname
                        type: 'POST',
                        data: parameters,
                        dataType: 'json',
                        processData: false,
                        contentType: false,
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback(data);
                            return false;
                        }
                        message_error(data.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    }).always(function (data) {

                    });
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    })
}
function submit_trabajo_with_ajax(url, title, content, parameters, callback) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url: url, //window.location.pathname
                        type: 'POST',
                        data: parameters,
                        enctype: 'multipart/form-data',
                        processData: false,
                        contentType: false,
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback(data);
                            return false;
                        }
                        message_error(data.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    }).always(function (data) {

                    });
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    })
}
    $(function () {
        $('#id_tipo_trabajo').on('change',function(){
            var selectValor = $(this).val();    
            if (selectValor === 'E-poster') {
                $('#id_tabla').prop('hidden', true);
                $('#tablaLabel_id').prop('hidden', true);
                $('#subtipoLabel_id').prop('hidden', true);
                $('#id_subtipo_trabajo').prop('hidden', true);


            }else {
              $('#id_tabla').prop('hidden', false);
              $('#tablaLabel_id').prop('hidden', false);
              $('#subtipoLabel_id').prop('hidden', false);
              $('#id_subtipo_trabajo').prop('hidden', false);


            }
        });
        $('#id_curso').on('change',function(){
            var selectValor = $(this).val();
            const csrf2 = document.getElementsByName('csrfmiddlewaretoken')[0].value

            $.ajax({
                delay: 250,
                type: 'POST',
                url: window.location.pathname,
                data: {curso_id: selectValor, action:'search_curso' },
                
                success: function (data) {
                    if (data['error']) {
                        alert(data['error']);
                        $('#botonEnviar').prop('hidden', true);
                        $('#botonEnviar').prop('disabled', true);

                    }
                    else{
                        $('#botonEnviar').prop('hidden', false);
                        $('#botonEnviar').prop('disabled', false);

                    }
                    return {                        
                        results: data
                    };
                    
                },
                error: function(data) {

                    alert(data);
                    $('#observaciones').val("");
                   }
              }) 
        });
        $('.select2').select2({
            theme: "bootstrap4",
            language: 'es',
            allowClear: true,
        });
        $('select[name="Autor_correspondencia"]').select2({
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
            minimumInputLength: 3,
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
                    return {                        
                        results: data
                    };
                },
            },
            placeholder: 'Ingrese un Nombre o apellido',
            minimumInputLength: 3,
        });
        $('#Autor_form1').on('submit', function (e) {
            e.preventDefault();
            var parameters = new FormData(this);
            parameters.append('action', 'create_autor1');
            submit_with_ajax(window.location.pathname, 'Notificación',
                '¿Estas seguro de crear al siguiente Autor?', parameters, function (response) {
                    //console.log(response);
                    var newOption = new Option(response.full_name, response.id, false, true);
                    $('select[name="Autor_correspondencia"]').append(newOption).trigger('change');
                    $('select[name="autor"]').append(newOption).trigger('change');

                    $('#autoresModal').modal('hide');
                });
        });

        $('#Autor_form2').on('submit', function (e) {
            e.preventDefault();
            var parameters = new FormData(this);
            parameters.append('action', 'create_autor2');
            submit_with_ajax(window.location.pathname, 'Notificación',
                '¿Estas seguro de registrar al siguiente Autor?', parameters, function (response) {
                    console.log(response);
                    var newOption = new Option(response.full_name, response.id, false, true);
                    $('select[name="Autor_correspondencia"]').append(newOption).trigger('change');
                    $('select[name="autor"]').append(newOption).trigger('change');

                    $('#autoresModal2').modal('hide');
                });
        });

        $('#trabajo_form').on('submit', function (e) {
            e.preventDefault();    
            trabajo.items.tipo_trabajo = $('select[name="tipo_trabajo"]').val();
            trabajo.items.titulo = $('input[name="titulo"]').val();
            trabajo.items.Autor_correspondencia = $('select[name="Autor_correspondencia"]').val();
            trabajo.items.otros_autores = $('select[name="autor"]').val();
            trabajo.items.observaciones = $('input[name="observaciones"]').val();
            trabajo.items.institucion_principal = $('input[name="institucion_principal"]').val();
            trabajo.items.otras_instituciones = $('select[name="institucion"]').val();
            trabajo.items.resumen_esp = $('input[name="resumen_esp"]').val();
            trabajo.items.palabras_claves = $('input[name="palabras_claves"]').val();
            trabajo.items.resumen_ingles = $('input[name="resumen_ingles"]').val();
            trabajo.items.keywords = $('input[name="keywords"]').val();
            trabajo.items.curso = $('select[name="curso"]').val();

            var archivos = [];
            var archivos2 = [];
            var ext =[];
            var contador = 0;
            const tamManus = $('input[name="manuscrito"]').get(0).files.length;
            const tamTablas = $('input[name="tabla"]').get(0).files.length;
            
            for (var i = 0; i < tamManus; ++i) {
                archivos.push($('input[name="manuscrito"]').get(0).files[i]);
                ext[i] = archivos[i].name.split('.').pop();
                ext[i] = ext[i].toLowerCase();
                if (archivos[i].size > MAXIMO_TAMANIO_BYTES) {
                    const tamanioEnMb = MAXIMO_TAMANIO_BYTES / 1000000;
                    alert(`El tamaño máximo del archivo ${archivos[i].name} debe ser menor a ${tamanioEnMb} MB`);
                    contador ++;
                }
                
                else if (ext[i] === "docx" ||  ext[i] === "doc") {
                    trabajo.items.manuscritos.push($('input[name="manuscrito"]').get(0).files[i].name);
                    
                } 
                else{
                    alert(`El  archivo ${archivos[i].name} debe ser documento word`);
                    contador ++;
                }
            };
            for (var i = 0; i < tamTablas; ++i) {
                archivos2.push($('input[name="tabla"]').get(0).files[i]);
                ext[i] = archivos2[i].name.split('.').pop();
                ext[i] = ext[i].toLowerCase();
                if (archivos2[i].size > MAXIMO_TAMANIO_BYTES) {
                    const tamanioEnMb = MAXIMO_TAMANIO_BYTES / 1000000;
                    alert(`El tamaño máximo del archivo ${archivos2[i].name} debe ser menor a ${tamanioEnMb} MB`);
                }
                else{
                    trabajo.items.tablas.push($('input[name="tabla"]').get(0).files[i].name);
                }
            };
            console.log(trabajo.items.otras_instituciones);
            if (contador == 0) {
                var parameters = new FormData();
                parameters.append('action', $('input[name="action"]').val());
                parameters.append('trabajo', JSON.stringify(trabajo.items));
                for (var i = 0; i < $('input[name="manuscrito"]').get(0).files.length; ++i) {
                    parameters.append('manuscritos', document.getElementById('id_manuscrito').files[i]);                    
                }
                for (var i = 0; i < $('input[name="tabla"]').get(0).files.length; ++i) {
                    parameters.append('tablas', document.getElementById('id_tabla').files[i]);                    
                }
                submit_trabajo_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
                    location.href = '/create_Trabajo/';
                });
            }            
        });
    });