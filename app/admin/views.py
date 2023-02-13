#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Project ：flaskBlog
# File ：views.py
# Author ：刘万
# Date ：2023/2/10 17:06
from flask import Blueprint, render_template, request
from app.auth.views.auth import login_required
from app.blog.models import Category

bp = Blueprint('admin', __name__, url_prefix='/admin', static_folder='static', template_folder='templates')


@bp.route('/')
@login_required
def index():
    return render_template('admin/index.html')


@bp.route('/category')
@login_required
def category():
    page = request.args.get('page', 1, type=int)
    pagination = Category.query.order_by(-Category.add_date).paginate(page=page, per_page=10, error_out=False)
    category_list = pagination.items
    print(category_list)

    return render_template('admin/category.html', category_list=category_list, pagination=pagination)
