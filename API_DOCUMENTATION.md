# Postman API Documentation
Welcome to the API documentation for our user and event management system. This documentation provides a detailed guide on how to use the API endpoints using Postman. You can test and interact with the API using the provided examples.

## Authentication
Before using the API, you'll need to authenticate to obtain access tokens.

### Authenticate User
- Endpoint: POST `/api/auth``
- Description: Authenticate a user and obtain access tokens.
- Request Body:
    ```
    json
    {
        "email": "user@example.com",
        "password": "password123"
    }
    
    ```