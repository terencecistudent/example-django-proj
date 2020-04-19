$( document ).ready(function() {
    // Alert message will disappear after 3 seconds.
    setTimeout(function () {
        if ($(".alert").is(":visible")) {
            $(".alert").fadeOut("fast");
        }
    }, 3000)

    // Navbar items active colour
    let current = location.pathname;
    $('.navbar-nav li a').each(function(){
        let $this = $(this);
        if($this.attr('href').indexOf(current) !== -1){
            $this.addClass('active');
        }
    });

    setTimeout(function() {

    // Trigger the active class on DOM Ready...
        $('.btn-group').find('.active').trigger('click');

    }, 10);

    // Selected value from dropdown shown below dropdowns
    let urlPath = window.location.pathname;
    if (urlPath.match("^/books/")) {
        urlPath = urlPath.replace("/books/", "");
    }

    if (urlPath != "") {
        $("#selectedOption").text(urlPath);
    }

    // changes html text depending on url match
    url = window.location.href;
    if (url.match("/books/published_date_desc")) {
        $("#selectedOption").html("Newest");
    } else if (url.match("/books/published_date_asc")) {
        $("#selectedOption").html("Oldest");
    } else if (url.match("/books/price_asc")) {
        $("#selectedOption").html("Low-High");
    } else if (url.match("/books/price_desc")) {
        $("#selectedOption").html("High-Low");
    } else if (url.match("/books/comics")) {
        $("#selectedOption").html("Comics");
    } else if (url.match("/books/food")) {
        $("#selectedOption").html("Food");
    } else if (url.match("/books/horror")) {
        $("#selectedOption").html("Horror");
    } else if (url.match("/books/mystery")) {
        $("#selectedOption").html("Mystery");
    } else if (url.match("/books/sport")) {
        $("#selectedOption").html("Sport");
    } 
});
