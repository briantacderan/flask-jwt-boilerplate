import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist

# Call the create_app function we created initially to create the application instance with the required parameter from the environment variable which can be either of the following - dev, prod, test. If none is set in the environment variable, the default dev is used

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

# Register Blueprint with the Flask application instance

app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

# Pass the db and MigrateCommand instances to the add_command interface of the managerto expose all the database migration commands through Flask-Script

manager.add_command('db', MigrateCommand)


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

# 1. py manage.py db migrate --message 'add {your input} table'
# 2. py manage.py db upgrade
