
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
        },
        error: function (data) {
            console.log('An error occurred.');
            console.log(data);
        },
    });
});

function loadComment() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("reviews").style.display="";
        }
    };
    xhttp.open("GET", "/templates/moviemania/movie.html", true);
     xhttp.send();
}