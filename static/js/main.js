$( document ).ready(function() {
    $(".nav-link").on("click", function(){
        $(".nav-link.active").removeClass("active");
        $(this).addClass("active");
    });

    // Alert message will disappear after 5 seconds.
    setTimeout(function () {
        if ($(".alert").is(":visible")) {
            $(".alert").fadeOut("fast");
        }
    }, 5000)
});
