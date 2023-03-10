#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Project ：flaskBlog
# File ：models.py
# Author ：刘万
# Date ：2023/2/9 13:49

from datetime import datetime
from RealProject import db
from enum import IntEnum
from sqlalchemy.dialects.mysql import LONGTEXT


class BaseModel(db.Model):
    '''
    基类模型
    '''
    __abstract__ = True
    add_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    pub_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)  # 更新时间


class Category(BaseModel):
    """
    分类模型
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    icon = db.Column(db.String(128), nullable=True)
    post = db.relationship('Post', backref='category', lazy=True)

    def __repr__(self):
        return '<Category %r>' % self.name


class PostPublishType(IntEnum):
    """ 文章发布类型
    """
    draft = 1  # 草稿
    show = 2  # 发布


# 多对多关系帮助器表
tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
                )


class Post(BaseModel):
    """文章模型
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.String(200), nullable=True)
    has_type = db.Column(db.Enum(PostPublishType), server_default='show', nullable=False)
    # 一对多关系
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    content = db.Column(LONGTEXT, nullable=False)
    # 多对多关系
    tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('post', lazy=True))

    def __repr__(self):
        return f'<Post {self.title}>'


class Tag(BaseModel):
    """ 文章标签
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)

    def __repr__(self):
        return f'<Tag {self.name}>'
