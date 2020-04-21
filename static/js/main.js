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
        Changes html text depending on url match below 'Filter:' and
        keeps navbar link active after each filter change
    */
    url = window.location.pathname;

    const urlArray = [
        {
            path: "/books/published_date_desc",
            value: "Newest"
        },
        {
            path: "/books/published_date_asc",
            value: "Oldest"
        },
        {
            path: "/books/price_asc",
            value: "Low-High"
        },
        {
            path: "/books/price_desc",
            value: "High-Low"
        },
        {
            path: "/books/comics",
            value: "Comics"
        },
        {
            path: "/books/food",
            value: "Food"
        },
        {
            path: "/books/horror",
            value: "Horror"
        },
        {
            path: "/books/mystery",
            value: "Mystery"
        },
        {
            path: "/books/sport",
            value: "Sport"
        },
    ]

    for (let i=0; i < urlArray.length; i++) {
        if (url === urlArray[i].path) {
            $("#selectedOption").html(urlArray[i].value);
            $("#books-item").addClass("active");
        }
    }

    /*
        If URL matches /search/ then remove hr line,
        filter div and pagination
    */
    if (url.match("/search/")) {
        $("#filter-div").hide();
        $("#filter-hr").hide();
        $("#books-item").addClass("active");
        $("#pagination-content").hide();
    }
});
