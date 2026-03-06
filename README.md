# Blog project


## Pre Commit

pre-commit is used to maintain code quality.

for first time setup:

```bash
pip install -r requirements/local.txt
pre-commit install
pre-commit run --all-files
```

## First Time install locally

```bash
virtualenv -p python3  env
source env/bin/activate
pip install -r requirements/local.txt
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver
git init
pre-commit install
pre-commit run --all-files
git commit -m "first commit"
```
