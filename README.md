# Education site

This is small Django-based project for Python course. The site is designed for user to learn capitals of different countries of the world. It has pages for learning capitals of countries and user testing. It gives some statistics and configuration as well.

## Video presentation

Following [the link](https://disk.yandex.ru/i/WDJFTTRkF2M5fQ), you can get short video presentation of the project.

## On running

In order to view the site you need to do following:

1. Git-clone this project if you did not do it yet:

    ```bash
    git clone https://github.com/sliv2001/education_site
    cd ./education_site
    ```

1. (Optionally) Create and enter the virtual environment:
    1. Run this to create new virtual environment:

        ```bash
        python -m venv myenv
        ```

    1. Run this to enter new virtual environment:

        ```bash
        ./myenv/Scripts/activate
        ```

1. Install needed requirenents from requirenents.txt:

    ```bash
    pip install -r .\requirements.txt
    ```

1. Run this to start the site from github repo:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

1. Now you can go to [site](127.0.0.1:8000) to check out the result.

## On lint checks

You can run the following line in order to get lint result in file lint.log:

```bash
pylint ./manage.py ./education_site ./geo_site ./users_auth > lint.log
```

## On project development

Some details on project frontend/backend structure as well as rationale for some design and development decisions may be found in [docs](./doc/README.md).
