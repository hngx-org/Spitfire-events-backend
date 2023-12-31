# API Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Error Handling](#error-handling)
3. [User Management](#user-management)
   - 3.1 [Authentication](#authentication)
     - 3.1.1 [Authenticate User](#authenticate-user)
     - 3.1.2 [Get Logged in User](#get-currently-logged-in-user)
     - 3.1.3 [Logout User](#logout)
   - 3.2 [Get a User's Profile](#get-user-profile)
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
   - 4.10 [Likes](#likes)  
     - 4.10.1 [Like a Comment](#like-a-comment)
     - 4.10.2 [Get Total Likes for a Comment](#get-total-likes-for-a-comment)
5. [User Interactions](#user-interactions)
   - 5.1 [Express Interest in an Event](#express-interest-in-an-event)
   - 5.2 [Remove Interest in an Event](#remove-interest-in-an-event)
   - 5.3 [Create a New Group](#create-a-new-group)
   - 5.4 [Get Group Details](#get-group-details)
   - 5.5 [Update Group Details](#update-group-details)
   - 5.6 [Delete a Group](#delete-a-group)
   - 5.7 [Add a User to a Group](#add-a-user-to-a-group)
   - 5.8 [Remove a User from a Group](#remove-a-user-from-a-group)
   - 5.9 [Get All Groups](#get-all-groups)
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

```JSON
{
  "error": "Bad Request",
  "message": "Invalid input data."
}
```

### 405 Method Not Allowed
- **Status Code**: 405
- **Response**:

```JSON
{
  "error": "Method Not Allowed",
  "message": "The HTTP method used is not allowed for this endpoint."
}

```

### 422 Unprocessable Entity
- **Status Code**: 422
- **Response**:

```JSON
{
  "error": "Unprocessable Entity",
  "message": "The server cannot process the request due to invalid data."
}
```

### 429 Too Many Requests
- **Status Code**: 429
- **Response**:

```JSON
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Please try again later."
}

```

### 500 Internal Server Error
- **Status Code**: 500
- **Response**:

```JSON
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
- session cookies expire after 30 days
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

- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
        ```JSON
        {
          "error": "Bad Request",
          "message": "Invalid token."
        }
        ```
    - **403 Forbidden**:
        - **Status Code**: 403
        - **Response Body**:
  ```JSON
  {
    "error": "Forbidden",
    "message": "Token is of unknown origin"
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
      "data:{
         "id": "user_id",
         "name": "user display name",
         "email": "user email",
         "avatar": "user image url"
       }
    }
    ```
    - **Attributes**:
        - `avatar` (string): mage url to users avatar.

- **Error Responses**:
    - **500 Internal Server Error**:
        - **Status Code**: 500
        - **Response Body**:
        ```JSON
        {
          "error": "Internal server error",
          "message": "It's not you it's us
        }
        ```

### Logout
- **Endpoint**: **GET/POST** `/api/auth/logout`
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
- **Endpoint**: **GET** `/api/users`
- **Description**: Get logged in user profile.
- **Success Response**:
    - **Status Code**: 200 (OK)
    - **Response**:
```JSON
{
     "data": {
       "id": "user-id",
       "name": "John Doe",
       "email": "johndoe@example.com",
       "avatar": "avatar-url",
       "created_at": "time_created in UTCNow",
       "updated_at": "time_updated in UTCNow"
     },
   
     "message": "user details fetched successfully"
}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
        ```JSON
        {
          "message": "your request could not be completed",
          "error": "Bad Request"
        }
        ```
    - **401 Unauthorized**:
        - **Status Code**: 401
        - **Response Body**:
        ```JSON
        {
          "error": "Unauthorized",
          "message": "You are not authorized to access this user's profile."
        }
        ```
    - **404 Not Found**:
        - **Status Code**: 404
        - **Response Body**:
        ```JSON
        {
          "error": "Not Found",
          "messgae": "User not found",
        }
        ```

### Update User Profile
- **Endpoint**: **PUT** `/api/users`
- **Description**: Update logged in user  profile.
- **Input**: JSON with user profile data (name, email, avatar).
```JSON
{
  "name": "Updated Name",
  "email": "updated@example.com",
  "avatar": "updated-avatar-url",
}

```
- **Success Response**:
    - **Status Code**: 201
    - **Response**:
```JSON
{
  "message": "user {user_id}  details updated successfully",
  "data": {  
  "id": "user-id",
  "name": "Updated Name",
  "email": "updated@example.com",
  "avatar": "updated-avatar-url",
  "created_at": "time_created in UTCNow",
  "updated_at": "time_updated in UTCNow"
  }
}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
  {
    "message": "your request could not be completed",
    "error": "Bad Request"
  }
  ```
    - **401 Unauthorized**:
        - **Status Code**: 401
        - **Response Body**:
  ```JSON
  {
    "error": "Unauthorized",
    "message": "You are not authorized to access this user's profile."
  }
  ```
    - **404 Not Found**:
        - **Status Code**: 404
        - **Response Body**:
  ```JSON
  {
    "error": "Not Found",
    "message": "User not found"
  }
  ```

## Event Management 

### Create a New Event
- **Endpoint**: **POST** `/api/events`
- **Description**: Create a new event.
- **Input**: JSON with event details (title, description, location, start date/time, end date/time, thumbnail).
```JSON
{
  "creator_id":"user_id",
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
```JSON
{ 
  "message": "Event Created",
  "data": {
    "id": "event-id",
    "title": "New Event",
    "description": "Event Description",
    "location": "Event Location",
    "start_date": "2023-09-21",
    "start_time": "10:00:00",
    "end_date": "2023-09-22",
    "end_time": "12:00:00",
    "created_at": "2023-09-22 19:24:04",
    "updated_at": "2023-09-22 19:24:04"
  }
}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
        {
          "error": "Bad Request",
          "message":  "An error occurred creating the event."
        }
  ```

### Get a List of Events
- **Endpoint**: **GET** `/api/events`
- **Description**: Get a list of events.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```JSON
{
   "message": "events returned succesfully", 
   [
     {
       "id": "event-id-1",
       "creator_id":"user_id",
       "title": "Event 1",
       "description": "Description 1",
       "location": "Location 1",
       "start_date": "2023-09-21",
       "start_time": "10:00:00",
       "end_date": "2023-09-22",
       "end_time": "12:00:00",
       "created_at": "2023-09-22 19:24:04",
       "updated_at": "2023-09-22 19:24:04"
     },
   
     {
       "id": "event-id-2",
       "creator_id":"user_id",
       "title": "Event 2",
       "description": "Description 2",
       "location": "Location 2",
       "start_date": "2023-09-23",
       "start_time": "14:00:00",
       "end_date": "2023-09-24",
       "end_time": "16:00:00",
       "created_at": "2023-09-22 19:24:04",
       "updated_at": "2023-09-22 19:24:04"
     }
   ]
}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
        {
          "error": "Bad Request",
          "message":  "something went wrong."
        }
  ```


### Get Event Details
- **Endpoint**: **GET** `/api/events/(id)`
- **Description**: Get event details by ID.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```JSON
{
  "message": "Event successfully Found",
  "data": {
    "id": "event-id",
    "title": "Event Title",
    "description": "Event Description",
    "creator_id": "creator-id",
    "location": "Event Location",
    "start_date": "2023-09-21",
    "start_time": "10:00:00",
    "end_date": "2023-09-22",
    "end_time": "12:00:00",
    "created_at": "2023-09-22 19:24:04",
    "updated_at": "2023-09-22 19:24:04"
  },

}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
        {
          "error": "Bad Request",
          "message":  "something went wrong."
        }
  ```
    - **404 Not Found**:
        - **Status Code**: 404
        - **Response Body**:
  ```JSON
        {
          "error": "Not Found",
          "Not Found": "Event not found"
        }
  ```

### Update Event Details
- **Endpoint**: **PUT** `/api/events/{id}`
- **Description**: Update event details by ID.
- **Input**: JSON with event details to update (title, description, location, start date/time, end date/time, thumbnail).
```JSON
{
  "creator_id":"user_id",
  "title": "New Event",
  "description": "Event Description",
  "location": "Event Location",
  "start_date": "2023-09-21",
  "start_time": "10:00:00",
  "end_date": "2023-09-22",
  "end_time": "12:00:00",
  "thumbnail": "thumbnail-url",

}
```
- **Success Response**:
    - **Status Code**: 201
    - **Response**:
```JSON
{
  "message": "item updated",
  "data": {
    "id": "event-id",
    "title": "Updated Event Title",
    "description": "Updated Event Description",
    "location": "Updated Location",
    "start_date": "2023-09-23",
    "start_time": "14:00:00",
    "end_date": "2023-09-24",
    "end_time": "16:00:00",
    "thumbnail": "updated-thumbnail-url",
    "created_at": "2023-09-22 19:24:04",
    "updated_at": "2023-09-22 19:24:04"
  }
}


```
- **Error Responses**:
    - **404 Not Found**:
        - **Status Code**: 404
        - **Response Body**:
  ```JSON
        {
          "error": "Not Found",
          "Not Found": "Event not found"
        }
  ```

### Delete an Event
- **Endpoint**: **DELETE** `/api/events/{id}`
- **Description**: Delete an event by ID.
- **Success Response**:
    - **Status Code**: 204 (No Content)
    - **Response**:
  ```JSON
    {
       "Message": "Event deleted",
       "data": []
    }
  ```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
        {
          "error": "Bad Request",
          "message":  "something went wrong."
        }
  ```

   - **403 Unauthorized**:
        - **Status Code**: 403
        - **Response Body**:
  ```JSON
        {
          "error": "Not Authorized",
          "Not Found": "Only the creator can delete group"
        }
  ```
    - **404 Not Found**:
        - **Status Code**: 404
        - **Response Body**:
  ```JSON
        {
          "error": "Not Found",
          "Not Found": "Event not found"
        }
  ```

  

### Add a Comment to an Event
- **Endpoint**: **POST** `/api/events/{id}/comments`
- **Description**:Add a comment to an event.
- **Input**:JSON with comment details (body).
```JSON
{
  "body": "This is a comment"
}

```
- **Success Response**:
    - **Status Code**: 201 (Created)
    - **Response**:
```JSON
{
  "message": "Comment saved successfully",
  "data": {
    "id": "comment-id",
    "body": "Comment body"
  }
}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
  {
     "message": "Failed to save to database",
     "error": "Bad Request"
   }

  ```
  **OR**
  ```JSON
  {
     "message": "Comment could not be saved",
     "error": "Bad Request"
   }

  ```

### Get Comments for an Event
- **Endpoint**: **GET** `/api/events/{event_id}/comments``
- **Description**: Get comments for an event.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```JSON
{
  "message": "Comments successfully fetched",
  "data": [
    {
      "id": "comment-id-1",
      "event_id": "event-id",
      "user_id":"user_id",
      "body": "Comment body 1",
      "created_at": "2023-09-22 19:24:04",
      "updated_at": "2023-09-22 19:24:04"
    },
    {
      "id": "comment-id-2",
      "event_id": "event-id",
      "user_id":"user_id",
      "body": "Comment body 2",
      "created_at": "2023-09-22 19:24:04",
      "updated_at": "2023-09-22 19:24:04"
    }
    // Additional comments...
  ]
}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
        {
          "error": "Bad Request",
          "message":   "An error occured while fetching all comments"
        }
  ```
    - **404 Not Found**:
        - **Status Code**: 404
        - **Response Body**:
  ```JSON
        {
          "status": "failed", 
          "message": "Comments not found"
        }
  ```


### Add an Image to a Comment
- **Endpoint**: **POST** `/api/comments/{id}/images`
- **Description**:Add an image to a comment.
- **Input**:JSON with image details (image_url).
```JSON
{
  "image_url": "image-url"
}

```
- **Success Response**:
    - **Status Code**: 201 (Created)
    - **Response**:
```JSON
{
   "message": "Image saved successfully",
  "image_id": "image-id",
  "comment_id": "comment-id",
  "image_url": "image-url"
}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
  {
      
     "message":  "Error: image data could not be saved",
     "error":  "Bad Request"
  }
  ```

### Get Images for a Comment
- **Endpoint**: **GET** `/api/comments/{id}/images`
- **Description**: Get images for a comment.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```JSON
{
   "message": "all images successfully fetched",
   "data":
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
}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
  {
     "message": "An error occurred while fetching all images",
     "error":  "Bad Request"
  }
  ```
## Likes

### Like A Comment
- **Endpoint** : `/like_comment/{comment_id}`
- **Description**: Like Or Unlike a particular comment.
- **Input Parameters**:`comment_id` (string, required): The ID of the comment to be liked.
- **Success Response**:
  - **Status Code**: 200
    - **Response**:
    - **FOR LIKE**
  ```JSON
    {
        "message": "Liked", 
        "data": "number_of_likes"
    }

  ```
   - **FOR UNLIKE**
  ```JSON
    {
        "message": "UnLiked", 
        "data": "number_of_likes"
    }

  ```
 - **Error Responses**:
    - **403 Forbidden**:
    - **Status Code**: 403
    - **Response Body**:
  ```JSON
  {
      "error": "Forbidden",
      "message": "you are not allowed to perform such actions"
  }
  ```
 - **404 Not Found**:
 - **Status Code**: 404
 - **Response Body**:
```JSON
{
  "error": "Not Found",
  "message": "Event Not Found",
}
```

### Get Total Likes for a Comment
- **Endpoint** : `/likes/{comment_id}`
- **Description**: Get the total number of likes for a particular comment.
- **Input Parameters**:`comment_id` (string, required): The ID of the comment for which to retrieve the total likes.
- **Success Response**:
  - **Status Code**: 200
    - **Response**:
  ```JSON
    {
        "message": "Number of likes", 
        "data": "number_of_likes"
    }

  ```
 - **Error Responses**:
    - **403 Forbidden**:
    - **Status Code**: 403
    - **Response Body**:
  ```JSON
  {
      "error": "Forbidden",
      "message": "you are not allowed to perform such actions"
  }
  ```
 - **404 Not Found**:
 - **Status Code**: 404
 - **Response Body**:
```JSON
{
  "error": "Not Found",
  "message": "Event Not Found",
}
```



## User Interactions

### Express Interest in an Event
- **Endpoint**: **POST** `/api/users/{id}/interests/{event_id}`
- **Description**:  Express interest in an event.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```JSON
{
     "message": "Interest registered.",
     "data": f"{user_id} has shown interest in {event_id}"
}
```
**OR**
```JSON
{
     "message": "Interest cannot be registered twice.",
     "data": f"{user_id} has shown interest in {event_id}"
}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
  {
     "message": "Something went wrong",
     "error":  "Bad Request"
  }
  ```
    - **404 Bad Request**:
        - **Status Code**: 404
        - **Response Body**:
  ```JSON
  {
    "Error": "Not Found",
    "message": "User or Event not found"
  }
  ```

### Remove Interest in an Event
- **Endpoint**: **DELETE** `/api/users/{id}/interests/{event_id}`
- **Description**:  Remove interest in an event.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```JSON
{
     "message": "Interest deleted",
     "data": "No content"
}
```
**OR**
```JSON
{
     "message": "user has not previously shown interest
     "data": "Nothing to delete"
}
```
**OR**
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
  {
     "message": "Something went wrong",
     "error":  "Bad Request"
  }
  ```
    - **404 Bad Request**:
        - **Status Code**: 404
        - **Response Body**:
  ```JSON
  {
       "Error": "Not Found",
       "message": "User or Event not found"
  }
  ```

## Group Management 

### Create a New Group
- **Endpoint**: **POST** `/api/groups`
- **Description**: Create a new group.
- **Input**: JSON with group title.
```JSON
{
  "title": "Group Title",
}

```
- **Success Response**:
    - **Status Code**: 201 (Created)
    - **Response**:
```JSON
{
  "message": "Group created successfully"
  "data": {
    "created_at": "2023-09-22 09:58:43",
    "id": "group-id",
    "title": "group-title",
    "updated": "2023-09-22 09:58:43"
  },
 
}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
  {
  "error": "Bad Request",
  "message": "group creation failed"
  }

  ```

### Get Group Details
- **Endpoint**: **GET** `/api/groups/{id}`
- **Description**: Get group details by ID.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```JSON
{
  "status": "success",
  "message": "Group details successfully fetched",
  "data": {
    "group_id": "group-id",
    "title": "Group Title"
  }
}
```
- **Error Responses**:
    - **404 Bad Request**:
        - **Status Code**: 404
        - **Response Body**:
  ```JSON
  {
    "error": "Not Found"
    "message": "Group not found"
  }
  ```
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
  {
    "error": "Bad Request",
    "message": "An error occurred while fetching group details"
  }
  ```


### Update Group Details
- **Endpoint**: **PUT** `/api/groups/{id}`
- **Description**: Update group details by ID.
- **Input**: JSON with group details to update (title).
```JSON
{
  "title": "Updated Title",
}

```
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```JSON
{
  "message": "Group updated successfully"
  "group": {
    "created_at": "2023-09-22 10:14:10",
    "id": "group-id",
    "title": "Updated Title",
    "updated": "2023-09-22 10:16:12"
    }
}
```
- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
  {
    "error": "Bad Request",
    "message": "Something is wrong with the request data"
  }
  ```
  - **Attributes**:
  `error` (string): Indicates that the 'title' attribute is missing in the request body.
  - **404 Not Found**:
    - **Status Code**: 404
    - **Response Body**:
  ```JSON
  {
    "error": "Group with ID {group_id} not found"
  }
  ```


### Delete a Group
- **Endpoint**: **DELETE** `/api/groups/{id}`
- **Description**: Delete a group by ID.
- **Success Response**:
    - **Status Code**: 204 (No Content)
   ```JSON
   {
      "message": "User removed from group successfully",
      "data": "group_id"
   }
   ```

- **Error Responses**:
    - **400 Bad Request**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
     {
     "error": "Bad Request",
     "message": "Your request could not be completed."
  }
  ```
  - **404 Not Found**:
        - **Status Code**: 404
        - **Response Body**:
  ```JSON
  {
       "message": "Group or user not found",
       "error":"Not Found"
  }

  ```

### Add a User to a Group
- **Endpoint**: **POST** `/api/groups/{group_id}/members/{member_id}`
- **Description**:  Add a user to a group.
- **Input Parameters** :
    - `group_id` (string, required): The ID of the group to which the user will be added.
    - `user_id` (string, required): The ID of the user to be added to the group.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```JSON
  {
     "data": "group_id",
     "message": "User added to Group"
  }
```
- **Error Responses**:
    - **404 Not Found**:
        - **Status Code**: 400
        - **Response Body**:
  ```JSON
  {
    "error": "Bad Request",
    "message":"Something went wrong with the request"
  }

  ```
  - **403 Forbidden**:
        - **Status Code**: 403
        - **Response Body**:
  ```JSON
  {
      "error":"Forbidden",
      "message":"User already in group"
  }
   ```

### Remove a User from a Group
- **Endpoint**: **DELETE** `/api/groups/{id}/members/{member_id}`
- **Description**:  Remove a user from a group.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```JSON
{
  "message": "User removed from group successfully",
  "data":group_id
}
```
- **Error Responses**:
    - **400 Bad Request**:
      - **Status Code**: 400
      - **Response Body**:
  ```JSON
  {
    "error": "Group ID {group_id} or User ID {group_id} not found"
  }
  ```
  - **403 Forbidden**:
        - **Status Code**: 403
        - **Response Body**:
  ```JSON
  {
      "error": "forbidden",
      "message": "User is not a member of this group"
  }
  ```

  - **404 Not Found**:
        - **Status Code**: 404
        - **Response Body**:
  ```JSON
  {
     "message": "Group or user not found",
     "error":"Not Found"
  }

### Get All Groups
- **Endpoint**: **GET** `/api/groups/`
- **Description**:  A list of group details.
- **Success Response**:
    - **Status Code**: 200
    - **Response**:
```JSON
{
  "message": "All groups successfully fetched",
  "data": group_list,
}
```
- **Error Responses**:
    - **400 Bad Request**:
      - **Status Code**: 400
      - **Response Body**:
  ```JSON
  {
      "error": "Bad Request",
       "message": "An error occurred while fetching all groups"
  }
  ```
  - **404 Not Found**:
        - **Status Code**: 404
        - **Response Body**:
  ```JSON
  {
     "message": "Group  not found",
     "error":"Not Found"
  }

  
## Models
### Users Model
- Represents user data with attributes:
    - `id` (string): Unique user ID.
    - `name` (string): User's name.
    - `email` (string): User's email address.
    - `avatar` (string): URL to the user's avatar image.

### Comments Model
- Represents comments data with attributes:
  - `comment_id` (string): Unique comment ID.
  - `event_id` (string): ID of the associated event.
  - `user_id` (string): ID of the user who made the comment.
  - `body` (string): Text content of the comment.
  - `images` (list of dictionaries): List of image data associated with the comment.

### Images Model
- Represents image data with attributes:
    - `id` (string): Unique image ID.
    - `comment_id` (string): ID of the comment to which the image belongs.
    - `image_url` (string): URL to the image

### UserGroups Model
- - Represents user-group relationships with attributes:
    - `user_id` (string): ID of the user.
    - `group_id` (string): ID of the group.

### InterestedEvents Model
- Represents user interest in events with attributes:
  - `user_id` (string): ID of the user who is interested in an event.
  - `event_id` (string): ID of the event that the user is interested in.

## Likes Model
- Represents user likes for comments with attributes:
  - comment_id (string): ID of the comment that is liked by a user.
  - user_id (string): ID of the user who liked the comment.


## Conclusion
This API documentation provides a comprehensive guide for integrating with the user and event management system. It covers authentication, user profiles, event creation and management, comments, images, user interactions, and group management. Developers can use this documentation to interact with the API and products that leverages these features.


