# Ted's Books Online - Code Institute

## Description
This is an ecommerce website that I created.  Users are able to register an account and sign in or sign out
out their account.  Users are able to view a variety of books and can use the search box or dropdowns to filter
the search.  Users can view a full book's detail by clicking on the image or book name.  This will direct them
to a page showing the book's image, name, genre, published date, description and price.  Also users can add that
book to the cart from the main books page or the book detail page.  Users can then fill in the quantity of a book
or books then add to cart.  In the cart, the order will show and the user can change the quantity of a book.
The user can click the checkout button bringing them to the checkout page.  It will show the same order or orders
made by the user however the quantity cannot be edited, this will have to be done in the cart.

Users with an account have access to the forum page.  On this page users can discuss book by creating a new post or
adding a comment within a post.

Users with an account will also be able to access their profile page, which includes their account details and order
history.

I have started this project by creating mockups and wireframes to help give me an idea of how I was going to 
design the website across all platforms considered, laptops, iPads and mobile devices.  Below is attached my
mocks and wireframes:


## Wireframes 
wireframes need to go here 


## UX
### User Stories
#### Implemented:
1. As a user, I would like to create an account on this website so I can access the forum page.
    - **End User Goal**: User is able to create an account and they can access the forum page.
    - **End Business Goal**: Registration form working as expected.
    - **Acceptance Criteria**: Account created for user and they have access to forum page.
    - **Measurement Of Success**: Check Manual Tests document.

2. As a user, I would like to sign into my account on this website so I can access the forum page.
    - **End User Goal**: User is able to sign in and they can access the forum page.
    - **End Business Goal**: Login form working as expected.
    - **Acceptance Criteria**: User signed in and they have access to forum page.
    - **Measurement Of Success**: Check Manual Tests document.

3. As a user, I would like to click on a book to view the book's details.
    - **End User Goal**: User is able to click on the book which will direct them to the book details page.
    - **End Business Goal**: Link working to the book details page and the details will be shown correctly.
    - **Acceptance Criteria**: Link is working bringing users to the book details page and the details will 
        be shown correctly.
    - **Measurement Of Success**: Check Manual Tests document.

4. As a user, I would like to add a book or books to the cart as I am interested in buying them.
    - **End User Goal**: User is able to enter an amount into the quantity input and click button
        Add to Cart, which will add the book(s) to the cart.
    - **End Business Goal**: Book added to cart with correct quantity chosen from user.
    - **Acceptance Criteria**: Book adds to cart with correct quantity chosen from user.
    - **Measurement Of Success**: Check Manual Tests document.

5. As a user, I would like to purchase these books in my cart as I am happy with what I have chosen.
    - **End User Goal**: User is able to enter their information and card details into the payment form
        then they can press the Submit Payment form which leads to the items being sold.
    - **End Business Goal**: Payment form details not empty and card details correct leading to a successful
        purchase.
    - **Acceptance Criteria**: Payment form details not valid if any details left out and card details are 
        correct leading to a successful purchase.
    - **Measurement Of Success**: Check Manual Tests document.

6. As a user, I would like to be notified if I have either registered an account, signed in or signed out of
    my account.
    - **End User Goal**: User registers/signs in/signs out and an alert message will be shown.
    - **End Business Goal**: When the user registers an account, signs in or signs out of their account, an
        account message will be displayed.
    - **Acceptance Criteria**: When the user registers an account, signs in or signs out of their account, an
        account message will be displayed.
    - **Measurement Of Success**: Check Manual Tests document and Jasmine Testing.

7. As a user, I would like to be access the forum to see what people think about books.
    - **End User Goal**: User can access forum page if they have an account.
    - **End Business Goal**: User creates an account which lets them access the forum page.
    - **Acceptance Criteria**: User can access forum page if they have an account.
    - **Measurement Of Success**: Check Manual Tests document.

8. As a user, I would like to be post some content on the forum page as I have an account and have access to do so.
    - **End User Goal**: User can create a post on the forum.
    - **End Business Goal**: User creates a post which will be shown on the forum page.
    - **Acceptance Criteria**: Post is created from the user which will be shown along with all the posts.
    - **Measurement Of Success**: Check Manual Tests document.

