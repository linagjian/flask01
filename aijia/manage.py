#coding=utf-8

from iHome.app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


# 调用creat_app方法，创建应用实例， 指定开发者模式
app = create_app('development')

#实现了数据库表的创建
Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    