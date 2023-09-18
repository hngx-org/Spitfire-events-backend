# Events App Team SpitFire

## Table Of Contents
- [Set up server for Local Machine](#set-up-the-server-local)
- [DataBase Info](#database-info)
- [Base Uri/Live Deployment](#base-uri)
- [Run API Tests](#run-api-tests)
- [UML Class Diagram](#uml-class-diagram)
- [Error Handling](#error-handling)
- [EndPoints](#endpoints)
  - [Authentication](#authentication)

- [Sample Usage](#sample-usage)
- [Limitations or Assumptions](#assumptionslimitations)
- [Authors](#authors)

## **Event SERVER API-ENDPOINT DOCUMENTATION**
---
<br>
<br>

### **Base Uri**
----
----
Hosted for live testing on **https://**
....
<br>

### **Set up the server (local)**
### Clone The Repository
```bash
$ git clone https://github.com/hngx-org/spitfire-events.git

$ cd spipfire-events
```

### Install Dependencies
```bash
# create Virtual Environment
$ python3 -m venv venv

# Activate Virtual Env
$ source venv/bin/activate

# Install Dependencies
$ pip install -r requirements.txt
```

#### if you use pipenv

```bash
$ pip install pipenv

# create virtuel environment
$ pipenv --python 3.10

# Activate virtual env
$ pipenv shell

# install dependencies in requirements.txt or pipfile
$ pipenv install
```


### Run the Server
```bash
$ python3 run.py 
```

### Run API TESTs
***Note:** ensure you are connected to the internet before running tests and are in spitfire-events directory*
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
>Errors are returned as JSON objects in the following format with their error code

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
        "id":1,
        "name":"name of user",
        "date_created":"Mon, 11 Sep 2023 01:04:27 GMT"
    }
 }
```
*status code: 200*

---

<br>

### **UML CLASS DIAGRAM**
---

## Authors
- [@Godhanded](https://github.com/Godhanded)