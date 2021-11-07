from .models import Asignatura, Clase, Curso, Departamento, Docente, Estudiante, EstudianteMatriculaCurso, Periodo, PlanAsignatura, PlanEstudio, ProgramaAcademico, Salon
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db

# TODO: Probar related views
# related_views = [EmployeeView]

class DepartamentoView(ModelView):
    datamodel = SQLAInterface(Departamento)
    add_columns=['id','nombre']
    
class ProgramaAcademicoView(ModelView):
    datamodel = SQLAInterface(ProgramaAcademico)
    add_columns=['id','nombre','departamento']
    
class AsignaturaView(ModelView):
    datamodel = SQLAInterface(Asignatura)
    add_columns=['id','nombre','departamento']
    
class PlanEstudioView(ModelView):
    datamodel = SQLAInterface(PlanEstudio)
    add_columns=['id','nombre','programa']

class PlanAsignaturaView(ModelView):
    datamodel = SQLAInterface(PlanAsignatura)
    
class PeriodoView(ModelView):
    datamodel = SQLAInterface(Periodo)
    add_columns=['id','nombre']
    
class SalonView(ModelView):
    datamodel = SQLAInterface(Salon)
    
class DocenteView(ModelView):
    datamodel = SQLAInterface(Docente)
    add_columns=['id','nombre', 'direccion', 'cedula', 'departamento']

class CursoView(ModelView):
    datamodel = SQLAInterface(Curso)
    add_columns=['id','nombre', 'docente', 'asignatura']
    
class ClaseView(ModelView):
    datamodel = SQLAInterface(Clase)
    
class EstudianteMatriculaView(ModelView):
    datamodel = SQLAInterface(EstudianteMatriculaCurso)

class EstudianteView(ModelView):
    datamodel = SQLAInterface(Estudiante)
    add_columns=['id','nombre', 'direccion', 'cedula', 'telefono', 'plan', 'periodo']


appbuilder.add_view(
    DepartamentoView, "Departamentos", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    ProgramaAcademicoView, "Programas Academicos", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    AsignaturaView, "Asignaturas", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    PlanEstudioView, "Planes de Estudio", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    PlanAsignaturaView, "Plan de Estudio - Asignatura", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    PeriodoView, "Periodos", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    SalonView, "Salones", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    DocenteView, "Docentes", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    CursoView, "Cursos", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    ClaseView, "Clases", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    EstudianteMatriculaView, "Estudiante-Matricula", icon="fa-folder-open-o", category="Universidad"
)

appbuilder.add_view(
    EstudianteView, "Estudiantes", icon="fa-folder-open-o", category="Universidad"
)