from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role,Blog
from  flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')
# app = create_app('tests')

migrate = Migrate(app,db)


manager = Manager(app)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role = Role,Blog=Blog)
if __name__ == '__main__':
    manager.run()
