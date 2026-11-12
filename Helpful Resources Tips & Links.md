# Helpful Resources, Tips & Links

A curated collection of useful Django documentation, learning material, and practical project tips. The Django documentation's **stable** version tracks the current supported release; check it when working with a specific version.

## Official Django resources

- [Django documentation](https://docs.djangoproject.com/en/stable/) — the main reference for Django.
- [Getting started tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) — build a small project step by step.
- [Topic guides](https://docs.djangoproject.com/en/stable/topics/) — models, the ORM, forms, authentication, testing, and more.
- [How-to guides](https://docs.djangoproject.com/en/stable/howto/) — practical instructions for common tasks.
- [Django reference](https://docs.djangoproject.com/en/stable/ref/) — detailed reference for Django APIs and settings.
- [Django FAQ](https://docs.djangoproject.com/en/stable/faq/) — answers to common questions.
- [Download Django](https://www.djangoproject.com/download/) — current releases and supported versions.
- [Django release notes](https://docs.djangoproject.com/en/stable/releases/) — changes and upgrade notes for each release.
- [Django security releases](https://www.djangoproject.com/security/) — security announcements and supported release information.
- [Deployment checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/) — production-readiness checks.
- [Security in Django](https://docs.djangoproject.com/en/stable/topics/security/) — Django's security features and recommendations.

## Learning Django

- [Django Girls Tutorial](https://tutorial.djangogirls.org/) — a beginner-friendly, hands-on introduction.
- [MDN: Django web framework](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) — a guided introduction to Django concepts and a sample application.
- [Django documentation: First steps](https://docs.djangoproject.com/en/stable/intro/) — project setup and the fundamentals.

## Useful documentation by task

- [Models and databases](https://docs.djangoproject.com/en/stable/topics/db/) — models, queries, transactions, and migrations.
- [Forms](https://docs.djangoproject.com/en/stable/topics/forms/) — handling and validating user input.
- [Authentication](https://docs.djangoproject.com/en/stable/topics/auth/) — users, permissions, and authentication.
- [Django admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/) — configure the built-in administration site.
- [Testing](https://docs.djangoproject.com/en/stable/topics/testing/) — write and run automated tests.
- [Static files](https://docs.djangoproject.com/en/stable/howto/static-files/) — manage CSS, JavaScript, and other static assets.
- [Settings reference](https://docs.djangoproject.com/en/stable/ref/settings/) — configure a Django project.
- [URL dispatcher](https://docs.djangoproject.com/en/6.0/topics/http/urls/) — map URL patterns to views.
- [Writing views](https://docs.djangoproject.com/en/6.0/topics/http/views/) — create views that handle web requests.
- [Request and response objects](https://docs.djangoproject.com/en/6.0/ref/request-response/) — use Django's `HttpRequest` and `HttpResponse` APIs.

## Popular Django ecosystem projects

These are separate projects; review their documentation and supported Django versions before adding them to an application.

- [Django REST framework](https://www.django-rest-framework.org/) — build Web APIs.
- [Django Channels](https://channels.readthedocs.io/en/stable/) — support asynchronous protocols such as WebSockets.
- [Celery with Django](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html) — run background and scheduled tasks.
- [WhiteNoise](https://whitenoise.readthedocs.io/en/stable/) — serve static files from a Django application.
- [django-allauth](https://docs.allauth.org/en/latest/) — account registration and authentication features.
- [Django Packages](https://djangopackages.org/) — discover reusable Django apps and tools.

## Python environment quick start

Run these commands from the directory containing `manage.py`. In Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install Django
python manage.py runserver
```

For other platforms, see Python's [`venv` guide](https://docs.python.org/3/library/venv.html) and the [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/).

## Practical project tips

1. **Keep the project and apps distinct.** A project contains site-wide settings and URL configuration; an app packages one area of functionality.
2. **Use a virtual environment.** Install dependencies in the project's environment, and record them in a dependency file so the project can be reproduced.
3. **Make and apply migrations deliberately.** After model changes, run `python manage.py makemigrations` and `python manage.py migrate`; review generated migrations before sharing them.
4. **Keep secrets out of source control.** Load secret keys and credentials from environment-specific configuration, and never publish them in code or screenshots.
5. **Prepare settings for production.** Turn `DEBUG` off, configure `ALLOWED_HOSTS`, use HTTPS, and follow Django's deployment checklist. Run `python manage.py check --deploy` against production settings.
6. **Protect user input and accounts.** Keep Django's CSRF protection enabled, validate input, and use Django's authentication and password tools rather than writing your own.
7. **Test important behavior.** Add tests for models, views, forms, and permissions; run them with `python manage.py test`.
8. **Separate static files from uploaded media.** Static assets belong to the application; user uploads need appropriate storage, access controls, and backups.
9. **Check query behavior as data grows.** Use Django's ORM tools such as `select_related()` and `prefetch_related()` where appropriate, and inspect queries before optimizing.
10. **Upgrade carefully.** Read release notes, update one supported version at a time when practical, and run tests after upgrading Django or third-party packages.

## Handy management commands

```text
python manage.py runserver       Start the local development server
python manage.py createsuperuser Create an admin account
python manage.py makemigrations  Create migrations for model changes
python manage.py migrate         Apply migrations to the database
python manage.py test            Run the project's tests
python manage.py check           Run Django's system checks
```

Use the documentation that matches the Django version installed in your environment when commands or APIs differ between releases.
