from datetime import datetime
from flask.helpers import url_for
from flask_appbuilder.api import expose
from flask_appbuilder.baseviews import BaseView
from flask_appbuilder.security.decorators import has_access
from .models import Asignatura, Asistencia, Clase, Curso, Departamento, Docente, Estudiante, EstudianteMatriculaCurso, Periodo, PlanAsignatura, PlanEstudio, ProgramaAcademico, Salon
from flask import render_template, request
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from flask import g
from flask_appbuilder.security.sqla.models import User
from flask import current_app, redirect
from datetime import timedelta, datetime
import time
import threading
import random, string


from . import appbuilder, db
import app

# TODO: Probar related views
# related_views = [EmployeeView]


class ClassesView(BaseView):
    
    default_view = 'listaClases'
    @has_access
    @expose('/listaClases')
    def listaClases(self):
        dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        roles = {
        "Admin": current_app.appbuilder.sm.find_role(
            current_app.appbuilder.sm.auth_role_admin
        ),
        "Estudiante": current_app.appbuilder.sm.find_role("Estudiante"),
        "Profesor": current_app.appbuilder.sm.find_role("Profesor"),
        }
        
        if g.user.roles[0] == roles['Estudiante']:
            id = db.session.query(Estudiante.id).filter_by(email=g.user.email).one()[0]
            data = db.session.query(EstudianteMatriculaCurso.curso_id, Periodo.nombre, Asignatura.nombre, Docente.nombre,Clase.inicio, Clase.fin, Clase.salon_id, Clase.id).filter(EstudianteMatriculaCurso.estudiante_id==id).\
                join(Periodo, Periodo.id==EstudianteMatriculaCurso.periodo_id).\
                join(Curso, EstudianteMatriculaCurso.curso_id==Curso.id).\
                join(Asignatura, Curso.asignatura_id==Asignatura.id).\
                join(Clase, Clase.curso_id==Curso.id).\
                join(Docente, Docente.id==Curso.docente_id).all()
            db.session.close()
            
            clases = {}

            for clase in data:
                fecha = clase[4].date()
                clases[fecha] = clases.get(fecha, []) + [clase]

            fechas = sorted(clases.keys())
            
            return render_template('ListaClases.html', user=g.user, data=clases, fechas=fechas, dias=dias, meses=meses)
        if g.user.roles[0] == roles['Profesor']:
            id = db.session.query(Docente.id).filter_by(email=g.user.email).one()[0]
            data = db.session.query(Curso.id, Periodo.nombre, Asignatura.nombre, Docente.nombre, Clase.inicio, Clase.fin, Clase.salon_id, Clase.id).filter_by(docente_id=id).\
                join(Periodo, Periodo.id==Curso.periodo_id).\
                join(Asignatura, Asignatura.id==Curso.asignatura_id).\
                join(Docente, Docente.id==Curso.docente_id).\
                join(Clase, Clase.curso_id==Curso.id).all()
            db.session.close()
            clases = {}

            for clase in data:
                fecha = clase[4].date()
                clases[fecha] = clases.get(fecha, []) + [clase]

            fechas = sorted(clases.keys())
            
            return render_template('ListaClases.html', user=g.user, data=clases, fechas=fechas, dias=dias, meses=meses)
        else:
            data = db.session.query(Curso.id, Periodo.nombre, Asignatura.nombre, Docente.nombre, Clase.inicio, Clase.fin, Clase.salon_id, Clase.id).\
                join(Periodo, Periodo.id==Curso.periodo_id).\
                join(Asignatura, Asignatura.id==Curso.asignatura_id).\
                join(Docente, Docente.id==Curso.docente_id).\
                join(Clase, Clase.curso_id==Curso.id).all()
            db.session.close()
            clases = {}

            for clase in data:
                fecha = clase[4].date()
                clases[fecha] = clases.get(fecha, []) + [clase]

            fechas = sorted(clases.keys())
            
            return render_template('ListaClases.html', user=g.user, data=clases, fechas=fechas, dias=dias, meses=meses)
    
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
        
        clase = db.session.query(Clase.id, Clase.inicio, Clase.fin, Clase.salon_id).filter(Clase.id==id).one()
        clase = [clase[1].date(), clase[1].strftime('%A'), clase[1].time(), clase[2].time(), clase[3]]
        
        materia = db.session.query(Clase.id, Curso.asignatura_id, Asignatura.nombre).filter(Clase.id==id).\
            join(Curso, Curso.id==Clase.curso_id).\
            join(Asignatura, Asignatura.id==Curso.asignatura_id).one()
        
        data = db.session.query(Asistencia.estudiante_id, Estudiante.nombre, Asistencia.estado, Asistencia.id).filter(Asistencia.clase_id==id).\
                            join(Estudiante, Estudiante.id==Asistencia.estudiante_id).all()
        
        data_profesor = db.session.query(Asistencia.docente_id, Docente.nombre, Asistencia.id, Asistencia.estado).filter(Asistencia.clase_id==id).\
                            join(Docente, Docente.id==Asistencia.docente_id).all()
                            
        if len(data_profesor)==0:
            profe = db.session.query(Clase.id, Docente.nombre, Docente.id).filter(Clase.id==id).join(Curso, Curso.id==Clase.curso_id).join(Docente, Docente.id==Curso.docente_id).one()
            if g.user.roles[0] == roles['Estudiante']:
                return render_template('Clase.html', user=g.user, id=id, data=[], materia=materia, clase=clase,  class_code='Por generar', profesor=[profe[2], profe[1], 'Sin generar', 'Ausente', 'OrangeRed'])
            
            return render_template('ClaseProfesor.html', user=g.user, id=id, data=[], materia=materia, clase=clase, profesor=[profe[2], profe[1], 'Sin generar', 'Ausente', 'OrangeRed'])
        
        data_profesor = data_profesor[0] + ('DarkGreen',) #(21, 'Martinez Troncoso Carlos', '1F4LS2KPZZ8NVDE', 'Asistencia', 'DarkGreen')
        data = [[dato if dato != None else 'Sin registrar' for dato in row] for row in data]
        data = [estudiante + ['DarkGreen' if estudiante[2]=='Asistencia' else 'OrangeRed'] for estudiante in data] #[1, 'Gonzalez Benitez Sebastian', 'Ausencia', 'XD4KV0S2II3HOA3', 'black']

        if g.user.roles[0] == roles['Estudiante']:
            if clase[4] == 'VIRTUAL':
                my_id = db.session.query(Estudiante.id).filter(Estudiante.email==g.user.email).one()[0]
                code = db.session.query(Asistencia.id).filter(Asistencia.clase_id==id, Asistencia.estudiante_id==my_id).one_or_none()
                if code == None:
                    code = 'Por generar'
                else:
                    code = code[0]
            else:
                code = 'Dado por el profesor'
            
            return render_template('Clase.html', user=g.user, id=id, data=data, materia=materia, clase=clase,  class_code=code, profesor=data_profesor)
        
        
        return render_template('ClaseProfesor.html', user=g.user, id=id, data=data, materia=materia, clase=clase, profesor=data_profesor)
    
    @has_access
    @expose('/iniciarclase/<id>')
    def IniciarClase(self, id):
        
        if db.session.query(Clase.estado).filter(Clase.id==id).one()[0]:
            print('entr1')
            return redirect(f'http://localhost:5000/classesview/clase/{id}')
        
        
        profesor = db.session.query(Clase.id, Clase.curso_id, Curso.docente_id, Clase.inicio).filter(Clase.id==id).\
                join(Curso, Curso.id==Clase.curso_id).one()
                
        if datetime.now() > profesor[3] + timedelta(minutes=20) or datetime.now() < profesor[3]:
            print('entre')
            return redirect(f'http://localhost:5000/classesview/clase/{id}')

        estudiantes = db.session.query(Clase.id, Clase.curso_id, EstudianteMatriculaCurso.estudiante_id).filter(Clase.id==id).\
                join(EstudianteMatriculaCurso, EstudianteMatriculaCurso.curso_id==Clase.curso_id).all()
        
        
        a_id = getRandomID()
        while checkID(a_id):
            a_id = getRandomID()
        asistencias = [
            Asistencia(id=a_id,  clase_id=profesor[0], curso_id=profesor[1], docente_id=profesor[2], hora_asistencia=datetime.now(), estado=getEstadoAsistencia(current=datetime.now(), inicio=profesor[3]))
        ]

        for estudiante in estudiantes:
            a_id = getRandomID()
            while checkID(a_id):
                a_id = getRandomID()
            asistencias += [Asistencia(id=a_id, clase_id=estudiante[0], curso_id=estudiante[1], estudiante_id=estudiante[2])]
            
        try:
            db.session.add_all(asistencias)
            db.session.query(Clase).filter(Clase.id==id).\
                                    update({Clase.estado: True})
            db.session.commit()
            db.session.close
        except Exception as e:
            print(e)
            db.session.rollback()
            
        
        return redirect(f'http://localhost:5000/classesview/clase/{id}')
    
    @has_access
    @expose('/registrarse/<id>', methods=['POST'])
    def Registrarse(self, id):
        
        codigo_asistencia = request.form['codC']
        codigo_profesor = request.form['codP']

        test = db.session.query(Asistencia.clase_id, Asistencia.estado).filter(Asistencia.id==codigo_asistencia).all()
        
        if len(test)==0:
            return redirect(f'http://localhost:5000/classesview/clase/{id}')
        
        test_profesor = db.session.query(Asistencia.clase_id).filter(Asistencia.id==codigo_profesor).all()
        
        if len(test)==0 or test[0][1]!=None:
            print(1)
            print(test[0][1])
            return redirect(f'http://localhost:5000/classesview/clase/{id}')
        elif test[0][0] != test_profesor[0][0]:
            print(2)
            print(test[0][0])
            print(test_profesor[0][0])
            return redirect(f'http://localhost:5000/classesview/clase/{id}')
        
        
        inicio_clase = db.session.query(Asistencia.hora_asistencia).filter(Asistencia.id==codigo_profesor).one()[0]    
        try:
            db.session.query(Asistencia).filter(Asistencia.id==codigo_asistencia).\
                                            update({Asistencia.hora_asistencia: datetime.now(), Asistencia.estado: getEstadoAsistencia(inicio=inicio_clase, current=datetime.now())})
            db.session.commit()
            db.session.close()
            return redirect(f'http://localhost:5000/classesview/clase/{id}')
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

