#!/usr/bin/env python

from flask_script import Manager
from flask_migrate import MigrateCommand
import subprocess

from app import create_app 

manager = Manager(create_app)
manager.add_command("db", MigrateCommand)

@manager.command
def test():
	"runs unit tests `tests/run.sh`"
	subprocess.run(["tests/run.sh"])


if __name__ == '__main__':
	manager.run()
