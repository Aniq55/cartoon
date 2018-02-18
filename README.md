# cartoon

Follow it sequentially.

## Get project
Needs to be changed after successfully merging to upstream.
```sh
git clone https://github.com/Compro-Prasad/cartoon
git checkout origin/cleanup
```

## Install `pipenv`
Install `pipenv` system-wide. It is much easier than `pip` + `venv`/`virtualenv`:
```sh
sudo pip install pipenv
```

## Setting up database
```sh
cp .env.example .env
```
Add mysql details in the `.env` file.

## Getting the dependencies
Be sure that you are inside the project root directory:
```sh
pipenv --three   # One time setup
pipenv shell     # Activates virtualenv
pipenv install   # Installs dependencies
```

## Setup the tables
```sh
./manage.py makemigrations
./manage.py migrate
```

## Run the server
```sh
./manage.py runserver
```

## Report an issue
(Issues)[https://github.com/nolanding/cartoon/issues]
