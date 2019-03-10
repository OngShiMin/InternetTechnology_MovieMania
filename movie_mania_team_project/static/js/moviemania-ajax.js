$(document).ready(function() {
    $('#likes').click(function() {
    var movieid;
    movieid = $(this).attr("data-movieid");
    $.get('/moviemania/like/', {movie_id: movieid}, function(data) {
        $('#like_count').html(data);
        $('#likes').hide();
    });
});



    $('#suggestion').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/moviemania/suggest_movie/', {suggestion: query}, function(data){
        $('#movies').html(data);
    });
});

});

