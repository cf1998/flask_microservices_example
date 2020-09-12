#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/12 8:13 下午
# @Author: John.bai
from app import db
from app.model.model import Users
from app.util.common import json_response


# 新增用户
def add_user(data):
    username = data.get('username', None)
    password = data.get('password', None)

    if username is not None and password is not None:

        db_data = {
            'username': username,
            'password': password
        }

        db_data = Users(**db_data)
        db.session.add(db_data)
        db.session.commit()
        data = json_response(status='0', msg='添加成功')
        return data

    else:
        return False, 400

