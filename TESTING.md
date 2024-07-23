![Logo](/documentationfiles/logo2.webp)
# Thrill Seeker API Testing

The testing.md file provides an overview of all tests that have been carried out specifically with the Thrill Seeker API.

## Content
1. [Code Validation](#code-validation)
2. [Manual testing](#manual-testing)
3. [Summary](#summary)


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
These steps were carried out to test the API manually:
1. Testing all urls Endpoints for proper functioning.
2. Checking the correct functioning of the apps. If what is expected happens during use and all functions work without problems. (CRUD functionality)
3. Testing the search function


#### URL Testing
| **Tested** | **Expected result** | **Result** | **Pass** |
--- | --- | --- | :---:


#### Functionality Testing - CRUD
| **Tested** | **Create** | **View** | **Update** | **Delete** |
--- | --- | --- | :---:| :---:


#### Search functionality
- Searching for park - name, park - description, park - user is working as expected.
