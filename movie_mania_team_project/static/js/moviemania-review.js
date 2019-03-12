//for submitting comments
$("#reviews").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.
    var form = $(this);
    var url = form.attr('action');

    $.ajax({
        type: "POST",
        url: url,
        data: form.serialize(), // serializes the form's elements.
        success: function(data)
        {
            console.log('Submission was successful.');
            alert("success");
            $("#reviews").hide();
        },
        error: function (data) {
            console.log('An error occurred.');
            console.log(data);
        },
    });
});

// load comment form by clicking on the comment button
$("comment-btn").click(function(e){
    $("#reviews").show();
    e.preventDefault();
 });
 
 // star rating
$(function () {

    var $rateYo = $("#rateYo").rateYo();

$("#getRating").click(function () {
    starWidth: "20px";
    /* get rating */
    var rating = $rateYo.rateYo("rating");

    window.alert("Its " + rating + " Yo!");
});

$("#setRating").click(function () {

    /* set rating */
    var rating = getRandomRating();
    $rateYo.rateYo("rating", rating);
});
});