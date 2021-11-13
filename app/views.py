from flask.helpers import url_for
from flask_appbuilder.api import expose
from flask_appbuilder.baseviews import BaseView
from flask_appbuilder.security.decorators import has_access
from .models import Asignatura, Asistencia, Clase, Curso, Departamento, Docente, Estudiante, EstudianteMatriculaCurso, Periodo, PlanAsignatura, PlanEstudio, ProgramaAcademico, Salon
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from flask import g
from flask_appbuilder.security.sqla.models import User
from flask import current_app, redirect

from . import appbuilder, db
import app

# TODO: Probar related views
# related_views = [EmployeeView]


class ClassesView(BaseView):
    


    
    default_view = 'listaClases'
    @has_access
    @expose('/listaClases')
    def listaClases(self):
        
        roles = {
        "Admin": current_app.appbuilder.sm.find_role(
            current_app.appbuilder.sm.auth_role_admin
        ),
        "Estudiante": current_app.appbuilder.sm.find_role("Estudiante"),
        "Profesor": current_app.appbuilder.sm.find_role("Profesor"),
        }
        
        if g.user.roles[0] == roles['Estudiante']:
            id = db.session.query(Estudiante.id).filter_by(email=g.user.email).one()[0]
            data = db.session.query(EstudianteMatriculaCurso.curso_id, Periodo.nombre, Asignatura.nombre, Docente.nombre,Clase.inicio, Clase.fin, Clase.salon_id, Clase.id).filter_by(estudiante_id=id).\
                join(Periodo, Periodo.id==EstudianteMatriculaCurso.periodo_id).\
                join(Curso, EstudianteMatriculaCurso.curso_id==Curso.id).\
                join(Asignatura, Curso.asignatura_id==Asignatura.id).\
                join(Clase, Clase.curso_id==Curso.id).\
                join(Docente, Docente.id==Curso.docente_id).all()
            db.session.close()
            return render_template('ListaClases.html', user=g.user, data=data)
        if g.user.roles[0] == roles['Profesor']:
            id = db.session.query(Docente.id).filter_by(email=g.user.email).one()[0]
            data = db.session.query(Curso.id, Periodo.nombre, Asignatura.nombre, Docente.nombre, Clase.inicio, Clase.fin, Clase.salon_id, Clase.id).filter_by(docente_id=id).\
                join(Periodo, Periodo.id==Curso.periodo_id).\
                join(Asignatura, Asignatura.id==Curso.asignatura_id).\
                join(Docente, Docente.id==Curso.docente_id).\
                join(Clase, Clase.curso_id==Curso.id).all()
            db.session.close()
            return render_template('ListaClases.html', user=g.user, data=data)
        else:
            data = db.session.query(Curso.id, Periodo.nombre, Asignatura.nombre, Docente.nombre, Clase.inicio, Clase.fin, Clase.salon_id, Clase.id).\
                join(Periodo, Periodo.id==Curso.periodo_id).\
                join(Asignatura, Asignatura.id==Curso.asignatura_id).\
                join(Docente, Docente.id==Curso.docente_id).\
                join(Clase, Clase.curso_id==Curso.id).all()
            db.session.close()
            return render_template('ListaClases.html', user=g.user, data=data)
    
    @has_access
    @expose('/clase/<id>')
    def ClaseMethod(self, id):
        
        roles = {
        "Admin": current_app.appbuilder.sm.find_role(
            current_app.appbuilder.sm.auth_role_admin
        ),
        "Estudiante": current_app.appbuilder.sm.find_role("Estudiante"),
        "Profesor": current_app.appbuilder.sm.find_role("Profesor"),
        }
        
        data = db.session.query(Asistencia.estudiante_id, Estudiante.nombre, Asistencia.estado).filter(Asistencia.clase_id==id).\
                            join(Estudiante, Estudiante.id==Asistencia.estudiante_id).all()
                            
        data = [[dato if dato != None else '' for dato in row] for row in data]
        
        clase = db.session.query(Clase.id, Clase.inicio, Clase.fin, Clase.salon_id).filter(Clase.id==id).one()

        c = [clase[1].date(), clase[1].strftime('%A'), clase[1].time(), clase[2].time(), clase[3]]
        
        
        materia = db.session.query(Clase.id, Curso.asignatura_id, Asignatura.nombre).filter(Clase.id==1).\
            join(Curso, Curso.id==Clase.curso_id).\
            join(Asignatura, Asignatura.id==Curso.asignatura_id).one()
        
        if g.user.roles[0] == roles['Estudiante']:
            
            return render_template('Clase.html', user=g.user, data=data, materia=materia, clase=c)
        else:
            
            s1='Al presionar este botón se generará toda la lista de clases para que los estudiantes puedan ingresar su asistencia'
            s2='Iniciar la clase'
            
            return render_template('ClaseProfesor.html', user=g.user, button=s2, label=s1, id=id, data=data, materia=materia, clase=c)
    
    @has_access
    @expose('/iniciarclase/<id>')
    def IniciarClase(self, id):
        
        data = db.session.query(Asistencia).filter(Asistencia.clase_id==id).all()
        if len(data) != 0:
            return redirect(f'http://localhost:5000/classesview/clase/{id}')
        
        
        profesor = db.session.query(Clase.id, Clase.curso_id, Curso.docente_id).filter(Clase.id==id).\
                join(Curso, Curso.id==Clase.curso_id).one()

        estudiantes = db.session.query(Clase.id, Clase.curso_id, EstudianteMatriculaCurso.estudiante_id).filter(Clase.id==id).\
                join(EstudianteMatriculaCurso, EstudianteMatriculaCurso.curso_id==Clase.curso_id).all()
                
        asistencias = [
            Asistencia(clase_id=profesor[0], curso_id=profesor[1], docente_id=profesor[2])
        ]

        for estudiante in estudiantes:
            asistencias += [Asistencia(clase_id=estudiante[0], curso_id=estudiante[1], estudiante_id=estudiante[2])]
            
        try:
            db.session.add_all(asistencias)
            db.session.commit()
            db.session.close
        except Exception as e:
            print(e)
            db.session.rollback()
        
        return redirect(f'http://localhost:5000/classesview/clase/{id}')

