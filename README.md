Create the python environment and install the necessary dependencies

    $ pipenv shell 
    $ pipenv install
> this install all dependencies in a python container

#test the API
------
Please install postgresql on your computer 
------
$ sudo apt install postgresql

create your database for example:
> $ sudo su postgres 

> $ createdb yourdbname -O youruser

or create a DB with a pgadmin o your favorite dbrowser

In the configuration file for 'SQLALCHEMY_DATABASE_URI'(api-servicepad/config/settings.py).
update for your user, password and name from you databae
------
> app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://***youruser:yourpassword***@localhost/***yourdbname***'
------
then you have to init a python terminal to make the migrations and insert the next comamnds
    $ python
    >>> from api.auth.models import Users
    >>> from api.publications.models import Publication
    >>> from config.settings import db
    >>> db.create_all()
    >>> exit()

-----
    now we can run the api in terminal write this lines
    $ export FLASK_APP=apps
    $ flask run
    * Running on http://127.0.0.1:5000/
----

