#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/12 8:04 下午
# @Author: John.bai
import pymysql
app_config = {
    'title': 'flask MicroService Demo',
    'version': '1.0',
    'description': 'flask MicroService Demo 的RESTful API服务'

}


class Config(object):
    SECRET_KEY = '5e8bca1c9aaa34aed6d069be3dfccd31'
    # 连接mysql数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = False   # 关闭警告信息
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG_LOG = True
