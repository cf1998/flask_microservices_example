#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/12 8:03 下午
# @Author: John.bai
from flask import Blueprint
from flask_restplus import Api
from app.config.base_config import app_config
from app.views.user_view import api as user

# 创建蓝图
blueprint = Blueprint('api', __name__)
# 创建REST API
api = Api(blueprint, **app_config)

api.add_namespace(user, path='/user')
