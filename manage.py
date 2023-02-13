#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Project ：flaskBlog
# File ：manage.py
# Author ：刘万
# Date ：2023/2/9 13:47
from RealProject import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