class DepartamentoView(ModelView):
    datamodel = SQLAInterface(Departamento)
    add_columns=['id','nombre']
    list_columns=['id','nombre']
    show_columns=['id','nombre']

class ProgramaAcademicoView(ModelView):
    datamodel = SQLAInterface(ProgramaAcademico)
    add_columns=['id','nombre','departamento']
    list_columns=['id','nombre','departamento']
    show_columns=['id','nombre','departamento']
    
class AsignaturaView(ModelView):
    datamodel = SQLAInterface(Asignatura)
    add_columns=['id','nombre','departamento']
    list_columns=['id','nombre','departamento']
    show_columns=['id','nombre','departamento']
    
class PlanEstudioView(ModelView):
    datamodel = SQLAInterface(PlanEstudio)
    add_columns=['id','nombre','programa']
    list_columns=['id','nombre','programa']
    show_columns=['id','nombre','programa']

class PlanAsignaturaView(ModelView):
    datamodel = SQLAInterface(PlanAsignatura)
    add_columns=['id','asignatura','plan']
    list_columns=['id','asignatura','plan']
    show_columns=['id','asignatura','plan']
    
    
class PeriodoView(ModelView):
    datamodel = SQLAInterface(Periodo)
    add_columns=['id','nombre']
    list_columns=['id','nombre']
    show_columns=['id','nombre']
    
class SalonView(ModelView):
    datamodel = SQLAInterface(Salon)
    add_columns=['id']
    list_columns=['id']
    show_columns=['id']
    
class DocenteView(ModelView):
    datamodel = SQLAInterface(Docente)
    add_columns=['id','nombre', 'direccion', 'email','cedula', 'departamento']
    list_columns=['id','nombre', 'direccion', 'email', 'cedula', 'departamento']
    show_columns=['id','nombre', 'direccion', 'email', 'cedula', 'departamento']

class CursoView(ModelView):
    datamodel = SQLAInterface(Curso)
    add_columns=['id', 'docente', 'asignatura']
    list_columns=['id', 'docente', 'asignatura']
    show_columns=['id', 'docente', 'asignatura']
    
class ClaseView(ModelView):
    datamodel = SQLAInterface(Clase)
    add_columns=['id', 'curso', 'inicio', 'fin', 'salon']
    list_columns=['id', 'curso', 'inicio', 'fin', 'salon']
    show_columns=['id', 'curso', 'inicio', 'fin', 'salon']
    
class EstudianteMatriculaView(ModelView):
    datamodel = SQLAInterface(EstudianteMatriculaCurso)
    add_columns=['curso', 'periodo', 'estudiante']
    list_columns=['curso', 'periodo', 'estudiante']
    show_columns=['curso', 'periodo', 'estudiante']

class EstudianteView(ModelView):
    datamodel = SQLAInterface(Estudiante)
    add_columns=['id','nombre', 'direccion', 'email', 'cedula', 'telefono', 'plan', 'periodo']
    list_columns=['id','nombre', 'direccion', 'email', 'cedula', 'telefono', 'plan', 'periodo']
    show_columns=['id','nombre', 'direccion', 'email', 'cedula', 'telefono', 'plan', 'periodo']

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

appbuilder.add_view(
    ClassesView, "Lista de clases", icon="fa-folder-open-o", category="Lista de clases"
)