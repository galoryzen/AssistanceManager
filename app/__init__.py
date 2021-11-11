import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA


logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)


@app.cli.command("initdata")
def init_db():
    from . import test_data
    
@app.cli.command("createusers")
def init_users():
    from . import create_users


from . import models, views