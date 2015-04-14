jQuery(document).ready(function() {
    var i = document.createElement('input');
    i.setAttribute('type', 'date');

    if(i.type == 'text')
    {
        $('input[type=date]').datepicker();
    }
});