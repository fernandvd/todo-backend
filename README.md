# TODO APP

## Description
    
It is a backend make in django for TODO APP. This backend use django-rest-framework. This use Django 5.1.3 and Postgres database

## Run application
    Before install you should install python and postgresql 

- Create a virtualenv
    ```bash
    # linux
    virtualenv venv

    # windows
    py -m venv venv
    ```

- Active virtual env and install dependencies
    ```bash
    # linux
    source venv/bin/activate

    # windows
    venv/Scripts/activate.bat
    venv/Scripts/Activate.ps1
    ```

- Install dependencies
    ```bash
    # install dependencies
    pip install -r requirements.txt
    ```

- Create .env file then copy .env.example to .env file and update theirs values.

- Run the following command for execute migrations
    ```bash
    python manage.py migrate
    ```

- Run the following command for start app
    ```bash
    python manage.py runserver
    ```

- For read documentation of APIS open `http://localhost:8000/swagger/`

