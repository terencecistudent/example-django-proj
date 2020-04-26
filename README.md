[![Build Status](https://travis-ci.org/terencecistudent/teds-books-online.svg?branch=master)](https://travis-ci.org/terencecistudent/teds-books-online)

# Ted's Books Online - Code Institute

## Description
This is an ecommerce website that I created which sells books.  Users are able to register an account and sign in or sign out
out their account.  Users are able to view a variety of books and can use the search box or dropdowns to filter
the search.  Users can view a full book's detail by clicking on the image or book name.  This will direct them
to a page showing the book's image, name, genre, published date, description and price.  Also, users can add that
book to the cart from the main books page or the book detail page.  Users can then fill in the quantity of a book
or books then add to cart.  In the cart, the books added to cart will show and the user can change the quantity of a book.
The user can click the checkout button bringing them to the checkout page.  It will show the same order or orders
made by the user however the quantity cannot be edited, this will have to be done in the cart.  Users can remove a book
from the cart by pressing the Remove button.

**For payments to be successful, use Stripe's test card number 4242424242424242**

Users with an account have access to the forum page.  On this page users can discuss book by creating a new post or
adding a comment within a post.

Users with an account will also be able to access their profile page, which includes their account details and order
history.

I have started this project by creating mockups and wireframes to help give me an idea of how I was going to 
design the website across all platforms considered, laptops, iPads and mobile devices.  Below is attached my
mocks and wireframes:
#

## Wireframes 
For the wireframes, I have used a software called Bootstrap Studio which focuses on building wireframes where the
Bootstrap framework is used.  The wireframes have been created to test devices XS, SM, MD, LG and XL as shown in
document below:

[Wireframes can be found here](https://github.com/terencecistudent/teds-books-online/blob/master/wireframes/Mockups2.pdf)

I have also created a document going through The Five Planes:

[The Five Planes](https://github.com/terencecistudent/teds-books-online/blob/master/wireframes/The%20Five%20Planes.pdf)
#

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
- **Edit Quantity**: Allows users to edit the quantity of a book in the cart.
- **Remove from Cart**: Button used to remove a book from the cart.
- **Payment Form**: Allows users to purchase a book by filling out the payment form in checkout and clicking
    the Submit Payment button.
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


## Database Schema
For this project I have used Heroku's add-on SQL Postgres.
### Setting It Up In Heroku
- Once in the app in Heroku, go to resources, find **Add-ons** and search for Heroku Postgres:

![image](https://user-images.githubusercontent.com/48124466/80263198-c4e0df80-8687-11ea-9910-326c645c6b9d.png)

- Click on Heroku Postgres, Plan name: Hobby Dev - Free:

![image](https://user-images.githubusercontent.com/48124466/80263413-74b64d00-8688-11ea-9f53-ea139c6ea2a9.png)

- It is now attached as a database:

![image](https://user-images.githubusercontent.com/48124466/80263452-99122980-8688-11ea-8e90-8194a95e424e.png)

- Go to Settings > Reveal Config Vars:

![image](https://user-images.githubusercontent.com/48124466/80263619-15a50800-8689-11ea-960c-fb93d9593184.png)


### Connecting Database To GitPod
- In GitPod terminal, install dj-database-url:

![image](https://user-images.githubusercontent.com/48124466/80263747-9106b980-8689-11ea-8536-91b0ae9927aa.png)

- Also install psycopg2 and after update requirements.txt file:

![image](https://user-images.githubusercontent.com/48124466/80263795-ba274a00-8689-11ea-9b8e-28897c154edf.png)

- In settings.py, import dj_database_url:

![image](https://user-images.githubusercontent.com/48124466/80264264-7cc3bc00-868b-11ea-81fa-0556df034caf.png)

- In settings.py, add dj_database_url to databases (I have used an env variable to store my DATABASE_URL):

![image](https://user-images.githubusercontent.com/48124466/80264126-ef806780-868a-11ea-8c23-184d0e3d30e2.png)

- run pip3 manage.py makemigrations
- run pip3 manage.py migrate
    - migrates all existing migrations to the new Postgres database.

- Create a new superuser:

![image](https://user-images.githubusercontent.com/48124466/80264234-63bb0b00-868b-11ea-910b-12595b3f9c80.png)

- The SQLite database which ran locally on your own machine was used for testing. You will have to rebuild your 
    items in the new production database.


## AWS S3 Buckets
### Setting It Up
- Go to [AWS](https://aws.amazon.com/) and create an account or sign in.
- Go to Management Console > S3 > Properties > Static website hosting:

![image](https://user-images.githubusercontent.com/48124466/80266264-d976a500-8692-11ea-9785-2dafed834ce5.png)

- Go to Permissions > CORS Config:
    - Add new cors configuration.

![image](https://user-images.githubusercontent.com/48124466/80266546-56564e80-8694-11ea-8c37-4e1e08baf92e.png)

- Go to Permissions > Bucket Policy:
    - Add a new policy here.

![image](https://user-images.githubusercontent.com/48124466/80266596-869ded00-8694-11ea-863b-9b5de9651642.png)

- Go to IAM > Groups:
    - Create New Group.

![image](https://user-images.githubusercontent.com/48124466/80266698-25c2e480-8695-11ea-9b78-a8b8e7b09752.png)

- Go to IAM > Policies:
    - Select JSON and create policy.

![image](https://user-images.githubusercontent.com/48124466/80266743-6e7a9d80-8695-11ea-92f1-7cd54b91222f.png)

- Now the policy is made, need to add it to the group that was made earlier:
    - Go to IAM > Groups.
    - Permissions > Attach Policy and attach policy created.

![image](https://user-images.githubusercontent.com/48124466/80266858-0ed0c200-8696-11ea-91db-acfd9e7228ab.png)

- Go to IAM > Users:
    - Add User
    - Access type: Turn Programmatic access on.

![image](https://user-images.githubusercontent.com/48124466/80266882-3758bc00-8696-11ea-906c-c195c5b6127c.png)

- Choose Group that was created:

![image](https://user-images.githubusercontent.com/48124466/80266966-afbf7d00-8696-11ea-833a-f7125dcafcfa.png)

- Once that is done, you will get this message.  Download and store Excel file carefully as it contains your keys
    needed in your software.

![image](https://user-images.githubusercontent.com/48124466/80267086-4a1fc080-8697-11ea-88cd-1648415d00e3.png)


### Add S3 To Django
- Install django-storages and boto3 in your GitPod terminal:
    - Both of these are packages that will allow you to connect Django to S3.

![image](https://user-images.githubusercontent.com/48124466/80267271-bc90a080-8697-11ea-9271-e617246366ff.png)

![image](https://user-images.githubusercontent.com/48124466/80267282-cb775300-8697-11ea-8560-b104d0ce91aa.png)

- In settings.py, add 'storages' to INSTALLED_APPS:

![image](https://user-images.githubusercontent.com/48124466/80267325-0ed1c180-8698-11ea-8a12-71c46a6b2dd7.png)

- In settings.py, add a setting in which will keep static files from expiring e.g.

![image](https://user-images.githubusercontent.com/48124466/80267379-6d973b00-8698-11ea-938e-4e79efe77ebd.png)

- In settings.py, you need to put in the AWS storage bucket name that you created in S3.
- Need to write which region you have used.
- You get your AWS access key and secret key from your environment variables e.g.

![image](https://user-images.githubusercontent.com/48124466/80267471-1180e680-8699-11ea-8065-abbd8ed3794a.png)

- The domain that you can use is something as follows, where your AWS Storage bucket 
    name is injected in there:

![image](https://user-images.githubusercontent.com/48124466/80267526-6c1a4280-8699-11ea-82ac-ba8d018555d5.png)

- You will have to tell it that the static file storage is storages:

![image](https://user-images.githubusercontent.com/48124466/80267557-86ecb700-8699-11ea-82b7-dc87915ff6d8.png)

- In the terminal- python3 manage.py collectstatic
    - Will transfer the static folder into S3

![image](https://user-images.githubusercontent.com/48124466/80269074-8574bc00-86a4-11ea-9148-c2d0227dcbd6.png)


### Add Media to S3
- This is a way of storing media files as well as static files on S3.
- Use STATICFILES_LOCATION from settings.py as the location.

![image](https://user-images.githubusercontent.com/48124466/80269142-f7e59c00-86a4-11ea-9539-b4a55d4d3909.png)

- In settings.py, add STATICFILES_LOCATION and give it a value 'static'.
- Change STATICFILES_STORAGE to custom_storages.StaticStorage.

![image](https://user-images.githubusercontent.com/48124466/80269268-14ce9f00-86a6-11ea-8dd7-fff076fee14d.png)

- In the terminal, run collectstatic and it will put a static directory in S3:

![image](https://user-images.githubusercontent.com/48124466/80269294-56f7e080-86a6-11ea-9eb8-d547537885ac.png)

- Refresh S3 Bucket:

![image](https://user-images.githubusercontent.com/48124466/80269306-7e4ead80-86a6-11ea-9e5f-669064484e76.png)

- In settings.py, MEDIAFILES_LOCATION will be media.
- DEFAULT_FILE_STORAGE will refer to the custom storages.py.

![image](https://user-images.githubusercontent.com/48124466/80269331-bce46800-86a6-11ea-9992-ca8003351062.png)
#


## Deployment
This application was deployed using Heroku which can be viewed from here: 
[Ted's Books Online](https://teds-books-online.herokuapp.com/)

I have used GitPod to build this application.  This was pushed to Heroku through the command line by linking 
the master git from my remote GitHub repository to a new app created in Heroku.

There are no differences between the website's development version and the deployed version to Heroku.

### Deploying to Heroku:
1. Go to the Heroku website [here](https://id.heroku.com/login).
2. Sign Up or Sign In which will direct you to the dashboard.
3. Click on **New > Create new app**.
4. Enter app name and choose region then press **Create App**.
5. Go to **Settings > Reveal Config Vars**:
    - Enter Keys and their values, example keys below:

    ![image](https://user-images.githubusercontent.com/48124466/80265160-80a50d80-868e-11ea-8db7-abec798f40cf.png)
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
### Travis CI
- At the top of this document, you will see Travis in action.
- It is a hosted continuous integration service used to build and test software projects.

### Django Testing
- I have carried out Django tests across a few apps in forms.py.

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
I have carried out manual tests on the functionality of the website.

The tests carried out involve:
- Search Box
- Dropdowns
- Adding Items to Cart, Edit Quantity and Remove Item from Cart
- Register/Sign In/Logout
- Book Details Page
- Checkout Form and Transactions
- Forum
- Social Media Links
- Password Reset
    - Demo for Password Reset:

    ![Password Reset](testing/demo/ResetPassword.gif)

[Manual Tests](https://github.com/terencecistudent/teds-books-online/blob/master/testing/Manual%20Tests.pdf)

### Responsiveness On Different Devices Tests:
I have carried out tests where I show my application being responsive on Google Chrome's laptop, iPad and
iPhone 6/7/8 views.

[Responsive Tests](https://github.com/terencecistudent/teds-books-online/blob/master/testing/Responsiveness%20On%20Different%20Devices.pdf)

### Running Responsive Designs on Google Chrome:
Here is a link how to run the application on a live server by configuring and exposing ports with GitPod:
https://www.gitpod.io/docs/43_config_ports/

**To view responsive applications:**
1. Right click then go to **Inspect Element**
2. Click on the **Toggle Device Toolbar** (Icons showing two devices):

![image](https://user-images.githubusercontent.com/48124466/68051275-f2ebf500-fcde-11e9-8b3a-adc7abc16c5f.png)

3. Click on any device, for example, iPhone 5/SE selected:

![image](https://user-images.githubusercontent.com/48124466/68051467-5aa24000-fcdf-11e9-8666-d29f1afa8955.png)


### Code Validation
- HTML
    - is validated using [W3 validator](https://validator.w3.org/).
- CSS
    - is validated using [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).
- JavaScript
    - is validated using [JS Hint](https://jshint.com/).
- Python
    - is validated using [Pep8Online](http://pep8online.com/).
#


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


## Cloning and Pushing To The Respository
### Cloning:
- Here is a link how to clone a repository: 
https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

### Pushing To The Respository:
- To add, commit and push files to the repository, e.g. index.html, open a New Terminal and type:
1. git add index.html
2. git commit -m "Leave a message here"
3. git push origin master - (which is for the master branch).

- To create a new branch within your current application, open a New Terminal:
1. Create a branch: git checkout -b new-branch-name
2. Edit, add to your application and commit the files.
3. Push the branch to the remote repository: git push origin new-branch-name.
#


## Bugs and Fixes
- Filter section in the Books page:
    - My inital idea was the change the value of the button however when clicked, the page would refresh.
        I created a div below the dropdowns where the HTML text of a dropdown value would be added.
        In my main.js file, I created an Array object which stored the value of each path name.  I then
        created a for loop which matched these paths.
- Quantity of 0 being added to cart:
    - When a user entered 0 in the quantity input then added to cart, the site would break.  I then set the the 
        input value being used for the quanity to 1.  This way all the customer would have to do is simply click 
        **Add to Cart** unless they wanted a higher quantity.  I tested this input after putting in a value.  When 
        0 is added to card, a simple error message displays saying that the quantity must be 1 or higher.
- Gmail's Reset Password:
    - For this I started off by adding email settings in settings.py apart from my own personal email.  I deployed 
        my project to Heroku, tested the password reset email and had no luck.  I carried out some research and got 
        help with tutor support.  I then added my email to my env file calling it in the settings.py file.  I also
        adding my email account details to Heroku's Config Var.  I turned on Allow Less Secure Apps in my Google
        account.  I then found a link to unluck captcha in my Google Account, which has fixed this problem for me.
#


## RoadMap
In the future, I would like to implement:
- A smoother and more eye catching design/layout for user UI.
- Dropdown searches to relate e.g. Genre selected Sports, then selected Price Low-High.
    - The Sport book with the lowest price would display.
- A remove cart item which removes all items from the cart.
- To create a profile model which when the user is online, their details are automatically shown on the
    payment form.
- In the user profile page, a section for the user to update their details.
- A price range for books so it will display books within a certain price.
- Delivery dates and refunds.
- A more maintenable and scalable way to show the dropdown filter's value. (Bugs and Fixes)
- Keep customer items in cart when they log out if they have an account.
#


## Support
To contact GitHub, follow this link: https://support.github.com/
#


## Credits
### Media:
- I got the background image from a free open sourced website: https://www.pexels.com/.
- For the uploaded images in my database, I used [Mumble Books](https://mumblebooks.co.uk/).

### Book Information:
- Book information was researched from [Mumble Books](https://mumblebooks.co.uk/).
- Book: Gordon Ramsay's Ultimate Fit Food was researched from
    [Amazon](https://www.amazon.co.uk/Gordon-Ramsay-Ultimate-Food-Mouth-watering-ebook/dp/B073BQJWRF/ref=sr_1_1?crid=1EB4L6ZFNCFA2&dchild=1&keywords=gordon+ramsay+ultimate+fit+food&qid=1587783464&sprefix=gordon+ramsay%27s+ult%2Caps%2C214&sr=8-1).

### Authors and Acknowledgment:
- **Autor**: Terence Logue
- **Acknowledgment**: Code Institute Slack, Code Institute Tutor Support, Assigned Mentor: Maranatha Ilesanmi
