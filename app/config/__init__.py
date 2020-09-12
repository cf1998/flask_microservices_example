#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/12 8:01 下午
# @Author: John.bai

from app.config.dev_config import DevConfig


def read_config(config_name):
    """
    如果多环境可以通过类似这样的方式控制
    :param config_name:
    :return:
    """

    if config_name == 'dev':
        return DevConfig