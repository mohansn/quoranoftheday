$(document).ready(function () {
    $( "form" ).submit(function( event ) {
        alert($("#nameselect").val());
        console.log($("#nameselect").val());
        $.ajax({
            url:"/getdata",
            type: 'get',
            data: {
                'user': $("#nameselect").val(),
                async:false
            },
            success: function (data) {
                // Send to D3 for plot
                alert ("Got data");
                console.log (data);
            }
        });
        event.preventDefault();
    });
});