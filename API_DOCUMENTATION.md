# API Documentation

## Introduction
Welcome to the API documentation for our user and event management system. This API documentation provides detailed information about the endpoints and models for a user and event management system. It includes information on how to use each endpoint, expected input data, success responses, and HTTP status codes.

## Error Handling
The API handles errors gracefully and returns JSON responses with appropriate status codes and error messages. Here are some common error responses:

### 400 Bad Request
- **Status Code**: 400
- **Response**:

```
{
  "error": "Bad Request",
  "message": "Invalid input data."
}
```

### 405 Method Not Allowed
- **Status Code**: 405
- **Response**:

```
{
  "error": "Method Not Allowed",
  "message": "The HTTP method used is not allowed for this endpoint."
}

```

### 422 Unprocessable Entity
- **Status Code**: 422
- **Response**:

```
{
  "error": "Unprocessable Entity",
  "message": "The server cannot process the request due to invalid data."
}
```

### 429 Too Many Requests
- **Status Code**: 429
- **Response**:

```
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Please try again later."
}

```

### 500 Internal Server Error
- **Status Code**: 500
- **Response**:

```
{
  "error": "Internal Server Error",
  "message": "It's not you, it's us. We encountered an internal server error."
}

```

## User Management Endpoints

### POST /api/auth
- **Description**: Authenticate a user and obtain access token.
- **Request Body**: 
    - **Input**: JSON with user credentials.
    ```
    {
      "email": "user@example.com",
      "password": "password123"
    }
    ```
    - Attributes:
        - `email` (string, required): User's email address.
        - `password` (string, required): User's password.
- **Success Response**:
    - **Status Code**: 200 (OK)
    - **Response**:
    ```
    {
      "access_token": "your-access-token",
      "refresh_token": "your-refresh-token"
    }
    ```
    - **Attributes**:
        - `access_token` (string): Token for authenticating future requests.
        - `refresh_token` (string): Token for refreshing access tokens.
-**Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
        ```
        {
          "error": "Bad Request",
          "message": "Invalid input data."
        }
        ```
    - **500 Internal Server Error**:
        - **Status Code**: 500
        - **Response Body**:
        ```
       {
          "error": "Internal Server Error",
          "message": "It's not you, it's us. We encountered an internal server error."
        }
        ```

### GET /api/users/:userId
- **Description**: Get user profile by ID.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "id": "user-id",
  "name": "John Doe",
  "email": "johndoe@example.com",
  "avatar": "avatar-url"
}
```

### PUT /api/users/:userId
- **Description**: Update user profile by ID.
- **Input**: JSON with user profile data (name, email, avatar).
```
{
  "name": "Updated Name",
  "email": "updated@example.com",
  "avatar": "updated-avatar-url"
}

```
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "id": "user-id",
  "name": "Updated Name",
  "email": "updated@example.com",
  "avatar": "updated-avatar-url"
}
```

## Event Management Endpoints

### POST /api/events
- **Description**: Create a new event.
- **Input**: JSON with event details (title, description, location, start date/time, end date/time, thumbnail).
```
{
  "title": "New Event",
  "description": "Event Description",
  "location": "Event Location",
  "start_date": "2023-09-21",
  "start_time": "10:00:00",
  "end_date": "2023-09-22",
  "end_time": "12:00:00",
  "thumbnail": "thumbnail-url"
}
```
- **Success Response**:
    - **Status Code**: 201 (Created)
    - **Response**:
```
{
  "id": "event-id",
  "title": "New Event",
  "description": "Event Description",
  "location": "Event Location",
  "start_date": "2023-09-21",
  "start_time": "10:00:00",
  "end_date": "2023-09-22",
  "end_time": "12:00:00",
  "thumbnail": "thumbnail-url"
}
```

### GET /api/events
- **Description**: Get a list of events.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
[
  {
    "id": "event-id-1",
    "title": "Event 1",
    "description": "Description 1",
    "location": "Location 1",
    "start_date": "2023-09-21",
    "start_time": "10:00:00",
    "end_date": "2023-09-22",
    "end_time": "12:00:00",
    "thumbnail": "thumbnail-url-1"
  },
  {
    "id": "event-id-2",
    "title": "Event 2",
    "description": "Description 2",
    "location": "Location 2",
    "start_date": "2023-09-23",
    "start_time": "14:00:00",
    "end_date": "2023-09-24",
    "end_time": "16:00:00",
    "thumbnail": "thumbnail-url-2"
  }
]

```

### GET /api/events/:eventId
- **Description**: Get event details by ID.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "id": "event-id",
  "title": "Event Title",
  "description": "Event Description",
  "creator_id": "creator-id",
  "location": "Event Location",
  "start_date": "2023-09-21",
  "start_time": "10:00:00",
  "end_date": "2023-09-22",
  "end_time": "12:00:00",
  "thumbnail": "thumbnail-url"
}
```

