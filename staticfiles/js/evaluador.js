
$(function () {

    $('#btnForm1').on('click', function () {
        alert_confirm1();
    });
    $('#btnForm2').on('click', function () {
        alert_confirm2();
    });
    $('#btnForm3').on('click', function () {
        alert_confirm3();
    });
    $('#btnForm4').on('click', function () {
        alert_confirm4();
    });
    $('#btnForm5').on('click', function () {
        alert_confirm5();
    });
    $('#btnForm6').on('click', function () {
        alert_confirm6();
    });
    $('#btnForm7').on('click', function () {
        alert_confirm7();
    });
});



function alert_confirm1() {
    
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
function alert_confirm2() {
    
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
                    document.frm2.submit();
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
function alert_confirm3() {
    
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
                    document.frm3.submit();
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
function alert_confirm4() {
    
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
                    document.frm4.submit();
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
function alert_confirm5() {
    
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
                    document.frm5.submit();
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
function alert_confirm6() {
    
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
                    document.frm6.submit();
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
function alert_confirm7() {
    
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
                    document.frm7.submit();
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