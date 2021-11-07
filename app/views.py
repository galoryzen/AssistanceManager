from .models import Estudiante
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db

class EstudianteView(ModelView):
    datamodel = SQLAInterface(Estudiante)
    # TODO: Prueba estos related views
    # related_views = [EmployeeView]

class EstudianteView(ModelView):
    datamodel = SQLAInterface(Estudiante)
    # TODO: Prueba estos related views
    # related_views = [EmployeeView]

appbuilder.add_view(
    EstudianteView, "Estudiantes", icon="fa-folder-open-o", category="Universidad"
)