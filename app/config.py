import os
from os import environ


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')