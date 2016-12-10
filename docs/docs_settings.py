"""
This is the local_settings file for Yacms's docs.
"""

from Yacms.project_template.project_name.settings import *  # noqa

DEBUG = False
ROOT_URLCONF = "Yacms.project_template.project_name.urls"

# Generate a SECRET_KEY for this build
from random import choice
characters = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = ''.join([choice(characters) for i in range(50)])

if "Yacms.accounts" not in INSTALLED_APPS:
    INSTALLED_APPS = tuple(INSTALLED_APPS) + ("Yacms.accounts",)
