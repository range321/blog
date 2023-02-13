#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Project ：flaskBlog
# File ：settings.py
# Author ：刘万
# Date ：2023/2/9 13:48
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

SECRET_KEY = 'l%3ya7fn3moipdpcltj(tdfcv5^@lj=t5d&72levvls+y*@_4^'

SQLALCHEMY_DATABASE_URI = 'mysql://root:qazwsx@114.115.152.68:3300/flask_blog'

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
