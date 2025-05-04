============
django-polls
============

django-polls is a Django app to conduct web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "django_polls",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("polls/", include("django_polls.urls")),

3. Run ``python manage.py migrate`` to create the models.

4. Start the development server and visit the admin to create a poll.

5. Visit the ``/polls/`` URL to participate in the poll.

Steps for Installing Django Polls App from Local Package
---------------------------------------------------------

Install the polls app package from the local tar.gz file:
Run the following command in your project directory to install the package via pip::

    pip install django-polls/dist/django_polls-0.1.tar.gz

Add the polls app to INSTALLED_APPS:
In your project's settings.py file, add the polls app configuration to the INSTALLED_APPS list::

    INSTALLED_APPS = [
        ...
        'django_polls.apps.PollsConfig',
        ...
    ]

Include the polls app URLs in the project URL configuration:
In your project's urls.py file (e.g., storefront/urls.py), include the polls app URLs::

    from django.urls import path, include

    urlpatterns = [
        ...
        path('polls/', include('django_polls.urls')),
        ...
    ]

Run database migrations:
Apply migrations to create the necessary database tables for the polls app::

    python manage.py migrate django_polls

Run the development server:
Start the Django development server to test the polls app::

    python manage.py runserver

Access the polls app in your browser:
Open your web browser and navigate to::

    http://127.0.0.1:8000/polls/

You should see the polls app homepage or index page.
