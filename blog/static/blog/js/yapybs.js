jQuery(document).ready(function() {
    var i = document.createElement('input');
    i.setAttribute('type', 'date');

    if(i.type == 'text')
    {
        $('input[type=date]').datepicker();
    }
});

function backToSearch(event) {
    if(!event)
    {
        var event = window.event;
    }
    event.preventDefault(event);
    window.history.back();
}