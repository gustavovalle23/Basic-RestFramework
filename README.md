# Basic Rest Framework

This is a basic django application, exploring different topics like rest api, cache, sessions, custom user, jwt, multitenancy and other things.


## API Documentation

#### Return all users

```http
  GET /users/
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `page`      | `integer`  | Default: 0                          |


### Use Cases
- [x] User Login (JWT)
- [x] User Register
- [ ] User Update
- [x] User Detail
- [ ] User Delete/Inactivate
- [x] User authorization
