![Logo](/documentationfiles/logo2.webp)
# Thrill Seeker API Readme

This is the Django Rest API for the Thrill Seeker website. The website provides you with articles about theme parks. Here the parks are rated and tips and recommendations are given for which target group the park is suitable. 

All other relevant files can be found here: <br>
[Live website](https://thrill-seekers-af06984a9bdb.herokuapp.com/) <br>
[Repository](https://github.com/SureDeveloping/thrill-seekers) <br>
[APi](https://thrill-seekers-api-5fd87044d4ac.herokuapp.com/) <br>
[API Repository](https://github.com/SureDeveloping/thrill-seeker-drf-api) <br>

## Content
- [Backend userstory](#backend-userstory)
- [Database](#database)
  * [Bucketlist](#bucketlist)
  * [Contact Form](#contact-form)
  * [Likes](#likes)
  * [Parks](#parks)
  * [Profiles](#profiles)
  * [Ratings](#ratings)
- [API endpoints](#api-endpoints)
- [Technology used](#technology-used)
  * [Languages](#languages)
  * [Frameworks](#frameworks)
  * [Database](#database)
  * [Libraries and packages](#libraries-and-packages)
  * [Software and tools](#software-and-tools)
- [Bugs](#bugs)
  * [Known bugs](#known-bugs)
  * [Fixed bugs](#fixed-bugs)
- [Testing](#testing)
- [Deployment](#deployment)
  * [Preparation for heroku depolyment](#preparation-for-heroku-depolyment) 
  * [Deploying on heroku](#deploying-on-heroku) 
  * [Fork this repository](#fork-this-repository) 
  * [Clone this repository](#clone-this-repository) 
  * [Run this project locally](#run-this-project-locally) 
- [Credits](#credits) 
  * [Content](#content) 
  * [Media](#media) 
  * [Code](#code) 
- [Acknowledgments](#acknowledgments) 

## Backend userstorys
To monitor the work, the following user story was created to create the backend. 

| Epic        | User Story                                                                                                                                         | Acceptance Cretary                                                                                                                                                                                                                                  | Tasks                                                                                                                        | Moscow      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Backend_API | As an admin, I need a stable API backend for my website to process the data entered on my website so I can connect the frontend to it.             | AC1: The repository  with all necessary libraries was set up.                                                                                                                                                                                       | T1: Create a repository and install all necessary libraries.<br>T2: Connected database to the backend                        | Must have   |
| Backend_API | As an admin, I need a model serializer view and urls for the parks app so I can connect it to the frontend.                                        | AC1: The backend for the park app works on the local server and on the deployed heroku version.<br>AC2: The CRUD function is working.                                                                                                               | T1: Create the model<br>T2: Create the view<br>T3: Create the serializer<br>T4: Create the URLs<br>T5: Test the app          | Must have   |
| Backend_API | As an admin I need a model serializer view and urls for the Bucketlist app so i can connect it to the frontend.                                    | AC1: The backend for the bucketlist app works on the local server  and on the deployed heroku version                                                                                                                                               | T1: Create the model<br>T2: Create the view<br>T3: Create the serializer<br>T4: Create the URLs<br>T5: Test the app          | Must have   |
| Backend_API | As an admin I need a model serializer view and urls for the rating app  so i can connect it to the frontend.                                       | AC1: The backend for the rating app works on the local server  and on the deployed heroku version                                                                                                                                                   | T1: Create the model<br>T2: Create the view<br>T3: Create the serializer<br>T4: Create the URLs<br>T5: Test the app          | Must have   |
| Backend_API | As an admin I need a model serializer view and urls for the like app  so i can connect it to the frontend.                                         | AC1: The backend for the like app works on the local server and on the deployed heroku version                                                                                                                                                      | T1: Create the model<br>T2: Create the view<br>T3: Create the serializer<br>T4: Create the URLs<br>T5: Test the app          | Could have  |
| Backend_API | As an admin, I need a model serializer view and urls for the contact form app so i can connect it to the frontend.                                 | AC1: The backend for the userprofile app works on the local server and on the deployed heroku version also for not loggin users.<br>AC2: I can CRUD the contact form data. Review the data , update, delete it only right after i created the form. | T1: Create the model<br>T2: Create the view<br>T3: Create the serializer<br>T4: Create the URLs<br>T5: Test the app          | Could have  |
| Backend_API | As an admin, I need a model serializer view and urls for the userprofile app so I can connect the frontend to it.                                  | AC1: The backend for the userprofile app works on the local server and on the deployed heroku version.                                                                                                                                              | T1: Create the model<br>T2: Create the view<br>T3: Create the serializer<br>T4: Create the URLs<br>T5: Test the app          | Could have  |
| Backend_API | As admin, I want to make sure that only the owner of a user profile can change it and has to authenticate himself to prevent unauthorized changes. | AC1: The backend for the user authentication is working.<br>AC2: Only owners of a profile can change this<br>AC3: Every not loggin user can read all profiles.                                                                                      | T1: Add authentication and permission functions to the profiles app.<br>T2: Test the authentication and permission function. | Must have   |
| Backend_API | As a user, I would like to see all my bucketlist items that I can plan my next park visit.                                                         | AC1: In the backend, a field indicates whether a park is on a user's bucketlist.<br>AC2: There is a field on my profile that shows the number of my bucketlist items.                                                                               | T1:  Add bucketlist count                                                                                                    | Should have |
| Backend_API | As a user, I would like to see all my set likes that I can read the corresponding ratings again.                                                   | AC1: In the backend, a field indicates whether a rating is liked by a user.<br>AC2: There is a field on my profile that shows the number of my likes.                                                                                               | T1:: Add like count                                                                                                          | Should have |
| Backend_API | As a user, I would like to see all my ratings that I can update them with new experiences.                                                         | AC1: In the backend, a field indicates whether a park is rated by a user.<br>AC2: There is a field on my profile that shows the number of my ratings.                                                                                               | <br>T1: Add ratings count                                                                                                    | Should have |
| Backend_API | As a user, I would like to search the parks by the name to find a park faster if it exists.                                                        | <br>AC1: I can search parks by name, author (username), country.                                                                                                                                                                                    | T1: Add search function                                                                                                      | Should have |
| Backend_API | As a user, I would see ratings and bucketlist count on the park page to get a better opinion on that park.                                         | AC1: The bucketlist count is on the park backend page.<br>AC2: The rating count is on the parks backend page.                                                                                                                                       | T1: Add bucketlist count<br>T2: Add rating count                                                                             | Should have |

## Database
This ERD Entity-Relationship Diagramm was created for the Thrill Seeker project. All the models serve the project goal and contribute to its success with their functions.
![Entity Relationship Diagramm](./documentationfiles/ERD.png)

### Bucketlist: 
This model is a list of parks that a user would like to visit. In other words, a watch list for a later date.  It is linked to the user model and the park model. 

### Contact Form: 
Visitors to the website can use the contact form model to send a message that is saved. The model contains first_name, last_name, email, subject, message, last_updated and an edit_token. This allows the data to be updated once, after the user has checked it. The edit token is used for verification and to secure the model against misuse.

### Likes: 
This model contains the Likes. These can be created by logged-in users for ratings. It is connected to the user models via and to the rating via a foreign key. It also contains a "created at" field. The Likes app is not yet available in the front. For the future, this has been integrated into the backend so that this function can be added quickly.

### Parks: 
The park model presents the articles that can be created by super users (is staff) and it is linked to the user as a foreign key. It contains the name of the park, a description, a picture, the number of rides, the number of roller coasters, the thrill factor, the overall rating and the website of the park. 

### Profiles: 
The Profiles model extends the user model with additional information such as favorite-park, favorite_ride userbio, profile_picture and timestamps for created-at and updated_at. The user profile is created automatically when a user is created.

### Ratings:
This model represents ratings that can be submitted by users who are logged in. 
It is linked to the user model and the parking model via a foreign key. It also contains a rating as an integer field, a reason for this rating, created at, updated at and last visited field. 

## API Endpoins
The following table provides an overview of all API endpoints. It also includes the HTTP Metod, CRUD Operation and View Type with a short description.

| Root Route     | Endpoint                     | HTTP Method | CRUD Operation | View Type           | Description                                                                     |
| -------------- | ---------------------------- | ----------- | -------------- | ------------------- | ------------------------------------------------------------------------------- |
|                | /                            | GET         | Read           | Function-based view | Root route                                                                      |
| Authentication |                              |             |                |                     |                                                                                 |
|                | /admin/                      | GET         | Read           | Django Admin        | Django admin interface                                                          |
|                | /dj-rest-auth/logout/        | POST        | Delete         | Function-based view | Custom logout route                                                             |
|                | /dj-rest-auth/login/         | POST        | Create         | DRF built-in view   | User login                                                                      |
|                | /dj-rest-auth/user/          | GET         | Read           | DRF built-in view   | Get current user details                                                        |
|                | /dj-rest-auth/user/          | PUT         | Update         | DRF built-in view   | Update current user details                                                     |
|                | /dj-rest-auth/registration/  | POST        | Create         | DRF built-in view   | User registration                                                               |
|                |                              |             |                |                     |                                                                                 |
| Bucketlist     |                              |             |                |                     |                                                                                 |
|                | /bucketlist/                 | GET         | Read           | ListAPIView         | List all bucketlist items                                                       |
|                | /bucketlist/                 | POST        | Create         | CreateAPIView       | Create a new bucketlist (authenticated users only)                              |
|                | /bucketlist/{id}/            | GET         | Read           | RetrieveAPIView     | Retrieve a specific bucketlist                                                  |
|                | /bucketlist/{id}/            | DELETE      | Delete         | DestroyAPIView      | Delete a specific bucketlist item (owner only)                                  |
|                |                              |             |                |                     |                                                                                 |
| Contact Form   |                              |             |                |                     |                                                                                 |
|                | /contact/                    | GET         | Read           | ListAPIView         | List all contact form messages                                                  |
|                | /contact/create/             | POST        | Create         | CreateAPIView       | Create a new contact message                                                    |
|                | contact/update/{edit_token}/ | GET         | Read           | RetrieveAPIView     | Retrieve the just created contact message authenticated via a unique edit_token |
|                | contact/update/{edit_token}/ | PUT         | Update         | UpdateAPIView       | Update the just created contact message. authenticated via a unique edit_token  |
|                | contact/update/{edit_token}/ | DELETE      | Delete         | DestroyAPIView      | Delete the just created contact message. authenticated via a unique edit_token  |
|                |                              |             |                |                     |                                                                                 |
| Likes          |                              |             |                |                     |                                                                                 |
|                | /likes/                      | GET         | Read           | ListAPIView         | List all likes                                                                  |
|                | /likes/                      | POST        | Create         | CreateAPIView       | Create a new like (authenticated users only)                                    |
|                | /likes/{id}/                 | GET         | Read           | RetrieveAPIView     | Retrieve a specific like                                                        |
|                | /likes/{id}/                 | DELETE      | Delete         | DestroyAPIView      | Delete a specific like (owner only)                                             |
|                |                              |             |                |                     |                                                                                 |
| Parks          |                              |             |                |                     |                                                                                 |
|                | /parks/                      | GET         | Read           | ListAPIView         | Retrieve a list of parks                                                        |
|                | /parks/                      | POST        | Create         | CreateAPIView       | Create a new park                                                               |
|                | /parks/{id}/                 | GET         | Read           | RetrieveAPIView     | Retrieve a specific park by ID                                                  |
|                | /parks/{id}/                 | PUT         | Update         | UpdateAPIView       | Update a specific park by ID                                                    |
|                | /parks/{id}/                 | DELETE      | Delete         | DestroyAPIView      | Delete a specific park by ID                                                    |
|                |                              |             |                |                     |                                                                                 |
| Profiles       |                              |             |                |                     |                                                                                 |
|                | /profiles/                   | GET         | Read           | ListAPIView         | List all profiles (logged in users)                                             |
|                | /profiles/{id}/              | GET         | Read           | RetrieveAPIView     | Retrieve a specific profile (logged in users)                                   |
|                | /profiles/{id}/              | PUT         | Update         | UpdateAPIView       | Update a specific profile (owner only)                                          |
|                |                              |             |                |                     |                                                                                 |
| Ratings        |                              |             |                |                     |                                                                                 |
|                | /ratings/                    | GET         | Read           | ListAPIView         | List all ratings                                                                |
|                | /ratings/                    | POST        | Create         | CreateAPIView       | Create a new rating (authenticated users only)                                  |
|                | ratings/{id}/                | GET         | Read           | RetrieveAPIView     | Retrieve a specific rating                                                      |
|                | /ratings/{id}/               | PUT         | Update         | UpdateAPIView       | Update a specific rating (owner only)                                           |
|                | /ratings/{id}/               | DELETE      | Delete         | DestroyAPIView      | Delete a specific rating (owner only)                                           |


## Technologies used
### Languages
Frondend: <br>
- HTML
- CSS
- Python
- JSX (JavaScript XML)
- Markdown

Backend: <br>
- Python
- Markdown

### Frameworks
Frondend: <br>
- React: JavaScript library for creating the Fontend user interfaces. 
- React-bootstrap: Front-end framework, rebuilt for React with a collection of HTML, CSS, and JavaScript components.

Backend: <br>
- Django rest framework was used for the API of this project.

### Database
- The PostgreSQL database from Code Institute was used as the database.

### Libraries and packages
Backend: <br>
- asgiref==3.3.4 - ASGI (Asynchronous Server Gateway Interface) specification, used by Django for asynchronous support
- certifi==2024.6.2 - A collection of root certificates for SSL/TLS verification
- cffi==1.16.0 - C Foreign Function Interface for Python.
- charset-normalizer==3.3.2 - Library for character encoding detection
- cloudinary==1.33.0 - Python SDK for Cloudinary, a cloud service for image and video management
- cryptography==3.4.8 - Library for various cryptographic operations
- defusedxml==0.7.1 - XML bomb protection for Python stdlib modules
- dj-database-url==0.5.0 - Utility to configure Django Database using URLs
- dj-rest-auth==2.1.9 - Authentication views for Django REST Framework
- Django==3.2.4 - The core Django web framework
- django-allauth==0.44.0 - Integrated set of Django applications addressing authentication, registration, account management
- django-cloudinary-storage==0.3.0 - Django package that provides Cloudinary storages for both media and static files
- django-cors-headers==3.7.0 - Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS)
- django-filter==2.4.0 - Django application for allowing users to filter querysets dynamically
- django-resized==1.0.2 - To resize uploaded images
- djangorestframework==3.12.4 - Powerful and flexible toolkit for building Web APIs in Django
- djangorestframework-simplejwt==4.7.2 - JSON Web Token authentication plugin for Django REST Framework
- gunicorn==20.1.0 - Python WSGI HTTP Server for UNIX, often used to deploy Django applications
- idna==3.7 - Internationalized Domain Names in Applications (IDNA) support
- oauthlib==3.1.1 - Generic, spec-compliant implementation of OAuth for Python
- Pillow==8.2.0 - Python Imaging Library (Fork), for opening, manipulating, and saving many different image file formats
- psycopg2==2.9.1 - PostgreSQL adapter for Python
- pycparser==2.22 - C parser in Python, required by some Python packages that interface with C code
- PyJWT==2.1.0 - JSON Web Token implementation in Pytho
- python3-openid==3.2.0 - OpenID support for modern servers and consumers
- pytz==2021.1 - World timezone definitions for Python
- requests==2.32.3 - HTTP library for Python
- requests-oauthlib==1.3.0 - OAuthlib authentication support for Requests
- six==1.16.0 - Python 2 and 3 compatibility library
- sqlparse==0.4.1 - Non-validating SQL parser for Python
- urllib3==1.26.19 - Python HTTP library that provides connection pooling, SSL/TLS support, and error handling

Frontend: <br>
- axios@0.21.4 - Promise-based HTTP client for making API requests.
- bootstrap@4.6.0 - CSS framework for responsive web design.
- jwt-decode@3.1.2 - Decodes JSON Web Tokens
- msw@0.35.0 - Core React library.
- react-bootstrap@1.6.3 - React components for Bootstrap.
- react-dom@17.0.2 - React package for working with the DOM.
- react-infinite-scroll-component@6.1.0 - react-infinite-scroll-component: Component for implementing infinite scroll functionality.
- react-router-dom@5.3.0 - Routing library for React applications.
- react-scripts@4.0.3 - Scripts and configuration used by Create React App.
- react-star-ratings@2.3.0 - Component for displaying star ratings.
- react@17.0.2 - Library for measuring web vitals metrics.
- web-vitals@1.1.2 - Mock Service Worker for API mocking in tests.
- jwt-decode: "^3.1.2", - to add token refresh fix


### Software and tools
- Balsamiq - To create a wireframe.
- Draw-io - To create an ERD.
- Gitpod - IDE to code the project
- Git - For version control.
- Github - To store the website.
- Gitpod - As an integrated development environment to write the code.
- Heroku - To deploy the website.
- Google Fonts - All fonts used are from google fonts.
- Google Dev Tools, and Lighthouse - For troubleshooting testing and fixing bugs.
- Deepl - For translating text.
- Birme - To change the image to webp format and reduce the size of the images.
- Tabletomarkdown.com - Used to Create table for markdown out of excel cheats.
- ChatGPT - To generate text content for the website.
- Microsoft Excel - To pre create tables for the readme.
- Pep8 CI Python Linter - To Linter the Python
- W3C HTML Validator - To validate the HTML code.
- W3C CSS Validator - To validate the CSS code.
- JS Hint - To detect errors and potential problems in JavaScript code.
- Cloudinary - Media management platform to save and provide images.
- Font Awesome - To provide icons for the project.


## Bugs
### Known bugs
- No unresolved known errors in the backend.

### Fixed bugs 
- I had the error “django.db.utils.IntegrityError: UNIQUE constraint failed: ratings_rating.user_id, ratings_rating.park_id. It was because there was already old data in the database. This has led to a conflict, an error with UNIQUE. The solution was to empty the database and delete the old data.

## Testing
The tests for the Thrill Seeker Api are listed in a separate file. This file can be found here. [TESTING.md](./TESTING.md)


## Deployment
The project was coded with Gipod and then deployed on Heroku.

### Preparation for heroku depolyment
* Make sure the requirements.txt are up to date - command pip3 freeze > requirements.txt.
* Create a procfile for the configuration of the Heroku deployment as a Gunicorn web application.
* Set ALLOWED_HOSTS, CLIENT_ORIGIN, CLIENT_ORIGIN_DEV in settings.py.
* Set the local environment variables, env.py file for the PostgreSQL URL, the Cloudinary URL and the secret Django key. 
* Set DEBUG in the settings.py file to False to ensure that the application runs in production mode during deployment. 
* Make migrations to have the latest models in the database schema. 
* Commit and push all changes to the GitHub repository.


### Deploying on heroku
* Log in to your Heroku account.
* Click on the NEW button and then on "create new app".
* Choose a unique name for the app.
* Choose a region, Europe or United States.
* Click on "create app."
* Choose the deployment method (For this project GitHub was used).
* Search for the repository name on GitHub ("thrill-seeker-drf-api").
* Connect the repository by clicking on Connect
* Click on the settings tab and then on reveal config vars.
* Input the required hidden variables
* Choose Node.js and Python as the designated buildpacks.
* Click on the Deployment tab
* Choose the main branch
* Deploy this project automated or manual (the project was deployed manually)
* Once a deployment has been successfully completed, a success message is displayed and a view button can be used to view the project in the browser.

### Fork this repository
* Visit the GitHub repository.
* Click on the Fork button, located in the upper right-hand corner, next to the star button.
* Once the forking process is complete, a copy of the repository is created in the GitHub account.

### Clone this repository
* Visit the GitHub repository. [repository](https://https://github.com/SureDeveloping/thrill-seeker-drf-api)
* Click the Code button, located in the top right, next to the About page.
* Choose between 'HTTPS', 'SSH', or 'GitHub CLI' based on your preferred method for cloning.
* Copy the URL.
* Open Git Bash.
* Choose the location where the cloned directory will be saved.
* Type git clone and paste the URL ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
* Press enter to create the local clone.

### Run this project locally
* Visit the GitHub repository. [repository](https://https://github.com/SureDeveloping/thrill-seeker-drf-api)
* Click the Code button, located in the top right, next to the About page.
* Click on download Zip.
* After downloding, open the zip file and run it an editor.
* Create an env.py file for the environment variables.
* Install PostgreSQL on your machine and open the ports.
* Create a virtual environment and install the Python modules in the pip file.
* Run python3 makemigrations, migrate and runserver


## Credits
### Content
The content of the website was created by Stephan Sure with the assistance of Chat GPT, Wikipedia and the websites of the amusement parks. 

### Media
The used images are from different websites. I explained this already in the design section more deeply.
Here are my image resources:
- [Freepiks](https://de.freepik.com/)
- [Pexels](https://www.pexels.com/de-de/)
- [Wikipedia](https://www.wikipedia.org/)

The used fonts are googlefonts:
- [googlefonts](https://fonts.google.com/) 

The logo and favicon is created logo:
- [Logo](https://logo.com/)

The used icons are from:
- [Fontawesome](https://https://fontawesome.com/icons/)


### Code
* CI Drango REST FRAMEFORK - API walkthrough - for the backend, especially for setting up the project
* CI codestar mouments walkthrough - especially for setting up the project
* [Stack overflow](https://stackoverflow.com/) -  in general for all questions about code.
* [React bootstrap](https://react-bootstrap.netlify.app/) - all questions about react bootstrap.
* [5 star rating](https://medium.com/@Vaibhavihole31/creating-a-star-rating-bar-in-reactjs-a3f66456d7bb) - for the 5 star rating
* [5 star rating](https://medium.com/@codeyourthoughts48/add-star-ratings-in-reactjs-33a720bff3a1) - for the 5 star rating
* [Axios react](https://www.freecodecamp.org/news/axios-react-how-to-make-get-post-and-delete-api-requests/) - detail information about axiox
* [Axios video](https://www.youtube.com/watch?v=6LyagkoRWYA) - detail information about axiox
* [React routing](https://blog.logrocket.com/react-router-dom-tutorial-examples/) - detail information about routing
* [404 page](https://www.digitalocean.com/community/tutorials/how-to-create-a-custom-404-page-in-apache) - code for the 404 page
* [Invisible content for screen readers](https://webaim.org/techniques/css/invisiblecontent/) - Invisible Content for Screen Readers, lable
* [React.lazy](https://www.freecodecamp.org/news/how-to-use-react-lazy-and-suspense-for-components-lazy-loading-8d420ecac58/
) - How to use React.lazy 
* [Forms in react](https://www.freecodecamp.org/news/how-to-build-forms-in-react/) - how to build forms in react
* [Styleing filter elements](https://css-tricks.com/almanac/properties/a/appearance/) - styleing filter elements

backend:
* [Django docs](https://www.djangoproject.com/) -  all questions about django.
* [Django rest framework](https://www.django-rest-framework.org/) -  all questions about django rest framework,e.g. Permissions, Models, Serializers, Signals, Forms
* [Token based auth](https://medium.com/django-unleashed/token-based-authentication-and-authorization-in-django-rest-framework-user-and-permissions-347c7cc472e9) - For the Contact Form edit token
* [Token based auth](https://www.bacancytechnology.com/blog/django-rest-framework-authentication) - Token based auth
* [Token based auth](https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html) - Token based auth

* [Token, universally unique identifier](https://datatracker.ietf.org/doc/html/rfc4122) - For the Contact Form edit token

* [Token, universally unique identifier](https://docs.python.org/3/library/uuid.html) - For the Contact Form edit token

* [Resizing images](https://www.codu.co/articles/resizing-images-and-converting-formats-in-django-1rj9kdho) - for resizing images in the backend 


## Acknowledgments
I like to thank the following persons for their help during the project:

- My Code Institute mentor, Spencer Barriball.
- The Tutor support team at Code Institute.
- Slack pear group and CI cohort.
- All the people who make their knowledge available for free.

This project is for educational use only and was created for the Code Institute course Full Stack Software Development by Stephan Sure.
