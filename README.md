Django User Management API
This Django-based API provides functionality for user registration, login, updates, deletion, and more. It allows you to manage users through RESTful endpoints.

After cloning the project, run the command below
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

After that you can check the endpoints below
API Endpoints
URL=http://127.0.0.1:8000/api
1. User Registration
URL: /register/
Method: POST
Description: This endpoint allows users to register by providing necessary information such as username, password, and other details.
2. Get All Users
URL: /users/
Method: GET
Description: Fetches a list of all users in the system.

3. Get User Details
URL: /users/<uuid:id>/
Method: GET
Description: Fetches the details of a specific user by their UUID.
Request Params:
id (UUID): The unique identifier of the user to fetch.

4. Update User
URL: /users/update/<uuid:id>/
Method: PUT
Description: Updates an existing user’s information. Fields can be partially updated.
Request Params:
id (UUID): The unique identifier of the user to update.

5. Partial Update User
URL: /users/partial-update/<uuid:id>/
Method: PATCH
Description: Allows partial updates to a user's details. You can update only the fields you need.
Request Params:
id (UUID): The unique identifier of the user to update.

6. Delete User
URL: /users/delete/<uuid:id>/
Method: DELETE
Description: Deletes a user from the system.
Request Params:
id (UUID): The unique identifier of the user to delete.

7. Login
URL: /login/
Method: POST
Description: Authenticates a user and returns an authentication token.

I have My Postman documentation link below 

https://documenter.getpostman.com/view/29757568/2sAYBYe9yh
