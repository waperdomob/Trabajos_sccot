$(function () {
    /* Función que recibe los eventos en la vista del alministrador
    Algunos eventos son: cambiar de pestaña y agregar especialidad
    NOTA: Todos los archivos js también hay que crearlos en la carpeta staticfiles en el mismo orden para que funcionen en producción.
    */
    $('#btnradio1').on('click', function () {
        $('#contenedorAutores').prop('hidden', false);
        $('#contenedorTrabajos').prop('hidden', true);
        $('#contenedorCursos').prop('hidden', true);
        $('#contenedorUsuarios').prop('hidden', true);
        $('#contenedorReportes').prop('hidden', true);
        
    });
    $('#btnradio2').on('click', function () {
        $('#contenedorAutores').prop('hidden', true);
        $('#contenedorTrabajos').prop('hidden', false);
        $('#contenedorCursos').prop('hidden', true);
        $('#contenedorUsuarios').prop('hidden', true);
        $('#contenedorReportes').prop('hidden', true);
    });
    $('#btnradio3').on('click', function () {
        $('#contenedorTrabajos').prop('hidden', true);
        $('#contenedorAutores').prop('hidden', true);
        $('#contenedorCursos').prop('hidden', false);
        $('#contenedorUsuarios').prop('hidden', true);
        $('#contenedorReportes').prop('hidden', true);        
    });
    $('#btnradio4').on('click', function () {
        $('#contenedorTrabajos').prop('hidden', true);
        $('#contenedorAutores').prop('hidden', true);
        $('#contenedorCursos').prop('hidden', true);
        $('#contenedorUsuarios').prop('hidden', false);
        $('#contenedorReportes').prop('hidden', true);
    });
    $('#btnradio5').on('click', function () {
        $('#contenedorTrabajos').prop('hidden', true);
        $('#contenedorAutores').prop('hidden', true);
        $('#contenedorCursos').prop('hidden', true);
        $('#contenedorUsuarios').prop('hidden', true);
        $('#contenedorReportes').prop('hidden', false);
    });

    $(document).on('click', '#btnAddEspec', function() {
        $('#crearCurso_Modal').modal('hide');
        $('#especialidadesModal').modal('show');
    });
    $(document).on('click', '#btnAddEspec2', function() {
        
        $('#crearAutor_Modal').modal('hide');
        $('#especialidadesModal2').modal('show');
    });

    $('#Espec_form1').on('submit', function (e) {
        e.preventDefault();
        const especialidad = document.getElementById('id_especialidad').value;
        
        var parameters = new FormData(this);
        parameters.append('action', 'create_especialidad');
        $.ajax({
            url: 'ajax_especialidades', 
            type: 'GET',
            data:{ 'especialidad': especialidad} ,
            headers: {
                'X-CSRFToken': csrftoken
              },
              success: function (data) {
                if (!data.hasOwnProperty('error')) {
                    message_success(data['mensaje']);
                    $(function () {
                        var newOption = new Option(data.especialidad, data.id, false, true);
                        $('select[name="especialidad"]').append(newOption).trigger('change');

                        $('#crearCurso_Modal').modal('show');                    
                        $('#especialidadesModal').modal('hide');
                    });
                    return false;
                }
                message_error(data['error']);
              },
              error: function(error) {
                console.log(error)
                $("#result").html("<p>ups... Algo salió mal</p>")
                },
        });
    });
    $('#Espec_form2').on('submit', function (e) {
        e.preventDefault();
        const especialidad = document.getElementById('id_especialidad2').value;
        
        var parameters = new FormData(this);
        parameters.append('action', 'create_especialidad');
        $.ajax({
            url: 'ajax_especialidades', 
            type: 'GET',
            data:{ 'especialidad': especialidad} ,
            headers: {
                'X-CSRFToken': csrftoken
              },
              success: function (data) {
                if (!data.hasOwnProperty('error')) {
                    message_success(data['mensaje']);
                    $(function () {
                        var newOption = new Option(data.especialidad, data.id, false, true);
                        $('select[name="especialidad"]').append(newOption).trigger('change');

                        $('#crearAutor_Modal').modal('show');                    
                        $('#especialidadesModal2').modal('hide');
                    });
                    return false;
                }
                message_error(data['error']);
              },
              error: function(error) {
                message_error(error)
                $("#result").html("<p>ups... Algo salió mal</p>")
                },
        });
    });
});