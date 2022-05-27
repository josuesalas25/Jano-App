let btnClear = document.querySelector('button');
let inputs = document.querySelectorAll('input');

btnClear.addEventListener('click', () => {
    inputs.forEach(input =>  input.value = '');
});



$(document).ready(function () {
    var table = $('#nombreCol').DataTable({
        orderCellsTop: true,
        fixedHeader: true,
        paging: true,
        lengthChange: false,
        searching: true,
        ordering: false,
        info: true,
        autoWidth: true,
        responsive: true,

    });

    //Creamos una fila en el head de la tabla y lo clonamos para cada columna
    $('#nombreCol thead tr').clone(true).appendTo('#nombreCol thead');

    $('#nombreCol thead tr:eq(1) th').each(function (i) {
        var title = $(this).text(); //es el nombre de la columna
        $(this).html('<input type="text" placeholder="Buscar" />');

        $('input', this).on('keyup change', function () {
            if (table.column(i).search() !== this.value) {
                table
                    .column(i)
                    .search(this.value)
                    .draw();
            }
        });
    });
});