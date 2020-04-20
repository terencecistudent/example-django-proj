$( document ).ready(function() {
    // Alert message will disappear after 3 seconds.
    setTimeout(function () {
        if ($(".alert").is(":visible")) {
            $(".alert").fadeOut("fast");
        }
    }, 3000)

    // Navbar items active colour when clicked
    let current = location.pathname;
    $('.navbar-nav li a').each(function(){
        let $this = $(this);
        if($this.attr('href').indexOf(current) !== -1) {
            $this.addClass('active');
        }
    });

    // Selected value from dropdown shown below dropdowns
    let urlPath = window.location.pathname;
    if (urlPath.match("^/books/")) {
        urlPath = urlPath.replace("/books/", "");
    } 

    if (urlPath != "") {
        $("#selectedOption").text(urlPath);
    }

    /*
        changes html text depending on url match below 'Filter:' and
        keeps navbar link active after each filter change
    */
    url = window.location.href;

    if (url.match("/books/published_date_desc")) {
        $("#selectedOption").html("Newest");
        $("#books-item").addClass("active");
    } else if (url.match("/books/published_date_asc")) {
        $("#selectedOption").html("Oldest");
        $("#books-item").addClass("active");
    } else if (url.match("/books/price_asc")) {
        $("#selectedOption").html("Low-High");
        $("#books-item").addClass("active");
    } else if (url.match("/books/price_desc")) {
        $("#selectedOption").html("High-Low");
        $("#books-item").addClass("active");
    } else if (url.match("/books/comics")) {
        $("#selectedOption").html("Comics");
        $("#books-item").addClass("active");
        $("#pagination-content").hide();
    } else if (url.match("/books/food")) {
        $("#selectedOption").html("Food");
        $("#books-item").addClass("active");
        $("#pagination-content").hide();
    } else if (url.match("/books/horror")) {
        $("#selectedOption").html("Horror");
        $("#books-item").addClass("active");
        $("#pagination-content").hide();
    } else if (url.match("/books/mystery")) {
        $("#selectedOption").html("Mystery");
        $("#books-item").addClass("active");
        $("#pagination-content").hide();
    } else if (url.match("/books/sport")) {
        $("#selectedOption").html("Sport");
        $("#books-item").addClass("active");
        $("#pagination-content").hide();
    }

    /*
        if URL matches /search/ then remove hr line,
        filter div and pagination
    */
    if (url.match("/search/")) {
        $("#filter-div").hide();
        $("#filter-hr").hide();
        $("#books-item").addClass("active");
        $("#pagination-content").hide();
    }
});
