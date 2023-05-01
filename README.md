# Basic Rest Framework

This is a basic django application, exploring different topics like rest api, cache, sessions, custom user, jwt, multitenancy and other things.

### Use Cases
- [x] User Login (JWT)
- [x] User Register
- [ ] User Update
- [x] User Detail
- [ ] User Delete/Inactivate
- [x] User authorization


## API Documentation
This project demonstrates how to implement authentication using `rest_framework_simplejwt` in Django.

## Installation

1. Clone the repository:

```sh
git clone git@github.com:gustavovalle23/Basic-RestFramework.git
```

2. Install dependencies:

```sh
pip install -r requirements.txt
```

3. Run database migrations:

```sh
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:

```sh
python manage.py createsuperuser
```

5. Run the development server:

```sh
python manage.py runserver
```

6. Use the API by sending requests to the endpoints.

## Usage

This project provides an API to create and manage users. The API includes the following endpoints:

### List Users

Returns a list of all users.

- URL: `/users/`
- Method: `GET`
- Headers: `Authorization: Bearer <access_token>`

### Create User

Creates a new user.

- URL: `/users/`
- Method: `POST`
- Headers: `Content-Type: application/json`
- Data Params: `{ "username": "<username>", "email": "<email>", "password": "<password>", "birth_date": "<YYYY-MM-DD>" }`

### Retrieve User

Retrieves a specific user.

- URL: `/users/<id>/`
- Method: `GET`
- Headers: `Authorization: Bearer <access_token>`

### Update User

Updates a specific user.

- URL: `/users/<id>/`
- Method: `PUT`
- Headers: `Authorization: Bearer <access_token>`, `Content-Type: application/json`
- Data Params: `{ "username": "<username>", "email": "<email>", "password": "<password>", "birth_date": "<YYYY-MM-DD>" }`

### Delete User

Deletes a specific user.

- URL: `/users/<id>/`
- Method: `DELETE`
- Headers: `Authorization: Bearer <access_token>`

## Running Tests

This project includes tests for the authentication and user endpoints. To run the tests, use the following command:

```sh
python manage.py test
```

## Credits

This project was created with the help of the `rest_framework_simplejwt` library for Django.
