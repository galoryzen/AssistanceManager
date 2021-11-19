from flask.helpers import url_for
from flask_appbuilder import IndexView,expose
from flask import g,url_for,redirect


class MyIndexView(IndexView):
     @expose('/')
     def index(self):
        user = g.user
        if user.is_anonymous:
           return redirect(url_for("AuthDBView.login"))
        else:
           return redirect(url_for('ClassesView.listaClases'))
