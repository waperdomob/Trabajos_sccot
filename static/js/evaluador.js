
$(function () {

    $('#btnForm1').on('click', function () {
        alert_confirm();
    });
    $('#btnForm2').on('click', function () {
        alert_confirm();
    });
    $('#btnForm3').on('click', function () {
        alert_confirm();
    });
    $('#btnForm4').on('click', function () {
        alert_confirm();
    });
    $('#btnForm5').on('click', function () {
        alert_confirm();
    });
    $('#btnForm6').on('click', function () {
        alert_confirm();
    });
    $('#btnForm7').on('click', function () {
        alert_confirm();
    });
});



function alert_confirm() {
    
    $.confirm({
        theme: 'material',
        title: "Confirmación",
        icon: 'fa fa-info',
        content: "¿Estas seguro de enviar la calificación?",
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
                    document.frm1.submit();
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    });

}