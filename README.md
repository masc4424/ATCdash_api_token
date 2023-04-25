# ATCdash_api_token

Developed solely for support team work purposes, this project is part of Adamas Tech Consultancy

## About the Project
The project I have created is a responsive dashboard that aims to monitor various E-commerce segments. These segments include Payment and Registration, which are vital aspects of any E-commerce platform. By monitoring these segments, the dashboard can quickly identify any issues or glitches that might arise and ensure that customers can complete their transactions seamlessly.

In addition to Payment and Registration, the dashboard also monitors SMS-LMS Sync, which refers to the synchronization between the SMS (student management system) and LMS (learning management system). This synchronization is critical for E-commerce platforms that offer online courses or training programs. The dashboard ensures that the SMS and LMS working properly so that no mismatch happens which makes it easy for support team to access and complete their queries.

Lastly, the dashboard monitors the LMS, which helps support team to monitor whether the recordings are uploading correctly , Class completions & license occupancy, Teachers are uploading their notes correctly or not, and lastly the attandance.

In summary, the project I have created is a responsive dashboard that monitors various E-commerce segments, including Payment and Registration, SMS-LMS Sync, SMS to Ticketing system, Support System Monitoring, and LMS. It ensures that these segments are functioning correctly, thereby enhancing the overall Monitoring for the Support Team.

## Installation

### Requirements
#### 1. Python v3
#### 2. Django   
#### 3. MySQL(recommended), PostgreSQL, Oracle Database and SQLite  
#### 4. POSTMAN (recommended) OR Swagger - API Call

1. Download the Project as .zip file
2. Extract the file as "Extract to 'ATCdash_api_token\'"
3. Open the extracted folder into your IDE (Pycharm).
4. Add a new virtual environment to this project (venv). to create venv follow the below commands and copy and paste to your IDE terminal.
```bash
python -m venv venv
```
now to activate venv
```bash
cd venv/Scripts/activate.ps1
```

5. Install the requirements from requirements.txt.

OR,

Clone this Project from this link.

```bash
https://github.com/masc4424/ATCdash_api_token.git
```

### Inside project
Now when you open this project inside your preffered IDE (Pycharm) you need to make some changes to the files.

settings.py

``` bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'atcdash_api_token',
        'USER': 'root',
        'PASSWORD': 'asd',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

change the database 

Engine, Name, user, password, to your database type 

```bash
DATABASES = {
    'default': {
        'ENGINE': '<YOUR DB ENGINE>',
        'NAME': '<YOUR DB NAME>',
        'USER': '<YOUR USER NAME>',
        'PASSWORD': '<YOUR PASSWORD>',
        'HOST': '127.0.0.1', <You can also use 'localhost'>
        'PORT': '3306', <this is the localhost port>
    }
}
```

after this run these commands in your IDE terminal 

go to the project directory in this project write 

```bash
cd dashboard
```

```bash
python manage.py makemigrations
```
```bash
python manage.py maigrate
```

Now you can add a superuser(admin) using this command "python manage.py createsuperuser" you can add username password and email address to you database which can help you to access adminpanel also you can login inside the page.

```bash
python manage.py createsuperuser
```

Now you can run the server.

```bash
python manage.py runserver
```

now open your browser and go to http://127.0.0.1:8000/


# API
  Use this url for testing and Generating API: http://127.0.0.1:8000/api_users/
  GET and POST response API through Postman OR your choice of API platform.
