![Logo](/documentationfiles/logo2.webp)
# Thrill Seeker API Testing

The testing.md file provides an overview of all tests that have been carried out specifically with the Thrill Seeker API.

## Content
- [Code Validation](#code-validation)
- [Manual testing](#manual-testing)
- [Resume](#resume)


### Code Validation 
The python code of the backend was checked by a Pyton linter. The code Institute python linter was used for this purpes.
[CI Python Linter](https://pep8ci.herokuapp.com/) 

#### Backend
| Tested File    | Test Result                                                                                                             | Pass            |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------- |
| permissions.py | <details><summary>backend permissions</summary><img src="./documentationfiles/testing/backend/permissions.png"></details> | Pass, No errors |
| serializers.py | <details><summary>backend serializers</summary><img src="./documentationfiles/testing/backend/serializers.png"></details> | Pass, No errors |
| settings.py    | <details><summary>backend settings</summary><img src="./documentationfiles/testing/backend/settings.png"></details>    | Pass, No errors |
| urls.py        | <details><summary>backend urls</summary><img src="./documentationfiles/testing/backend/urls.png"></details>        | Pass, No errors |
| views.py       | <details><summary>backend views</summary><img src="./documentationfiles/testing/backend/views.png"></details>       | Pass, No errors |

#### Bucketlist
| Tested File    | Test Result                                                                                                             | Pass            |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------- |
| models         | <details><summary>bucketlist models</summary><img src="./documentationfiles/testing/bucketlist/models.png"></details>   | Pass, No errors |
| serializers.py | <details><summary>bucketlist serializers</summary><img src="./documentationfiles/testing/bucketlist/serializers.png"></details> | Pass, No errors |
| urls.py        | <details><summary>bucketlist urls</summary><img src="./documentationfiles/testing/bucketlist/urls.png"></details>     | Pass, No errors |
| views.py       | <details><summary>bucketlist views</summary><img src="./documentationfiles/testing/bucketlist/views.png"></details>    | Pass, No errors |


#### Contact Form
| Tested File    | Test Result Screenshot                                                                                                    | Result          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------- |
| models         | <details><summary>contact_form models</summary><img src="./documentationfiles/testing/contact_form/models.png"></details>   | Pass, No errors |
| serializers.py | <details><summary>contact_form serializers</summary><img src="./documentationfiles/testing/contact_form/serializers.png"></details> | Pass, No errors |
| urls.py        | <details><summary>contact_form urls</summary><img src="./documentationfiles/testing/contact_form/urls.png"></details>     | Pass, No errors |
| views.py       | <details><summary>contact_form views</summary><img src="./documentationfiles/testing/contact_form/views.png"></details>    | Pass, No errors |


#### Rating
| Tested File    | Test Result Screenshot                                                                                              | Result          |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | --------------- |
| models         | <details><summary>rating models</summary><img src="./documentationfiles/testing/rating/models.png"></details>   | Pass, No errors |
| serializers.py | <details><summary>rating serializers</summary><img src="./documentationfiles/testing/rating/serializers.png"></details> | Pass, No errors |
| urls.py        | <details><summary>rating url</summary><img src="./documentationfiles/testing/rating/urls.png"></details>     | Pass, No errors |
| views.py       | <details><summary>rating view</summary><img src="./documentationfiles/testing/rating/views.png"></details>    | Pass, No errors |

#### Like
| Tested File    | Test Result Screenshot                                                                                            | Result          |
| -------------- | ----------------------------------------------------------------------------------------------------------------- | --------------- |
| models         | <details><summary>like models</summary><img src="./documentationfiles/testing/like/models.png"></details>   | Pass, No errors |
| serializers.py | <details><summary>like serializers</summary><img src="./documentationfiles/testing/like/serializers.png"></details> | Pass, No errors |
| urls.py        | <details><summary>like urls</summary><img src="./documentationfiles/testing/like/urls.png"></details>     | Pass, No errors |
| views.py       | <details><summary>like views</summary><img src="./documentationfiles/testing/like/views.png"></details>    | Pass, No errors |


#### Park
| Tested File    | Test Result Screenshot                                                                                            | Result          |
| -------------- | ----------------------------------------------------------------------------------------------------------------- | --------------- |
| models         | <details><summary>park models</summary><img src="./documentationfiles/testing/park/models.png"></details>   | Pass, No errors |
| serializers.py | <details><summary>park serializers</summary><img src="./documentationfiles/testing/park/serializers.png"></details> | Pass, No errors |
| urls.py        | <details><summary>park urls</summary><img src="./documentationfiles/testing/park/urls.png"></details>     | Pass, No errors |
| views.py       | <details><summary>park views</summary><img src="./documentationfiles/testing/park/views.png"></details>    | Pass, No errors |


#### Profile
| Tested File    | Test Result Screenshot                                                                                               | Result          |
| -------------- | -------------------------------------------------------------------------------------------------------------------- | --------------- |
| models         | <details><summary>profile models</summary><img src="./documentationfiles/testing/profile/models.png"></details>   | Pass, No errors |
| serializers.py | <details><summary>profile serializers</summary><img src="./documentationfiles/testing/profile/serializers.png"></details> | Pass, No errors |
| urls.py        | <details><summary>profile urls</summary><img src="./documentationfiles/testing/profile/urls.png"></details>     | Pass, No errors |
| views.py       | <details><summary>profile views</summary><img src="./documentationfiles/testing/profile/views.png"></details>    | Pass, No errors |



### Manual testing
Manual testing ensures that all apps and their endpoints work as planned and desired. All functions of the apps must work and the urls must be accessible. The search function must also work. This later ensures that users can use everything without any problems but only have access to data and functions where they are authorized.

#### Root Route
| Endpoint | Method | CRUD Operation | Description | Test Result Screenshot                                                                                                    | Expected Result                                                                        | Actual Result                                                                          | Result          |
| -------- | ------ | -------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------- |
| /        | GET    | Read           | Root route  | <details><summary>root route</summary><img src="./documentationfiles/testing/endpoint/root_rout/root-rout.png"></details> | Leads to root root with "message": "This is the API from the Thrill Seekers website.!" | Leads to root root with "message": "This is the API from the Thrill Seekers website.!" | Pass, No errors |


#### Authentication
| Endpoint                    | Method | CRUD Operation | Description                 | Test Result Screenshot                                                                                                            | Expected Result                              | Actual Result                             | Result          |
| --------------------------- | ------ | -------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------- | --------------- |
| /admin/                     | GET    | Read           | Django admin interface      | <details><summary>admin1</summary><img src="./documentationfiles/testing/endpoint/auth/admin.png"></details>                      | Admin interface loads successfully           | Admin interface loaded successfully       | Pass, No errors |
|                             |        |                |                             | <details><summary>admin2</summary><img src="./documentationfiles/testing/endpoint/auth/admin-logged-in.png"></details>            |                                              |                                           |                 |
| /dj-rest-auth/logout/       | POST   | Delete         | Custom logout route         | <details><summary>logout</summary><img src="./documentationfiles/testing/endpoint/auth/logout.png"></details>                     | User is logged out and session is terminated | User logged out successfully              | Pass, No errors |
| /dj-rest-auth/login/        | POST   | Create         | User login                  | <details><summary>login1</summary><img src="./documentationfiles/testing/endpoint/auth/login1.png"></details>                     | User is authenticated and receives a token   | User authenticated and received token     | Pass, No errors |
|                             |        |                |                             | <details><summary>login2</summary><img src="./documentationfiles/testing/endpoint/auth/login2.png"></details>                     |                                              |                                           |                 |
| /dj-rest-auth/user/         | GET    | Read           | Get current user details    | <details><summary>auth-user-read</summary><img src="./documentationfiles/testing/endpoint/auth/auth-user.png"></details>          | Returns current user's profile information   | Returned correct user profile information | Pass, No errors |
| /dj-rest-auth/user/         | PUT    | Update         | Update current user details | <details><summary>auth-user-update</summary><img src="./documentationfiles/testing/endpoint/auth/auth-user-update.png"></details> | User details are updated successfully        | User details updated correctly            | Pass, No errors |
| /dj-rest-auth/registration/ | POST   | Create         | User registration           | <details><summary>register1</summary><img src="./documentationfiles/testing/endpoint/auth/register1.png"></details>               | New user account is created                  | New user account created successfully     | Pass, No errors |
|                             |        |                |                             | <details><summary>register2</summary><img src="./documentationfiles/testing/endpoint/auth/register2.png"></details>               |                                              |                                           |                 |
|                             |        |                |                             | <details><summary>register3</summary><img src="./documentationfiles/testing/endpoint/auth/register3.png"></details>               |                                              |                                           |                 |


#### Bucketlist
| Endpoint          | Method | CRUD Operation | Description                                        | Test Result Screenshot                                                                                                                              | Expected Result                                                  | Actual Result                                         | Result          |
| ----------------- | ------ | -------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------- | --------------- |
| /bucketlist/      | GET    | Read           | List all bucketlist items                          | <details><summary>bucketlist-read-list</summary><img src="./documentationfiles/testing/endpoint/bucketlist/bucketlist-read-list.png"></details>     | Returns a list of all bucketlist items                           | Returned a list of all bucketlist successfully        | Pass, No errors |
| /bucketlist/      | POST   | Create         | Create a new bucketlist (authenticated users only) | <details><summary>bucketlist-create1</summary><img src="./documentationfiles/testing/endpoint/bucketlist/bucketlist-create1.png"></details>         | New bucketlist item is created and returned                      | New bucketlist item created and returned successfully | Pass, No errors |
|                   |        |                |                                                    | <details><summary>bucketlist-create2</summary><img src="./documentationfiles/testing/endpoint/bucketlist/bucketlist-create2.png"></details>         |                                                                  |                                                       |                 |
| /bucketlist/{id}/ | GET    | Read           | Retrieve a specific bucketlist                     | <details><summary>bucketlist-read-detail</summary><img src="./documentationfiles/testing/endpoint/bucketlist/bucketlist-read-detail.png"></details> | Returns a specific bucketlist item                               | Returned  the specified bucketlist item successfully  | Pass, No errors |
| /bucketlist/{id}/ | DELETE | Delete         | Delete a specific bucketlist item (owner only)     | <details><summary>bucketlist-delete1</summary><img src="./documentationfiles/testing/endpoint/bucketlist/bucketlist-delete1.png"></details>         | Deletes the specified bucketlist item by the authenticated owner | Bucketlist item deleted successfully                  | Pass, No errors |
|                   |        |                |                                                    | <details><summary>bucketlist-delete2</summary><img src="./documentationfiles/testing/endpoint/bucketlist/bucketlist-delete2.png"></details>         |                                                                  |                                                       |                 |




#### Contact Form
| Endpoint                     | Method | CRUD Operation | Description                                                                     | Test Result Screenshot                                                                                                               | Expected Result                             | Actual Result                                         | Result          |
| ---------------------------- | ------ | -------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------- | ----------------------------------------------------- | --------------- |
| /contact/                    | GET    | Read           | List all contact form messages                                                  | <details><summary>contact-list1</summary><img src="./documentationfiles/testing/endpoint/contact/contact-list1.png"></details>       | Superuser (is_staff) sees all messages      | Messages list is displayed                            | Pass, No errors |
|                              |        |                |                                                                                 | <details><summary>contact-list2</summary><img src="./documentationfiles/testing/endpoint/contact/contact-list2.png"></details>       |                                             |                                                       |                 |
| /contact/create/             | POST   | Create         | Create a new contact message                                                    | <details><summary>contact-create1</summary><img src="./documentationfiles/testing/endpoint/contact/contact-create1.png"></details>   | New contact message is created and returned | New contact message created and returned successfully | Pass, No errors |
|                              |        |                |                                                                                 | <details><summary>contact-create2</summary><img src="./documentationfiles/testing/endpoint/contact/contact-create2.png"></details>   |                                             |                                                       |                 |
| contact/update/{edit_token}/ | GET    | Read           | Retrieve the just created contact message authenticated via a unique edit_token | <details><summary>contact-retrieve</summary><img src="./documentationfiles/testing/endpoint/contact/contact-retrieve.png"></details> | Contact Form details returned               | Contact Form details returned                         | Pass, No errors |
| contact/update/{edit_token}/ | PUT    | Update         | Update the just created contact message. authenticated via a unique edit_token  | <details><summary>contact-update1</summary><img src="./documentationfiles/testing/endpoint/contact/contact-update1.png"></details>   | Updates the existing contact message        | Contact message updated successfully                  | Pass, No errors |
|                              |        |                |                                                                                 | <details><summary>contact-update2</summary><img src="./documentationfiles/testing/endpoint/contact/contact-update2.png"></details>   |                                             |                                                       |                 |
| contact/update/{edit_token}/ | DELETE | Delete         | Delete the just created contact message. authenticated via a unique edit_token  | <details><summary>contact-delete1</summary><img src="./documentationfiles/testing/endpoint/contact/contact-delete1.png"></details>   | Deletes the specified contact message       | Contact message deleted successfully                  | Pass, No errors |
|                              |        |                |                                                                                 | <details><summary>contact-delete2</summary><img src="./documentationfiles/testing/endpoint/contact/contact-delete2.png"></details>   |                                             |                                                       |                 |


#### Likes
| Endpoint     | Method | CRUD Operation | Description                                  | Test Result Screenshot                                                                                                       | Expected Result                                       | Actual Result                                        | Result          |
| ------------ | ------ | -------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------- | --------------- |
| /likes/      | GET    | Read           | List all likes                               | <details><summary>like-read</summary><img src="./documentationfiles/testing/endpoint/likes/like-read.png"></details>         | Returns a list of all likes                           | Returned a list of all likes successfully            | Pass, No errors |
| /likes/      | POST   | Create         | Create a new like (authenticated users only) | <details><summary>like-create1</summary><img src="./documentationfiles/testing/endpoint/likes/like-create1.png"></details>   | New like is created and returned                      | New like created and returned successfully           | Pass, No errors |
|              |        |                |                                              | <details><summary>like-create2</summary><img src="./documentationfiles/testing/endpoint/likes/like-create2.png"></details>   |                                                       |                                                      |                 |
| /likes/{id}/ | GET    | Read           | Retrieve a specific like                     | <details><summary>like-retrieve</summary><img src="./documentationfiles/testing/endpoint/likes/like-retrieve.png"></details> | Returns a specific like                               | Returned correct a specified like                    | Pass, No errors |
| /likes/{id}/ | DELETE | Delete         | Delete a specific like (owner only)          | <details><summary>like-delete1</summary><img src="./documentationfiles/testing/endpoint/likes/like-delete1.png"></details>   | Deletes the specified like by the authenticated owner | Like deleted successfully by the authenticated owner | Pass, No errors |
|              |        |                |                                              | <details><summary>like-delete2</summary><img src="./documentationfiles/testing/endpoint/likes/like-delete2.png"></details>   |                                                       |                                                      |                 |

#### Parks
| Endpoint     | Method | CRUD Operation | Description                    | Test Result Screenshot                                                                                                         | Expected Result                | Actual Result                  | Result          |
| ------------ | ------ | -------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ | ------------------------------ | --------------- |
| /parks/      | GET    | Read           | Retrieve a list of parks       | <details><summary>park-list-read</summary><img src="./documentationfiles/testing/endpoint/parks/park-list-read.png"></details> | List of parks returned         | List of parks returned         | Pass, No errors |
| /parks/      | POST   | Create         | Create a new park              | <details><summary>park-create1</summary><img src="./documentationfiles/testing/endpoint/parks/park-create1.png"></details>     | Park created, details returned | Park created, details returned | Pass, No errors |
|              |        |                |                                | <details><summary>park-create2</summary><img src="./documentationfiles/testing/endpoint/parks/park-create2.png"></details>     |                                |                                |                 |
| /parks/{id}/ | GET    | Read           | Retrieve a specific park by ID | <details><summary>park-retrieve</summary><img src="./documentationfiles/testing/endpoint/parks/park-retrieve.png"></details>   | Park details returned          | Park details returned          | Pass, No errors |
| /parks/{id}/ | PUT    | Update         | Update a specific park by ID   | <details><summary>park-update1</summary><img src="./documentationfiles/testing/endpoint/parks/park-update1.png"></details>     | Updates the existing park page | Park page updated successfully | Pass, No errors |
|              |        |                |                                | <details><summary>park-update2</summary><img src="./documentationfiles/testing/endpoint/parks/park-update2.png"></details>     |                                |                                |                 |
| /parks/{id}/ | DELETE | Delete         | Delete a specific park by ID   | <details><summary>park-delete1</summary><img src="./documentationfiles/testing/endpoint/parks/park-delete1.png"></details>     | Park deleted                   | Park deleted                   | Pass, No errors |
|              |        |                |                                | <details><summary>park-delete2</summary><img src="./documentationfiles/testing/endpoint/parks/park-delete2.png"></details>     |                                |                                |                 |

#### Profiles
| Endpoint        | Method | CRUD Operation | Description                                   | Test Result Screenshot                                                                                                                    | Expected Result                                        | Actual Result                                                    | Result          |
| --------------- | ------ | -------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------- | --------------- |
| /profiles/      | GET    | Read           | List all profiles (logged in users)           | <details><summary>profiles-list-read</summary><img src="./documentationfiles/testing/endpoint/profiles/profiles-list-read.png"></details> | Returns a list of all user profiles                    | Partially updates the profile details for the authenticated user | Pass, No errors |
| /profiles/{id}/ | GET    | Read           | Retrieve a specific profile (logged in users) | <details><summary>profiles-retrieve</summary><img src="./documentationfiles/testing/endpoint/profiles/profiles-retrieve.png"></details>   | Returns details of a specific user profile             | Returned correct details for the specified profile               | Pass, No errors |
| /profiles/{id}/ | PUT    | Update         | Update a specific profile (owner only)        | <details><summary>profiles-update1</summary><img src="./documentationfiles/testing/endpoint/profiles/profiles-update1.png"></details>     | Updates the profile details for the authenticated user | Profile details updated successfully for the authenticated user  | Pass, No errors |
|                 |        |                |                                               | <details><summary>profiles-update2</summary><img src="./documentationfiles/testing/endpoint/profiles/profiles-update2.png"></details>     |                                                        |                                                                  |                 |


#### Ratings
| Endpoint       | Method | CRUD Operation | Description                                    | Test Result Screenshot                                                                                                                 | Expected Result                                         | Actual Result                                   | Result          |
| -------------- | ------ | -------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------- | --------------- |
| /ratings/      | GET    | Read           | List all ratings                               | <details><summary>ratings-list-read</summary><img src="./documentationfiles/testing/endpoint/ratings/ratings-list-read.png"></details> | Returns a list of all ratings                           | Returned a list of all ratings successfully     | Pass, No errors |
| /ratings/      | POST   | Create         | Create a new rating (authenticated users only) | <details><summary>ratings-create1</summary><img src="./documentationfiles/testing/endpoint/ratings/ratings-create1.png"></details>     | New rating is created and returned                      | New rating is created and returned successfully | Pass, No errors |
|                |        |                |                                                | <details><summary>ratings-create2</summary><img src="./documentationfiles/testing/endpoint/ratings/ratings-create2.png"></details>     |                                                         |                                                 |                 |
| ratings/{id}/  | GET    | Read           | Retrieve a specific rating                     | <details><summary>ratings-retrieve</summary><img src="./documentationfiles/testing/endpoint/ratings/ratings-retrieve.png"></details>   | Returns details of a specific rating                    | Returned the rating data successfully           | Pass, No errors |
| /ratings/{id}/ | PUT    | Update         | Update a specific rating (owner only)          | <details><summary>ratings-update1</summary><img src="./documentationfiles/testing/endpoint/ratings/ratings-update1.png"></details>     | Updates the rating by the authenticated owner           | Rating updated successfully                     | Pass, No errors |
|                |        |                |                                                | <details><summary>ratings-update2</summary><img src="./documentationfiles/testing/endpoint/ratings/ratings-update2.png"></details>     |                                                         |                                                 |                 |
| /ratings/{id}/ | DELETE | Delete         | Delete a specific rating (owner only)          | <details><summary>rating-delete1</summary><img src="./documentationfiles/testing/endpoint/ratings/ratings-delete1.png"></details>      | Deletes the specified rating by the authenticated owner | Rating deleted successfully                     | Pass, No errors |
|                |        |                |                                                | <details><summary>rating-delete2</summary><img src="./documentationfiles/testing/endpoint/ratings/ratings-delete2.png"></details>      |                                                         |                                                 |                 |

#### Search functionality
Searching for park - name, park - description, park - user has been tested and it is working as expected.

| Search filter  | Search word | Test Result Screenshot                                                                                   | Result          |
| -------------- | ----------- | -------------------------------------------------------------------------------------------------------- | --------------- |
| user__username | Stephan     | <details><summary>search1</summary><img src="./documentationfiles/testing/search/search1.png"></details> | Pass, No errors |
|                | Stephan     | <details><summary>search2</summary><img src="./documentationfiles/testing/search/search2.png"></details> |                 |
| name           | Fun         | <details><summary>search3</summary><img src="./documentationfiles/testing/search/search3.png"></details> | Pass, No errors |
|                | Fun         | <details><summary>search4</summary><img src="./documentationfiles/testing/search/search4.png"></details> |                 |
| description    | coaster     | <details><summary>search5</summary><img src="./documentationfiles/testing/search/search5.png"></details> | Pass, No errors |
|                |             | <details><summary>search6</summary><img src="./documentationfiles/testing/search/search6.png"></details> |      

### Resume
All tests were passed. Accordingly, the code is ready for use and publication.