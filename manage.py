#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2020/9/12 8:03 下午
# @Author: John.bai
import os
from app import create_app,db
from app.route import blueprint
from flask_cors import CORS
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 获取环境变量
env = os.getenv('RUNTIME_ENV') or 'dev'
# 创建 app
app = create_app(env)
# 加载蓝图
app.register_blueprint(blueprint)

# 创建 manager
manager = Manager(app)
# 创建 migrate
migrate = Migrate(app, db)
# 新增 db 到 manager中
manager.add_command('db', MigrateCommand)

# 跨域请求
CORS(app, supports_credentials=True)


@manager.command
def run():
    """ runs user permission and auth service """
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)


@manager.command
def create():
    """ runs create db all data """
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    manager.run()
