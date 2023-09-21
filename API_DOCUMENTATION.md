# API Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Error Handling](#error-handling)
3. [User Management](#user-management)
   - 3.1 [Authentication](#authentication)
    - 3.1.1 [Authenticate User](#authenticate-user)
    - 3.1.2 [Get Logged in User](#get-currently-logged-in-user)
    - 3.1.3 [logout user](#logout)
   - 3.2 [Get a Users Profile](#get-user-profile)
   - 3.3 [Update User Profile](#update-user-profile)
4. [Event Management](#event-management)
   - 4.1 [Create a New Event](#create-a-new-event)
   - 4.2 [Get a List of Events](#get-a-list-of-events)
   - 4.3 [Get Event Details](#get-event-details)
   - 4.4 [Update Event Details](#update-event-details)
   - 4.5 [Delete an Event](#delete-an-event)
   - 4.6 [Add a Comment to an Event](#add-a-comment-to-an-event)
   - 4.7 [Get Comments for an Event](#get-comments-for-an-event)
   - 4.8 [Add an Image to a Comment](#add-an-image-to-a-comment)
   - 4.9 [Get Images for a Comment](#get-images-for-a-comment)
5. [User Interactions](#user-interactions)
   - 5.1 [Express Interest in an Event](#express-interest-in-an-event)
   - 5.2 [Remove Interest in an Event](#remove-interest-in-an-event)
   - 5.3 [Create a New Group](#create-a-new-group)
   - 5.4 [Get Group Details](#get-group-details)
   - 5.5 [Update Group Details](#update-group-details)
   - 5.6 [Delete a Group](#delete-a-group)
   - 5.7 [Add a User to a Group](#add-a-user-to-a-group)
   - 5.8 [Remove a User from a Group](#remove-a-user-from-a-group)
6. [Models](#models)
   - 6.1 [Users Model](#users-model)
   - 6.2 [Images Model](#images-model)
   - 6.3 [UserGroups Model](#usergroups-model)
7. [Conclusion](#conclusion)


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

## User Management 

### Authentication
- Session based Authentication is used
- A Session Cookie is sent and stored on client after athenticating with google
- subsequent requests should come with the cookie in the request headers
### Authenticate User
- **Endpoint**: **POST** /api/auth
- **Description**: Authenticate a user and obtain access token.
- **Request Body**: 
    - **Input**: JSON with auth token.
    ```JSON
    {
      "token": "google id token",
    }
    ```
    - Attributes:
        - `token` (string, required): Google id token.
- **Success Response**:
    - **Status Code**: 200 (OK)
    - **Response**:
    ```JSON
    {
      "message": "success",
      "name": "user display name",
      "email": "user email",
      "avatar": "user image url"
    }
    ```
    - **Attributes**:
        - `avatar` (string): mage url to users avatar.

-**Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
        ```JSON
        {
          "error": "Bad Request",
          "message": "Invalid token."
        }
        ```
    - **500 Internal Server Error**:
        - **Status Code**: 500
        - **Response Body**:
        ```JSON
        {
          "error": "Internal Server Error",
          "message": "It's not you, it's us. We encountered an internal server error."
        }
        ```

### Get Currently Logged In User
- **Endpoint**: **GET** /api/auth/@me
- **Description**: Get user details of the currently logged in user
- **Success Response**:
    - **Status Code**: 200 (OK)
    - **Response**:
    ```JSON
    {
      "message": "success",
      "name": "user display name",
      "email": "user email",
      "avatar": "user image url
    }
    ```
    - **Attributes**:
        - `avatar` (string): mage url to users avatar.

-**Error Responses**:
    - **401 Unauthorised**:
        - **Status Code**: 400
        - **Response Body**:
        ```JSON
        {
          "error": "Unauthorised",
          "message": "You are not logged in"
        }
        ```

### Logout
- **Endpoint**: **GET/POST** /api/auth/logout
- **Description**: log out user session
- **Success Response**:
    - **Status Code**: 204 (OK)
    - **Response**:
    ```JSON
    {
      "message": "success",
    }
    ```

### Get User Profile
- **Endpoint**: **GET** `/api/users/{id}`
- **Description**: Get user profile by ID.
- **Success Response**:
    - **Status Code**: 200 (OK)
    - **Response**:
```JSON
{
  "status": "success",
  "message": "user {user_id} details fetched successfully",
  "data": {
    "id": "user-id",
    "name": "John Doe",
    "email": "johndoe@example.com",
    "avatar": "avatar-url"
  }
}
```
-**Error Responses**:
    - **404 Not Found**:
        - **Status Code**: 404
        - **Response Body**:
        ```JSON
        {
          "error": "User not found",
        }
        ```

### Update User Profile
- **Endpoint**: **PUT** `/api/users/{id}`
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

## Event Management 

### Create a New Event
- **Endpoint**: **POST** `/api/events`
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

### Get a List of Events
- **Endpoint**: **GET** `/api/events`
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

### Get Event Details
- **Endpoint**: **GET** `/api/events/(id)`
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

### Update Event Details
- **Endpoint**: **PUT** `/api/events/{id}`
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

### Delete an Event
- **Endpoint**: **DELETE** `/api/events/{id}`
- **Description**: Delete an event by ID.
- **Success Response**:
    - **Status Code**: 204 (No Content)

### Add a Comment to an Event
- **Endpoint**: **POST** `/api/events/{id}/comments`
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

### Get Comments for an Event
- **Endpoint**: **GET** `/api/events/{id}/comments``
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

### Add an Image to a Comment
- **Endpoint**: **POST** `/api/comments/{id}/images`
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

### Get Images for a Comment
- **Endpoint**: **GET** `/api/comments/{id}/images`
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

## User Interactions

### Express Interest in an Event
- **Endpoint**: **POST** `/api/users/{id}/interests/{event_id}`
- **Description**:  Express interest in an event.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "message": "Interest expressed successfully."
}
```

### Remove Interest in an Event
- **Endpoint**: **PDELETE** `/api/users/{id}/interests/{event_id}`
- **Description**:  Remove interest in an event.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "message": "Interest removed successfully."
}
```

## Group Management 

### Create a New Group
- **Endpoint**: **POST** `/api/groups`
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
### Get Group Details
- **Endpoint**: **PUT** `/api/groups/{id}`
- **Description**: Update group details by ID.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "id": "group-id",
  "name": "Group Name",
  "description": "Group Description"
}
```

### Update Group Details
- **Endpoint**: **PUT** `/api/groups/{id}`
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

### Delete a Group
- **Endpoint**: **DELETE** `/api/groups/{id}`
- **Description**: Delete a group by ID.
- **Success Response**:
    - **Status Code**: 204 (No Content)

### Add a User to a Group
- **Endpoint**: **POST** `/api/groups/:groupId/members/{id}`
- **Description**:  Add a user to a group.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```
{
  "message": "User added to the group successfully."
}
```

### Remove a User from a Group
- **Endpoint**: **DELETE** `/api/groups/{id}/members/{user_id}`
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


