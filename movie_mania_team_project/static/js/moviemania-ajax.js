$('#suggestion').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/moviemania/suggest/', {suggestion: query}, function(data){
        $('#movies').html(data);
    });
});