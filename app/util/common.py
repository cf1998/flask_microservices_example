#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/12 9:19 下午
# @Author: John.bai
import json
from flask import Response

# 继承自dict，实现可以通过.来操作元素
class AttrDict(dict):
    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __getattr__(self, item):
        return self.__getitem__(item)

    def __delattr__(self, item):
        self.__delitem__(item)


def json_response(status='', data='', msg='', error=''):
    content = AttrDict(status=status, msg=msg, data=data, error=error)
    if error:
        content.data = ''
    return Response(json.dumps(content,ensure_ascii=False))


