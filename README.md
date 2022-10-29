Create the python environment and install the necessary dependencies

    $ pipenv shell 
    $ pipenv install
> this install all dependencies in a python container

##test the API
------
Please install postgresql on your computer 
------
$ sudo apt install postgresql

create your database for example:
> $ sudo su postgres 

> $ createdb yourdbname -O youruser

or create a DB with a pgadmin o your favorite dbrowser

update database_uri in app.config 
------
> app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://***youruser:yourpassword***@localhost/***yourdbname***'
------
then you have to init a python terminal to make the migrations and insert the next comamnds
=====
    >>> from api.auth.models import Users

    >>> from api.publications.models import Publication

    >>> from config.settings import db

    >>> db.create_all()
    
    >>> exit()
=====

-----
    now we can run the api in terminal write this lines
    $ export FLASK_APP=apps
    $ flask run
    * Running on http://127.0.0.1:5000/
----

## API reference

## User managment

```https
  POST /api/auth/register
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `fullname` | `string` | **Required*. Username |
| `email` | `string` | **Required*. Email |
| `password` | `string` | **Required*. Password |


```https
  POST /api/auth/login
  ```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required*. Email |
| `password` | `string` | **Required*. Password |


```https
  PUT /api/auth
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required*. Username |
| `email` | `string` | **Required*. Email-id |
| `password` | `string` | **Required*. Password |
| `image` | `string($binary)` | **Required*. Image |


## Publications

```http
  POST api/publications
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required* Title  |
| `description`      | `string` | **Required* Description |
| `priority`      | `number` | **Required* Priority  |
| `status`      | `string` | **Required* Current status |

```http
  PUT api/publications/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required* Title |
| `description`      | `string` | **Required* Description |
| `priority`      | `number` | **Required* Priority |
| `status`      | `string` | **Required* Current status |

```http
  GET /api/publications/{pub_id}
```

```http
  DELETE /api/publications/{pub_id}
```
