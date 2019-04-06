# /run.py
import os
from dotenv import load_dotenv, find_dotenv

from {{cookiecutter.app_name}}.app import create_app

load_dotenv(find_dotenv())

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == '__main__':
    env_port = os.getenv('PORT')
    env_host = os.getenv('FLASK_HOST')
    # run app
    app.run(host=env_host, port=env_port)
