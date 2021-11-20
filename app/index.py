from flask.globals import current_app
from flask.helpers import url_for
from flask_appbuilder import IndexView,expose
from flask import g,url_for,redirect


class MyIndexView(IndexView):
      @expose('/')
      def index(self):
        
         roles = {
            "Admin": current_app.appbuilder.sm.find_role(
               current_app.appbuilder.sm.auth_role_admin
            ),
            "Estudiante": current_app.appbuilder.sm.find_role("Estudiante"),
            "Profesor": current_app.appbuilder.sm.find_role("Profesor"),
         }
         
         
         
         user = g.user
         if user.is_anonymous:
            return self.render_template('my_index.html')
         else:
            if g.user.roles[0] == roles['Admin']:
               return self.render_template('my_index.html')
            else:
               return redirect(url_for('ClassesView.listaClases'))
