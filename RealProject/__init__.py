#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Project ：flaskBlog
# File ：__init__.py.py
# Author ：刘万
# Date ：2023/2/9 13:47

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from RealProject.settings import BASE_DIR

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    # create and configure the app
    ## instance_relative_config设置为True则代表开启从文件加载配置，默认为False
    app = Flask(__name__, instance_relative_config=True)
    # app.config其实调用的是flask类的config属性，该属性又被设置为了一个Config的类
    ## from_mapping则是该Config类下的一个方法，用来更新默认配置，返回值为True
    ## 至于Flask的默认配置项都有哪些，其实可以深入源码查看default_config属性所列出的项
    # 默认配置
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    if test_config is None:
        CONFIG_PATH = BASE_DIR / 'RealProject/settings.py'
        app.config.from_pyfile(CONFIG_PATH, silent=True)
    else:
        # 和最开始的配置意思一致
        app.config.from_mapping(test_config)

    # 注册链接数据库
    db.init_app(app)
    # 注册migrate
    migrate.init_app(app, db)

    # 递归创建目录，确保项目文件存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 注册视图
    from app.blog import views as blog
    app.register_blueprint(blog.bp)

    from app.auth import views as auth
    app.register_blueprint(auth.bp)

    from app.admin import views as admin
    app.register_blueprint(admin.bp)

    # url引入
    app.add_url_rule('/', endpoint='index', view_func=blog.index)

    # 注册数据库模型
    from app.blog import models
    from app.auth import models

    return app
