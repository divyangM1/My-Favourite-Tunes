// Logic to move from table rows to further detailed view.
var $ = jQuery.noConflict();

$(document).ready(function() {
    $(".table-row").click(function() {
        console.log("Row clicked!");
        window.location.href = $(this).data("href");
    });
});


// AddSongs onclick function logic 
function redirectToAddSongs(event) {
    // Prevents this button to work as search button.
    event.preventDefault();

    // Redirects to the "Add Songs" path
    window.location.href = "add-songs/";
}

// AddSongs onclick function logic 
function redirectToArtist(event) {
    // Prevents this button to work as search button.
    event.preventDefault();

    // Redirects to the "Add Songs" path
    window.location.href = 'artist-songs/';
}

