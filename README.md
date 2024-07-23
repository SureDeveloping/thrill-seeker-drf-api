![Logo](/documentationfiles/logo2.webp)
# Thrill Seeker API Readme

This readme provides information about the API endpoints and functionalities for Thrill Seeker website. 
All other relevant files can be found here:
[Live website]() Fehlt noch! <br>
[Repository](https://github.com/SureDeveloping/thrill-seekers) <br>
[APi](https://thrill-seekers-api-5fd87044d4ac.herokuapp.com/) <br>
[API Repository](https://github.com/SureDeveloping/thrill-seeker-drf-api) <br>

## Content
- [Backend Userstory](#backend-userstory)
- [Database](#database)
  * [Bucketlist](#bucketlist-)
  * [Contact](#contact)
  * [Likes](#likes)
  * [Parks](#parks)
  * [Profiles](#profiles)
  * [Ratings](#ratings)
- [Bugs](#bugs)
  * [Known bugs](#known-bugs)
  * [Fixed bugs](#fixed-bugs)
- [Testing](#testing)
  * [Languages](#languages)
  * [Frameworks](#frameworks)
  * [Database](#database-1)
  * [Tools](#tools)
  * [Supporting Libraries and Packages](#supporting-libraries-and-packages)
- [Deployment](#deployment)
- [Credits](#credits)   ???? Die gi

## Backend Userstorys

## Database
This ERD Entity-Relationship Diagramm was created for the Thrill Seeker project. All the models serve the project gole and contribute to its success with their functions.
![Entity Relationship Diagramm](/readmefiles/erd.png)
Das Userprofil muss ich noch mal Prüfen!!!

### Bucketlist: 
This model is a list of parks that a user would like to visit. In other words, a watch list for a later date.  It is linked to the user model and the park model. 

### Contact Form: 
Visitors to the website can use the contact form model to send a message that is saved. The model contains first_name, last_name, email, subject, message, last_updated and an edit_token. This allows the data to be updated once, after the user has checked it. The edit token is used for verification and secure the model against misuse.

### Rating:
This model represents ratings that can be submitted by users who are logged in. 
It is linked to the user model and the parking model via a foreign key. It also contains a rating as an integer field, a reason for this rating, created at, updated at and last visited field. 

### Like: 
This model contains the Likes. These can be created by logged-in users for ratings. It is connected to the user models via and to the rating via a foreign key. It also contains a "created at" field. The likes app is not yet available in the front. For the future, this has been integrated into the backend so that this function can be added quickly.

### Post: 
The park model presents the articles that can be created by super users (is staff) and it is linked to the user as a foreign key. It contains the name of the park, a description, a picture, the number of rides, the number of roller coasters, the thrill factor, the overall rating and the website of the park. 

### Traveler: 
The Profiles model extends the user model with additional information such as favorite-park, favorite_ride userbio, profile_picture and timestamps for created-at and updated_at. The user profile is created automatically when a user is created.


## Bugs
?????????????

### Known bugs
???????????????????????????

### Fixed bugs 
Here is a summary of the identified bugs along with brief descriptions of their fixes. luding the bug report, commits, and the steps taken to resolve the issue.??????????????????????????????????????????


## Testing
The tests for the Thrill Seeker Api are listed in a separate file. This file can be found here. [TESTING.md](https://github.com/SureDeveloping/thrill-seeker-drf-api/blob/main/TESTING.md).

### Languages
- Python
- Markdown

### Frameworks
The Django rest framework was used for the API of this project.

### Database
The PostgreSQL database from Code Institute was used as the database.

### Software and Tools
- Draw.io - To create the ERD
- Gitpod - IDE to code the project
- Git - For version control
- Heroku – to deploy the website
- Github - to store the website
- Excel - to create for the readme and the testing.md tabels
- Pep8 CI Python Linter - To Linter the python
- Cloudinary - For managing and saving images
- Code Institute Postgres Database - PostgreSQL database for this project


### Supporting Libraries and Packages
??????? Oder zusammen mit tools???

## Deployment
Deploying the Django backend :
It is assumed that user accounts exist for the respective services used and that usage rights are available.

1. Set DEBUG in the settings.py file to False to ensure that the application runs in production mode during deployment. 
2. Log in to the Heroku account, create a new Heroku app. and select a region.
3. Set the local environment variables, env.py file for the PostgreSQL URL, the Cloudinary URL and the secret Django key. These variables must also be added in the Heroku app under the Config Vars section. To communicate with the Heroku application. Avoid exposing your environment variables in your public repository. Use the Config Vars section in Heroku to securely set your environment variables.
4. Perform all database migrations and have the current state of the models in the database schema. Commit and push all changes to the GitHub repository. The commands python manage.py makemigrations and python manage.py migrate were used for this. 
4. In the Heroku dashboard, the created app is connected to the GitHub repository under the "Deployment method" section on the deployment page. The app is then deployed via "Manual deployment" by clicking the Deploy Branch button. After successful deployment, Heroku provides a URL for accessing the live application. 


## Credits ????
email senden für user profile???
edit token
[django-versatileimagefield - Custom filters](https://django-versatileimagefield.readthedocs.io/en/2.1/writing_custom_sizers_and_filters.html)