9. As a user, I would like to be comment some content on the forum page as I have an account and have access to do so.
    - **End User Goal**: User can comment on a post on the forum.
    - **End Business Goal**: User comments on a post which will show in the post detail page.
    - **Acceptance Criteria**: User submits comment in a post, that comment submits and is shown in the comments section.
    - **Measurement Of Success**: Check Manual Tests document.

10. As a user, I would like to see my account details and order history when I click on Profile.
    - **End User Goal**: User is able to see their account information and order history.
    - **End Business Goal**: User visits the Profile page showing them their account information and order history.
    - **Acceptance Criteria**: User submits comment in a post, that comment submits and is shown in the comments section.
    - **Measurement Of Success**: Check Manual Tests document.
#


## Framework
I have chosen to use Bootstrap 4 for the design and layout of my website.  Bootstrap is effective, very efficient to use
and suited the styling of this website.

I have also used the Django framework including jinja templates to also help me create this website.

For the font used, I have used Roboto from Google Fonts.  I have used this font as it is clear and  can be easily read 
by users.
#


## Requirements
- Access to desktop, laptop, table or mobile devices.
- Internet connection.
#


## Features
There are a few features included for this application to work:
- **Navbar Links**: Allows users to easily access each page.
- **Books**: Shows all the books including their information displayed in a presentable fashion.
- **Text Search**: Used for users to text search for a book.
- **Dropdowns**: Used for users to search books based on price: low-high/high-low, published date: newest/oldest
    and genre: Comics, Food, Horror, Mystery and Sport.
- **Add to Cart**: Allows users to add a book to the cart.
- **Payment Form**: Allows users to purchase a book by filling out the payment form in checkout and clicking
    the Submit Payment button.
- **Edit Quantity**: Allows users to edit the quantity of a book in the cart.
- **Register Form**: Allows users to create an account.
- **Sign In**: Allows users to sign into their.
- **Django Messages**: Alert message shown when user registers, signs in/out of their account, also shown
    when their payment transactions are successful or unsuccessful.
- **Logout**: Allows users to sign out of their account.
- **New Post**: Allows users to create a new post to the forum page.
- **Comment**: Allows users to add a comment in a post.
- **User Profle**: Allows users to view their account information and order history.
- **Pagination**: Used on the books and forum pages.
- **Footer**: Allows users to visit the Twitter, Facebook and Instagram websites.
#


## Deployment
This application was deployed using Heroku which can be viewed from here: 
...

I have used GitPod to build this application and close to the end of finishing up.  This was pushed
to Heroku through the command line by linking the master git from my remote GitHub repository to a 
new app created in Heroku.

There are no differences between the website's development version and the deployed version to Heroku.

