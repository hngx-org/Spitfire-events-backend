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

# Configure Environment Variables

Make sure to set the following environment variables:

    SECRET_KEY: [Your Secret Key]
    SQLALCHEMY_DATABASE_URI: [Your Database URI]

### Run the Server

```bash
$ python3 run.py
```

### Run API TESTs

**\*Note:** ensure you are connected to the internet before running tests and are in spitfire-events directory\*

```bash
# install test suite and http requests library
$ pip install requests pytest

# Run the tests in test_crud.py
$ pytest test_event.py -v
```

[click for test_event.py file](test_event.py)

<br>

#### **Error Handling**

---

---

> Errors are returned as JSON objects in the following format with their error code

```json
{
  "error": "error name",
  "message": "error description"
}
```

The API will return 5 error types, with diffreent descriptions when requests fail;

- 400: Request unprocessable
- 403: Forbidden
- 404: resource not found
- 422: Bad Request
- 429: Too Many Requests(rate limiting)
- 500: Internal server error

<br>

<br>

### **EndPoints**

---

---

<br>

#### **Authentication**

`GET '/auth/${id}'`

- Gets a person from the database using user id
- Path Parameter: `id`- integer id of person to retrieve
- Returns: JSON, message and person object containing name id and date created

```json
{
  "message": "Success",
  "person": {
    "id": 1,
    "name": "name of user",
    "date_created": "Mon, 11 Sep 2023 01:04:27 GMT"
  }
}
```

_status code: 200_

---

<br>

### **UML CLASS DIAGRAM**

---

## Authors

- [@Godhanded](https://github.com/Godhanded)
