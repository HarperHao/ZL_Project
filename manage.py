"""
Author   : HarperHao
TIME    ： 2020/12/7
FUNCTION:  数据库的迁移
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zlbbs import create_app
from exts import db
from apps.cms import models as cms_models

CMSuser = cms_models.CMSUser
app = create_app()
manager = Manager(app)
Migrate(app, db)

manager.add_command("db", MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSuser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    #print(user.password)
    print('管理员用户添加成功\n')



@manager.command
def recreate():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
