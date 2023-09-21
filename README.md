# Events App Team SpitFire

## Table Of Contents

- [Introduction](#introduction)
- [Base URI / Live Deployment](#base-uri--live-deployment)
- [Local Server Setup](#local-server-setup)
  - [Clone The Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
  - [Configure Environment Variables](#configure-environment-variables)
  - [Run the Server](#run-the-server)
  - [Run API Tests](#run-api-tests)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [Authentication Endpoint](#authentication-endpoint)
- [Sample Usage](#sample-usage)
- [Error Handling](#error-handling)
- [UML Class Diagram](#uml-class-diagram)
- [Limitations and Assumptions](#limitations-and-assumptions)
- [Authors](#authors)

## Introduction

Welcome to the Events App documentation for Team SpitFire! This document provides detailed information on setting up the server locally, API endpoints, authentication, sample usage, error handling, and more.

---

## Base URI / Live Deployment

The Events App is hosted for live testing at [insert_base_uri_here]. Replace `[insert_base_uri_here]` with the actual base URI where the API is deployed.

---

## Local Server Setup

### Clone The Repository

To get started with the local development environment, clone the repository:

```bash
$ git clone https://github.com/hngx-org/spitfire-events.git
$ cd spitfire-events/Backend
```

### Install Dependencies

You can set up the environment using either `venv` or `pipenv`. Here are instructions for both:

Using `venv`:

```bash
# create Virtual Environment
$ python3 -m venv venv

# Activate Virtual Env
$ source venv/bin/activate

# Install Dependencies
$ pip install -r requirements.txt
```

Using `pipenv`:

```bash
$ pip install pipenv

# create virtuel environment
$ pipenv --python 3.10

# Activate virtual env
$ pipenv shell

# install dependencies in requirements.txt or pipfile
$ pipenv install
```

### Configure Environment Variables

Make sure to set the following environment variables:

    SECRET_KEY: [Your Secret Key]
    SQLALCHEMY_DATABASE_URI: [Your Database URI]
    OAUTHLIB_INSECURE_TRANSPORT: 1
    ANDROID_CLIENT_ID: 
    IOS_CLIENT_ID: 

### Run the Server

```bash
$ python3 run.py
```

### Run API Tests

**Note:** ensure you are connected to the internet before running tests and are in `spitfire-events` directory

```bash
# install test suite and HTTP requests library
$ pip install requests pytest

# Run the tests in test_crud.py
$ pytest test_event.py -v
```

[click for test_event.py file](test_event.py)

<br>

---

## **Authentication**

The authentication mechanism used by this API is Google oAuth2 with session cookies
see [Authentication here](./API_DOCUMENTATION.md)

## **EndPoints**
see [Api Documentation here](./API_DOCUMENTATION.md)
### Authentication Endpoint

`POST 'API/auth'`

- Retrieves a person from the database using user id
- **Request Body**: 
    - **Input**: JSON with auth token.
    ```
    {
      "token": "google id token",
    }
    ```
- Returns: JSON response with a message and person object containing `id`, `name` and `date created`

Example Response

```json
  {
    "message": "success",
    "name": "user display name",
    "email": "user email",
    "avatar": "user image url"
  }
```

_status code: 200_
see [Api Documentation here](./API_DOCUMENTATION.md)
---

## Sample Usage

## **Error Handling**

> Errors are returned as JSON objects in the following format with their error code

```json
{
  "error": "error name",
  "message": "error description"
}
```

<br>

The API will return 5 error types, with diffreent descriptions when requests fail;

- 400: Request unprocessable
- 403: Forbidden
- 404: resource not found
- 422: Bad Request
- 429: Too Many Requests(rate limiting)
- 500: Internal server error

<br>

## **UML CLASS DIAGRAM**

---

## Limitations and Assumptions

## Authors

- [@Godhanded](https://github.com/Godhanded)
