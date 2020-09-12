#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/12 8:17 下午
# @Author: John.bai

from flask_restplus import Namespace, fields


class UserDTO(object):
    api = Namespace('用户管理', description='用户操作相关')

    add_user_input = api.model('添加用户', {
        'username': fields.String(required=True, description='用户名'),
        'password': fields.String(required=True, description='密码')
    }
    )

