# Online docs

https://hackmd.io/@rt0sfDCMRAKPrjq1mxbhgw/H1snEB8-9

Basic setup for django

**Setup pip and virtual environment**

```bash
# install pip and venv
python3 -m pip install wheel
# upgrade pip
python3 -m pip install -U pip

# install pipenv
python3 -m pip install pipenv
# cd $projectroot/
cd /to/path/of/the-project/

# create virtual environment
pipenv install
# this might take a few minutes
```

---

**Start virtual environment and get dev-dependencies**

```bash

# activate virtual environment
pipenv shell

# sync libraries and dev dependencies
# this step has to be performed only when libraries are updated
pipenv sync --dev

```

## Startup django

when you activate the pipenv shell a few environment variables in `.env` file will be available in your
shell like the `DJANGO_SETTINGS_MODULE`

```bash
# run django dev server
python3 manage.py runserver
```

Open up

- [http://localhost:8000/admin/](http://localhost:8000/admin/)
  - Django admin
