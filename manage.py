import os
import unittest
# line 4 and 5 imports the migrate and manager modules respectively
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist

# line 13 calls the create_app function we created initially to create the application instance with the required parameter from the environment variable which can be either of the following - dev, prod, test. If none is set in the environment variable, the default dev is used

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

# line 19 and 21 instantiates the manager and migrate classes by passing the app instance to their respective constructors

manager = Manager(app)

migrate = Migrate(app, db)

# In line 25,we pass the db and MigrateCommandinstances to the add_command interface of the managerto expose all the database migration commands through Flask-Script

manager.add_command('db', MigrateCommand)
# line 29 and 34 marks the two functions as executable from the command line
@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()

    
# Each time the database model changes, repeat the migrate and upgrade commands
#
# 1. py manage.py db migrate
# 2. py manage.py db upgrade
