# My Weather Site Project

This project was done as an assessment for Byte Orbit's interview. Due to time constraints, there are some work still needs to be added and addressed, which are listed in the [TODOs](#todos) and [Known Issues](#known-issues) section.

## Application

User will be presented a landing page where they can login or register for this application. There are only 3 required fields to register an user:

* email
* password
* password_repeat

After the user submits the registration form, a login page will be presented to him/her. After an user is successfully logged in, a 7-day weather forcasts will be presented to the user in paginated fashion, where each page will contain 3-day forecasts. Styles are still missing for the represented weather data, which will be address in the future work as enhancements.

## Dependencies

* Python 3.6
* Django 1.9
* Django REST framework 3.3
* sqlite3

A full list of dependencies is described in the *requirements.pip* located in the root of the file directory.

## Forecast Data

The app needs data, the data is pulled into an sqlite3 database by an admin. This is done with the management command:

```bash
(venv) $ python manage.py getforecasts
```

This command pull data from [http://weather.news24.com](http://weather.news24.com). The full URL is set in the app's *settings.py*. Each forecast is for a particular day and if a forecast for the same is fetched, the forecast for that day will just be updated with the new data.

## Installation

This version of the application is only meant for trial purpose as it is not really complete. A virtual environment needs to be create before this application can be deployed in a local system.

The compressed file needs to be unzipped somewhere in your system, then follow these commands to install and start the application:

```bash
$ cd EnZhou_App
$ virtualenv -p python3.6 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.pip
(venv) $ pip install -e ./
(venv) $ sh run.sh
```

While the application is running, you can open this link with your browser: [http://127.0.0.1:8080](). This address and port are predefined the in the *run.sh* file. You can change the port number if you see something like:

```bash
Error: That port is already in use.
```

## API Structure

The API gives access to the cities and forecasts to admin user ONLY. It's made with Django REST framework and uses the basic HTTP auth provided by the framework. An admin is a person who know how to use Django's management commands and has a django superuser created using the following command.

```bash
(venv) $ python manage.py createsuperuser
```

List of APIs:

* [http://127.0.0.1:8080/api/v1/cities]()

> This gives you a list of cities available in the database

* [http://127.0.0.1:8080/api/v1/cities/1]()

> This gives you the city whose *id* is **1** in the database

* [http://127.0.0.1:8080/api/v1/forecasts]()

> This gives you the list of forecasts in the database

* [http://127.0.0.1:8080/api/v1/forecasts/1]()

> This gives you the forecast whose **id** is 1 in the database.

## Logging

The default log will be store in *mysite/log/app.log*. It can be tailed as following while the application is running:

```bash
(venv) $ tail -f mysite/log/app.log
```

## TODOs

Due to the time constraints and skills needed, the following items will be add in the futhur:

* Deploying script
* Functional tests
* ~~Styling using CSS~~
* logging need to be covered more areas

## Known Issues

* I've tried to deploy this app on my USB drive, had permission error while installing the virtual environment.

```bash
(venv) $  PermissionError: [Errno 1] Operation not permitted: 'python3.6'
```

* Logout link issue

> > Sometimes, the logout link shows in the home page with a user's email address, but no forecast data displaying. User had loggout and login to get rid of. I think this has to do with the user's session wasn't flushed properly.
