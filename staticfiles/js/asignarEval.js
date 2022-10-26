var evaluador_trabajo = {
    items: {
        evaluador: "",
        plantilla: "",
        confirmacion: null,
    },
};
$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es',
        dropdownParent: $('#evaluador_Modal .modal-content')
    });
});
