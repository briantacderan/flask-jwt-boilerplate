.PHONY: env clean python-packages install tests run all

env: 
    pipenv shell

clean: 
    pipenv clean

python-packages: 
    pipenv install

install: clean python-packages

tests: 
    py manage.py test

run: 
    py manage.py run

all: clean install tests run
