#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/12 8:10 下午
# @Author: John.bai

from app import db


# 用户表
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=True, default=None)
    password = db.Column(db.String(128),  nullable=True, default=None)