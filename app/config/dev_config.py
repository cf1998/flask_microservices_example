#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/12 8:09 下午
# @Author: John.bai

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from app.config.base_config import Config


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@127.0.0.1:3306/demo?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
