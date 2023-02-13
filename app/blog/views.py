#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Project ：flaskBlog
# File ：views.py
# Author ：刘万
# Date ：2023/2/9 13:49
from flask import Blueprint,render_template

bp = Blueprint('blog', __name__, url_prefix='/blog', static_folder='static', template_folder='templates')


def index():
    posts=[1,2,3,4,5]
    return render_template('base.html',posts=posts)