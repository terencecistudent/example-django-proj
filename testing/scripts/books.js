/*
    function for removedMessages
*/
function removedMessage(message) {
    if (message == "You have signed in") {
        return ("Message alerted");
    } else if (message == "You have signed out") {
        return ("Message alerted")
    } else if (message == "You have registered an account") {
        return ("Message alerted")
    }
}

/*
    function for selectedBook
*/
function selectedBook(book) {
    if (book === "DarkWoods") {
        return ("Matches!");
    } else if (book == "Thinner") {
        return ("Matches!");
    } else if (book == "Wenger") {
        return ("Matches!");
    } else if (book == "SkeletonKeys") {
        return ("Matches!");
    }
}

/*
    function for selectedBook
*/
function activeNav(navItem) {
    if (navItem === "About") {
        return ("Active");
    } else if (navItem == "Books") {
        return ("Active");
    } else if (navItem == "Forum") {
        return ("Active");
    } else if (navItem == "Profile") {
        return ("Active");
    } else if (navItem == "Sign In") {
        return ("Active");
    } else if (navItem == "Register") {
        return ("Active");
    } else if (navItem == "Cart") {
        return ("Active");
    }
}

/*
    function for selectedGenre
*/
function selectedGenre(genre) {
    if (genre === "Comics") {
        return ("Genre Picked");
    } else if (genre == "Food") {
        return ("Genre Picked");
    } else if (genre == "Horror") {
        return ("Genre Picked");
    } else if (genre == "Mystery") {
        return ("Genre Picked");
    } else if (genre == "Sport") {
        return ("Genre Picked");
    }
}

/*
    function for selectedPrice
*/
function selectedPrice(price) {
    if (price === "Low-High") {
        return ("Price Picked");
    } else if (price == "High-Low") {
        return ("Price Picked");
    }
}

/*
    function for selectedDate
*/
function selectedDate(date) {
    if (date === "Newest-Oldest") {
        return ("Published Date");
    } else if (date == "Oldest-Newest") {
        return ("Published Date");
    }
}