### Deploying to Heroku:
1. Go to the Heroku website [here](https://id.heroku.com/login).
2. Sign Up or Sign In which will direct you to the dashboard.
3. Click on **New > Create new app**.
4. Enter app name and choose region then press **Create App**.
5. Go to **Settings > Reveal Config Vars**:
    - Enter Keys and their values, example keys below:

    ![image](https://user-images.githubusercontent.com/48124466/76408488-eeb69f00-6384-11ea-8672-d0261d3156f5.png)
6. In the CLI, login into Heroku by **heroku login -i**, where you will be asked to your enter email address and
    password.
7. If you have already created your Heroku app, you can remote to your local repository with the heroku git:remote command.
8. Set debug=False for deployment.
9. To deploy your app to Heroku, use the git push command to push the code from your local repository’s master branch to 
    your heroku remote:

    ![image](https://user-images.githubusercontent.com/48124466/76408974-ae0b5580-6385-11ea-9cf1-8d67c4f0dff5.png)
10. When the build is complete, on the Heroku website, in the app click **Open App**.

[Deploying with Git](https://devcenter.heroku.com/articles/git)
#


## Installing
Software used to complete this game: **GitPod**

First go to GitHub: https://github.com/
1. Sign In or Sign Up to GitHub.
2. Once signed in, go to the left side of the screen and you will see:

![image](https://user-images.githubusercontent.com/48124466/68049737-89b6b280-fcdb-11e9-9e41-e02d4dc6fa9a.png)

3. Click **New**.
4. Fill out new repository details.
5. Click **Create Repository** at the bottom.
6. At the top right click GitPod (if installed) or enter URL Prefix.
7. Follow instructions below.

**How to install GitPod:**
- URL Prefix:
- Browser Extension
- GitHub App

Here is the link for instructions: https://www.gitpod.io/

URL Prefix:
Browser Extension
GitHub App
Here is the link for instructions: https://www.gitpod.io/
#


## Testing
### Jasmine Tests:
I have conducted tests using Jasmine Testing Framework [click here](https://github.com/terencecistudent/Data-Centric-Dev-Project-TL/tree/master/testing), 
such tests involve:

1. Selecting the price either asc or desc which returns HTML text with that price selected:

![image](https://user-images.githubusercontent.com/48124466/80009980-ac26cd00-84c1-11ea-8cf3-524eb5dc5a9b.png)

2. Selecting the genre will return HTML text with that genre selected:

![image](https://user-images.githubusercontent.com/48124466/80010160-ea23f100-84c1-11ea-91c7-817af85ff417.png)

3. Selecting the published date either asc or desc will return HTML text with that date selected:

![image](https://user-images.githubusercontent.com/48124466/80010258-13448180-84c2-11ea-9cf8-1d1fda77ecc6.png)

4. Alert messages will appear when the user registers/signs in/logs out:

![image](https://user-images.githubusercontent.com/48124466/80010380-3f600280-84c2-11ea-9790-be7f56627f1e.png)

5. Book image should match the book content:

![image](https://user-images.githubusercontent.com/48124466/80010480-63234880-84c2-11ea-8314-3408bb5968f2.png)

6. Active navbar changes when another nav-link is clicked:

![image](https://user-images.githubusercontent.com/48124466/80010638-9f56a900-84c2-11ea-9ec6-20d70517700e.png)


### Manual Tests:
I have also carried out manual tests which show the CRUD operations in use and filtering animal types.

[Manual Tests](https://github.com/terencecistudent/Data-Centric-Dev-Project-TL/blob/master/testing/Manual%20Tests.pdf)


### Running Responsive Designs on Google Chrome:
Here is a link how to run the application on a live server by configuring and exposing ports with GitPod:
https://www.gitpod.io/docs/43_config_ports/

**To view responsive applications:**
1. Right click then go to **Inspect Element**
2. Click on the **Toggle Device Toolbar** (Icons showing two devices):

![image](https://user-images.githubusercontent.com/48124466/68051275-f2ebf500-fcde-11e9-8b3a-adc7abc16c5f.png)

3. Click on any device, for example, iPhone 5/SE selected:

![image](https://user-images.githubusercontent.com/48124466/68051467-5aa24000-fcdf-11e9-8666-d29f1afa8955.png)


## Technologies Used
### Languages:
- HTML5
    - Used for the structure and layout.
- CSS3
    - Used for the styling of the wesbsite.
- JavaScript
    - Used to implement Stripe and custom JavaScript.
- Python
    - Used to code the back end functions.

### README.md:
- Markdown
    - Used for the README.md file.

### Frameworks:
- Bootstrap v4.3.1
    - This framework used in this appplication for:
        - Navbar
        - Styling
        - Responsive Layouts
        - Buttons
- Django Framework
    - Is a Python framework that encourages rapid development.
- Stripe
    - Used to create valid transactions including using Stripe's test card number 4242424242424242.

### Database:
- Heroku Postgres
    - PostgreSQL used to link tables together.

### Libraries:
- Font Awesome
    - Font Awesome Icons were used throughout the website.
- jQuery
    - Used to help simplify HTML DOM tree traversal and manipulation.
- Google Fonts
    - Helped with the visibility of the text for users to see clearly.

### Others:
- Git 
    - Version control to the GitHub repositories.
    - Ran the code to expose a live port.
- GitHub
    - Remote repository.
- Google Chrome Developer Tools 
    - Helped with small changes.
#


## Support
To contact GitHub, follow this link: https://support.github.com/
#


## Credits
### Media:
- I got the background image from a free open sourced website: https://www.pexels.com/.
- For the uploaded images in my database, I used [Mumble Books](https://mumblebooks.co.uk/)

### Book Information:
- Book information was researched from [Mumble Books](https://mumblebooks.co.uk/)

### Authors and Acknowledgment:
- **Autor**: Terence Logue
- **Acknowledgment**: Code Institute Slack, Code Institute Tutor Support, Assigned Mentor: Maranatha Ilesanmi
