""" Management commands for Worker0 """
import os
import urllib.parse

from flask import url_for
from flask_script import Manager

from worker0_server import create_app, db


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

@manager.command
def list_routes():
    """ List all available application routes. """
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint,
                                                              methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == "__main__":
    manager.run()
