# Steps for Setup
1.	Make the root directory for the project
2.	git init in the directory
3.	make a .gitignore (can get it from the tutorial or another project you set up before like flaskr)
4.	Make setup.py
5.	Change name of setup.py in the file so that it matches your project name NO HYPHENS
6.	You can also change the version to 0.0.0 probably
7.	You’ll need to set `packages=find_packages()` so that you can install dependencies.
8.	You can now make extras_require dictionary if you want, and make a list for dev dependencies within the dictionary. These are usually `pytest` and `coverage`. The key name is your choice, but the dependencies in the list are the names of the dependencies. Pip will take care of installing these.
9.	Create the virtual environment `python3 -m venv venv`
10.	Activate the virtual environment. (You can check to see if you successfully activated this by checking the python version)
11.	Now that you’re in the venv, install the required dependencies in setup.py using pip or pip3: `pip install -e .`
12.	Now, install dev dependencies using `pip install -e ‘.[list, of, dependencies]’`(You’re usually gonna want to install the test dependency)
13.	Set up flask’s environment variables `export FLASK_APP=name` and `export FLASK_ENV=development`
14.	Make the project folder
15.	Create __init__.py, import flask into it, and create a function called create_app() which initializes flask in the directory and creates an index for our site. The flask directory is within venv/lib/python3.7/site-packages, as well as all the other dependencies. This is the code for __init__.py:
```
from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello World!'

    return app
```
