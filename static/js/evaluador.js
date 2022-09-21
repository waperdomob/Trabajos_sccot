var $calificarBTN = document.getElementById("#calificarBTN");
$(function () {
    
    $('.plantilla1BTN').on('click', function () {
        $('#plantilla1_Modal').modal('show');
    });
    $('.plantilla2BTN').on('click', function () {
        $('#plantilla2_Modal').modal('show');
    });
    $('.plantilla3BTN').on('click', function () {
        $('#plantilla3_Modal').modal('show');
    });
    $('.plantilla4BTN').on('click', function () {
        $('#plantilla4_Modal').modal('show');
    });
    $('.plantilla5BTN').on('click', function () {
        $('#plantilla5_Modal').modal('show');
    });
    $('.plantilla6BTN').on('click', function () {
        $('#plantilla6_Modal').modal('show');
    });
    $('.plantilla7BTN').on('click', function () {
        $('#plantilla7_Modal').modal('show');
    });
    $('.plantillaEPBTN').on('click', function () {
        $('#plantillaEP_Modal').modal('show');
    });

    $('#plantilla1_form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'realizar_evaluacion1');
        console.log(parameters);
        submit_with_ajax(window.location.pathname, 'Notificación',
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