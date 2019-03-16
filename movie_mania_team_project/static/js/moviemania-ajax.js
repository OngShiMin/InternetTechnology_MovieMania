$(document).ready(function() {
    $('#likes').click(function() {
    var movieid;
    movieid = $(this).attr("data-movieid");
    $.get('/moviemania/like/', {movie_id: movieid}, function(data) {
        $('#like_count').html(data);
        $('#likes').hide();
    });
});
});

$(document).ready(function() {
    $('#watchlist').click(function() {
    var movieid;
    movieid = $(this).attr("data-movieid");
    $.get('/moviemania/watchlist_add/', {movie_id: movieid}, function(data) {
        $('#watchlist_count').html(data);
        $('#watchlist').hide();
    });
});
});


$(document).ready(function() {
    $('#remove_favorites_button').click(function() {
    var movieid;
    movieid = $(this).attr("data-movieid");
    $.get('/moviemania/favorites_remove/', {movie_id: movieid}, function(data) {
        $('#like_count').html(data);
        $('#remove_favorites_button').hide();
    });
});
});

$(document).ready(function() {
    $('#remove_watchlist_button').click(function() {
    var movieid;
    movieid = $(this).attr("data-movieid");
    $.get('/moviemania/watchlist_remove/', {movie_id: movieid}, function(data) {
        $('#watchlist_count').html(data);
        $('#remove_watchlist_button').hide();
    });
});
});

$(document).ready(function() {
    $('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/moviemania/suggest_movie/', {suggestion: query}, function(data){
            $('#movies').html(data);
        });
    });

});

