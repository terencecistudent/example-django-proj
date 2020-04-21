describe("Teds Books Online", function(){
    /*
        Alert messages
    */
    describe("Alert messages will appear after user signs in/registers/logs out", function() {
        it("should leave a message for the user if they signed in", function() {
            var result = removedMessage("You have signed in");
            expect(result).toBe("Message alerted");
        });
        it("should leave a message for the user if they signed out", function() {
            var result = removedMessage("You have signed out");
            expect(result).toBe("Message alerted");
        });
        it("should leave a message for the user if they registered an account", function() {
            var result = removedMessage("You have registered an account");
            expect(result).toBe("Message alerted");
        });
    });

    /*
        Book image matching book's content.
        A sample of books.
    */
    describe("Book image should match book content", function() {
        it("should return Matches! for viewing the Dark Woods book", function() {
            var selected = selectedBook("DarkWoods");
            expect(selected).toBe("Matches!");
        });
        it("should return Matches! for viewing the Thinner book", function() {
            var selected = selectedBook("Thinner");
            expect(selected).toBe("Matches!");
        });
        it("should return Matches! for viewing the Wenger book", function() {
            var selected = selectedBook("Wenger");
            expect(selected).toBe("Matches!");
        });
        it("should return Matches! for viewing the Skeleton Keys book", function() {
            var selected = selectedBook("SkeletonKeys");
            expect(selected).toBe("Matches!");
        });
    });

    /*
        Active navbar status coloured white
    */
    describe("Active navbar active class changed when nav-link is clicked", function() {
        it("should changed the active class to About nav-link when clicked", function() {
            var selected = activeNav("About");
            expect(selected).toBe("Active");
        });
        it("should changed the active class to Books nav-link when clicked", function() {
            var selected = activeNav("Books");
            expect(selected).toBe("Active");
        });
        it("should changed the active class to Forum nav-link when clicked", function() {
            var selected = activeNav("Forum");
            expect(selected).toBe("Active");
        });
        it("should changed the active class to Profile nav-link when clicked", function() {
            var selected = activeNav("Profile");
            expect(selected).toBe("Active");
        });
        it("should changed the active class to Sign In nav-link when clicked", function() {
            var selected = activeNav("Sign In");
            expect(selected).toBe("Active");
        });
        it("should changed the active class to Register nav-link when clicked", function() {
            var selected = activeNav("Register");
            expect(selected).toBe("Active");
        });
        it("should changed the active class to Cart nav-link when clicked", function() {
            var selected = activeNav("Cart");
            expect(selected).toBe("Active");
        });
    });

    /*
        Selected genre returning books
        with that genre
    */
    describe("Selected genre returns HTML with genre selected below dropdowns", function() {
        it("should return Genre Picked for books with genres Comics", function() {
            var selected = selectedGenre("Comics");
            expect(selected).toBe("Genre Picked");
        });
        it("should return Genre Picked for books with genres Food", function() {
            var selected = selectedGenre("Food");
            expect(selected).toBe("Genre Picked");
        });
        it("should return Genre Picked for books with genres Horror", function() {
            var selected = selectedGenre("Horror");
            expect(selected).toBe("Genre Picked");
        });
        it("should return Genre Picked for books with genres Mystery", function() {
            var selected = selectedGenre("Mystery");
            expect(selected).toBe("Genre Picked");
        });
        it("should return Genre Picked for books with genres Sport", function() {
            var selected = selectedGenre("Sport");
            expect(selected).toBe("Genre Picked");
        });
    });

    /*
        Selected price asc or desc
    */
    describe("Selected price asc or desc returns HTML with price selected below dropdowns", function() {
        it("should return Price Picked for books with price low-high", function() {
            var selected = selectedPrice("Low-High");
            expect(selected).toBe("Price Picked");
        });
        it("should return Price Picked for books with price high-low", function() {
            var selected = selectedPrice("High-Low");
            expect(selected).toBe("Price Picked");
        });
    });

    /*
        Selected date published asc or desc
    */
    describe("Selected published date asc or desc returns HTML with published date selected below dropdowns", function() {
        it("should return Published Date for books with price low-high", function() {
            var selected = selectedDate("Newest-Oldest");
            expect(selected).toBe("Published Date");
        });
        it("should return Price Picked for books with price high-low", function() {
            var selected = selectedDate("Oldest-Newest");
            expect(selected).toBe("Published Date");
        });
    });
});
