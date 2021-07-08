### Install Env:
```bash
pip install -r requirements.txt
```

If you use mysql, need to install:
```bash
pip install mysqlclient
```
Or other db like pgsql.

Copy `.env.example` to `app_name` folder, and rename `.env`

Generate SECRET_KEY:
```bash
python manage.py shell
```

```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

Migrate DB:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Web Server:
```bash
daphne -b 0.0.0.0 -p 8000 {{cookiecutter.app_name}}.asgi:application
```

[daphne Github](https://github.com/django/daphne)


### Environment
[django environ](https://django-environ.readthedocs.io/en/latest/#)