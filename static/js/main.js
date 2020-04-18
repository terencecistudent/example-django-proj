$( document ).ready(function() {
    // Alert message will disappear after 3 seconds.
    setTimeout(function () {
        if ($(".alert").is(":visible")) {
            $(".alert").fadeOut("fast");
        }
    }, 3000)
});
