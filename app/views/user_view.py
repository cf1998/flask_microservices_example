#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/12 8:16 下午
# @Author: John.bai

from flask import request
from flask_restplus import Resource

from app.dto.user_dto import UserDTO
from app.service.user_service import add_user


api = UserDTO.api
add_user_input = UserDTO.add_user_input


# 用户相关操作
@api.route('')
@api.response(200, 'SUCCESS')
@api.response(400, 'BAD REQUEST')
@api.response(401, 'NOT AUTHORIZED')
@api.response(404, 'NOT FOUND')
class Users(Resource):

    @api.expect(add_user_input, validate=True)
    def post(self):
        """ 新增用户 """
        data = add_user(request.json)
        return data

    def delete(self):
        pass