### PUT /api/events/:eventId
- **Description**: Update event details by ID.
- **Input**: JSON with event details to update (title, description, location, start date/time, end date/time, thumbnail).
```
{
  "title": "Updated Event Title",
  "description": "Updated Event Description",
  "location": "Updated Location",
  "start_date": "2023-09-23",
  "start_time": "14:00:00",
  "end_date": "2023-09-24",
  "end_time": "16:00:00",
  "thumbnail": "updated-thumbnail-url"
}
```
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "id": "event-id",
  "title": "Updated Event Title",
  "description": "Updated Event Description",
  "creator_id": "creator-id",
  "location": "Updated Location",
  "start_date": "2023-09-23",
  "start_time": "14:00:00",
  "end_date": "2023-09-24",
  "end_time": "16:00:00",
  "thumbnail": "updated-thumbnail-url"
}
```

### DELETE /api/events/:eventId
- **Description**: Delete an event by ID.
- **Success Response**:
    - **Status Code**: 204 (No Content)

### POST /api/events/:eventId/comments
- **Description**:Add a comment to an event.
- **Input**:JSON with comment details (body).
```
{
  "body": "This is a comment"
}

```
- **Success Response**:
    - **Status Code**: 201 (Created)
    - **Response**:
```
{
  "comment_id": "comment-id",
  "event_id": "event-id",
  "user_id": "user-id",
  "body": "This is a comment",
  "images": []
}
```

### GET /api/events/:eventId/comments
- **Description**: Get comments for an event.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
[
  {
    "comment_id": "comment-id-1",
    "event_id": "event-id",
    "user_id": "user-id-1",
    "body": "Comment 1",
    "images": []
  },
  {
    "comment_id": "comment-id-2",
    "event_id": "event-id",
    "user_id": "user-id-2",
    "body": "Comment 2",
    "images": []
  }
]

```

### POST /api/comments/:commentId/images
- **Description**:Add an image to a comment.
- **Input**:JSON with image details (image_url).
```
{
  "image_url": "image-url"
}

```
- **Success Response**:
    - **Status Code**: 201 (Created)
    - **Response**:
```
{
  "image_id": "image-id",
  "comment_id": "comment-id",
  "image_url": "image-url"
}
```

### GET /api/events/:eventId/comments
- **Description**: Get images for a comment.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
[
  {
    "image_id": "image-id-1",
    "comment_id": "comment-id",
    "image_url": "image-url-1"
  },
  {
    "image_id": "image-id-2",
    "comment_id": "comment-id",
    "image_url": "image-url-2"
  }
]
```

## User Interactions Endpoints

### POST /api/users/:userId/interests/:eventId
- **Description**:  Express interest in an event.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "message": "Interest expressed successfully."
}
```

### DELETE /api/users/:userId/interests/:eventId
- **Description**:  Remove interest in an event.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "message": "Interest removed successfully."
}
```

## Group Management Endpoints

### POST /api/groups
- **Description**: Create a new group.
- **Input**: JSON with group details (name, description).
```
{
  "name": "Group Name",
  "description": "Group Description"
}

```
- **Success Response**:
    - **Status Code**: 201 (Created)
    - **Response**:
```
{
  "id": "group-id",
  "name": "Group Name",
  "description": "Group Description"
}
```

### PUT /api/groups/:groupId
- **Description**: Update group details by ID.
- **Input**: JSON with group details to update (name, description).
```
{
  "name": "Updated Group Name",
  "description": "Updated Group Description"
}

```
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "id": "group-id",
  "name": "Updated Group Name",
  "description": "Updated Group Description"
}
```

###  DELETE /api/groups/:groupId
- **Description**: Delete a group by ID.
- **Success Response**:
    - **Status Code**: 204 (No Content)

### POST /api/groups/:groupId/members/:userId
- **Description**:  Add a user to a group.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "message": "User added to the group successfully."
}
```

### DELETE /api/groups/:groupId/members/:userId
- **Description**:  Remove a user from a group.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "message": "User removed from the group successfully."
}
```

## Models
### Users Model
- Represents user data with attributes:
    - `id` (string): Unique user ID.
    - `name` (string): User's name.
    - `email` (string): User's email address.
    - `avatar` (string): URL to the user's avatar image.
  
### Images Model
- Represents image data with attributes:
    - `id` (string): Unique image ID.
    - `comment_id` (string): ID of the comment to which the image belongs.
    - `image_url` (string): URL to the image

### UserGroups Model
- Represents user-group relationships with attributes:
    - `user_id` (string): ID of the user.
    - `group_id` (string): ID of the group.


## Conclusion
This API documentation provides a comprehensive guide for integrating with the user and event management system. It covers authentication, user profiles, event creation and management, comments, images, user interactions, and group management. Developers can use this documentation to interact with the API and products that leverages these features.


