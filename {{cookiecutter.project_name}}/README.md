### Install Env:
```bash
pip install -r requirements.txt
```

### Start Web Server:
```bash
daphne -b 0.0.0.0 -p 8000 {{cookiecutter.app_name}}.asgi:application
```

[daphne Github](https://github.com/django/daphne)


### Environment
[django environ](https://django-environ.readthedocs.io/en/latest/#)