#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/12 8:01 下午
# @Author: John.bai
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import read_config


# 创建 app
app = Flask(__name__)

# 创建 db
db = SQLAlchemy()


def create_app(env):

    # 读取环境变量
    app.config.from_object(read_config(env))

    # 注册 db
    db.init_app(app)

    return app
