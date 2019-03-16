$(document).ready(function() {
    /*
    $("#about-btn").click( function(event) {
        msgstr = $("#msg").html()
        msgstr = msgstr + "ooo"
        $("#msg").html(msgstr)
        alert("You clicked the button using JQuery!");

    });
    */


    $("p").hover( function() {
        $(this).css('color', 'red');
    },
    function() {
        $(this).css('color', 'blue');
    });




});