def checkID(id):
    a = db.session.query(Asistencia.id).filter(Asistencia.id==id).all()
    
    if len(a)!=0:
        return True
    else:
        return False
    
def getRandomID(n=15):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))

def getEstadoAsistencia(inicio: datetime, current: datetime):
    if current <= inicio + timedelta(minutes=10):
        return 'Asistencia'
    elif current <= inicio + timedelta(minutes=20):
        return 'Retraso'
    else:
        return 'Ausencia'
    
def check_asistencia():
    
    while True:
        
        print('Actualicé')
        clases = db.session.query(Clase.id).filter(Clase.inicio + timedelta(minutes=20) < datetime.now(), Clase.estado==True).all()
        clases = [clase[0] for clase in clases]

        db.session.query(Asistencia.id, Asistencia.clase_id, Asistencia.docente_id, Asistencia.estudiante_id, Asistencia.estado).filter(Asistencia.clase_id.in_(clases), Asistencia.estado==None).\
                        update({Asistencia.estado: 'Ausencia'}, synchronize_session=False)
        
        db.session.query(Clase.estado).filter(Clase.inicio + timedelta(minutes=20) < datetime.now(), Clase.estado==False).update({Clase.estado: None}, synchronize_session=False)
        
        db.session.commit()
        time.sleep(300)

Assistance_Thread = threading.Thread(target=check_asistencia)
Assistance_Thread.daemon = True
Assistance_Thread.start()