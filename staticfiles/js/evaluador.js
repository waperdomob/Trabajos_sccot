var $calificarBTN = document.getElementById("#calificarBTN");
$(function () {
    
    $('#plantilla1_form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        console.log(parameters);
        parameters.append('action', 'realizar_evaluacion1');
        submit_with_ajax('/Evaluador/evaluacionECC/'+parameters.idf, 'Notificación',
            '¿Estas seguro de realizar la siguiente evaluación?', parameters, function (response) {
                //console.log(response);
                message_success("Trabajo registrado con exito!");
                location.href = '/';
            });
    });
    $('#plantilla2_form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        console.log(parameters);
        parameters.append('action', 'realizar_evaluacion');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de realizar la siguiente evaluación?', parameters, function (response) {
                //console.log(response);
                message_success("Trabajo registrado con exito!");
                location.href = '/';
            });
    });
    $('#plantilla3_form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        console.log(parameters);
        parameters.append('action', 'realizar_evaluacion');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de realizar la siguiente evaluación?', parameters, function (response) {
                //console.log(response);
                message_success("Trabajo registrado con exito!");
                location.href = '/';
            });
    });
    $('#plantilla4_form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'realizar_evaluacion');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de realizar la siguiente evaluación?', parameters, function (response) {
                //console.log(response);
                message_success("Trabajo registrado con exito!");
                location.href = '/';
            });
    });
    $('#plantilla5_form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'realizar_evaluacion');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de realizar la siguiente evaluación?', parameters, function (response) {
                //console.log(response);
                message_success("Trabajo registrado con exito!");
                location.href = '/';
            });
    });
    $('#plantilla6_form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'realizar_evaluacion');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de realizar la siguiente evaluación?', parameters, function (response) {
                //console.log(response);
                message_success("Trabajo registrado con exito!");
                location.href = '/';
            });
    });
    $('#plantilla7_form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'realizar_evaluacion');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de realizar la siguiente evaluación?', parameters, function (response) {
                //console.log(response);
                message_success("Trabajo registrado con exito!");
                location.href = '/';
            });
    });


});