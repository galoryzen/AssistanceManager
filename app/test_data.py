from datetime import datetime, timedelta
from flask_appbuilder.cli import create_admin
from flask import current_app
import logging

from sqlalchemy.sql.sqltypes import DateTime
from app import db
from app.models import Asignatura, Clase, Curso, Departamento, Docente, Estudiante, EstudianteMatriculaCurso, Periodo, PlanAsignatura, PlanEstudio, ProgramaAcademico, Salon
log = logging.getLogger(__name__)

try:
    db.drop_all()
    db.create_all()
except Exception as e:
    print(e)

deps= [
    Departamento(id=1, nombre='Dpto. de Economía'),
    Departamento(id=2, nombre='Dpto. Mercadeo y Neg. Internac'),
    Departamento(id=3, nombre='Dpto. Emprendim y Management'),
    Departamento(id=4, nombre='Dpto. Finanzas y Contaduría'),
    Departamento(id=5, nombre='Dpto.Ing Eléctrica-Electrónica'),
    Departamento(id=6, nombre='Dpto. Ingeniería Mecánica'),
    Departamento(id=7, nombre='Dpto. Ingeniería Industrial'),
    Departamento(id=8, nombre='Dpto. Ing. Civil y Ambiental'),
    Departamento(id=9, nombre='Dpto. Ingeniería de Sistemas'),
    Departamento(id=10, nombre='Dpto. Medicina'),
    Departamento(id=11, nombre='Dpto. Enfermería'),
    Departamento(id=12, nombre='Dpto. Salud Pública'),
    Departamento(id=13, nombre='Dpto. Odontología'),
    Departamento(id=14, nombre='Dpto. Comunicación Social'),
    Departamento(id=15, nombre='Dpto. Psicología'),
    Departamento(id=16, nombre='Dpto. Educación'),
    Departamento(id=17, nombre='Dpto. Humanidades y Filosofía'),
    Departamento(id=18, nombre='Dpto. Arquitectura y Urbanismo'),
    Departamento(id=19, nombre='Dpto. Historia y Cs. Sociales'),
    Departamento(id=20, nombre='Dpto. Diseño'),
    Departamento(id=21, nombre='Dpto. Cs Politica y Rel Intern'),
    Departamento(id=22, nombre='Dpto. Derecho'),
    Departamento(id=23, nombre='Dpto. Música'),
    Departamento(id=24, nombre='Dpto. Física'),
    Departamento(id=25, nombre='Dpto. Matematicas y estadístic'),
    Departamento(id=26, nombre='Dpto. Química y Biología'),
    Departamento(id=27, nombre='Dpto. Español'),
    Departamento(id=28, nombre='Dpto. Lenguas Extranjeras')
]

asignaturas = [
    Asignatura(id='IST7111', nombre='Bases de datos', departamento_id=9),
    Asignatura(id='IST4012', nombre='Redes de computacion', departamento_id=9),
    Asignatura(id='IST7191', nombre='Soluciones computacionales', departamento_id=9),
    Asignatura(id='IST4360', nombre='Estructura del computador I', departamento_id=9)
]

periodos = [
    Periodo(id=1, nombre='2021-10')
]

progsAcad = [
    ProgramaAcademico(id=1, nombre='Prog. de Economía', departamento_id=1),
    ProgramaAcademico(id=2, nombre='Prog. Mercadeo y Neg. Internac', departamento_id=2),
    ProgramaAcademico(id=3, nombre='Prog. Emprendim y Management', departamento_id=3),
    ProgramaAcademico(id=4, nombre='Prog. Finanzas y Contaduría', departamento_id=4),
    ProgramaAcademico(id=5, nombre='Prog.Ing Eléctrica-Electrónica', departamento_id=5),
    ProgramaAcademico(id=6, nombre='Prog. Ingeniería Mecánica', departamento_id=6),
    ProgramaAcademico(id=7, nombre='Prog. Ingeniería Industrial', departamento_id=7),
    ProgramaAcademico(id=8, nombre='Prog. Ing. Civil y Ambiental', departamento_id=8),
    ProgramaAcademico(id=9, nombre='Prog. Ingeniería de Sistemas', departamento_id=9),
    ProgramaAcademico(id=10, nombre='Prog. Medicina', departamento_id=10),
    ProgramaAcademico(id=11, nombre='Prog. Enfermería', departamento_id=11),
    ProgramaAcademico(id=12, nombre='Prog. Salud Pública', departamento_id=12),
    ProgramaAcademico(id=13, nombre='Prog. Odontología', departamento_id=13),
    ProgramaAcademico(id=14, nombre='Prog. Comunicación Social', departamento_id=14),
    ProgramaAcademico(id=15, nombre='Prog. Psicología', departamento_id=15),
    ProgramaAcademico(id=16, nombre='Prog. Educación', departamento_id=16),
    ProgramaAcademico(id=17, nombre='Prog. Humanidades y Filosofía', departamento_id=17),
    ProgramaAcademico(id=18, nombre='Prog. Arquitectura y Urbanismo', departamento_id=18),
    ProgramaAcademico(id=19, nombre='Prog. Historia y Cs. Sociales', departamento_id=19),
    ProgramaAcademico(id=20, nombre='Prog. Diseño', departamento_id=20),
    ProgramaAcademico(id=21, nombre='Prog. Cs Politica y Rel Intern', departamento_id=21),
    ProgramaAcademico(id=22, nombre='Prog. Derecho', departamento_id=22),
    ProgramaAcademico(id=23, nombre='Prog. Música', departamento_id=23),
    ProgramaAcademico(id=24, nombre='Prog. Física', departamento_id=24),
    ProgramaAcademico(id=25, nombre='Prog. Matematicas y estadístic', departamento_id=25),
    ProgramaAcademico(id=26, nombre='Prog. Química y Biología', departamento_id=26),
    ProgramaAcademico(id=27, nombre='Prog. Español', departamento_id=27),
    ProgramaAcademico(id=28, nombre='Prog. Lenguas Extranjeras', departamento_id=28)
]

planesEstudio = [
    PlanEstudio(id=1, nombre='Ingenieria de Sistemas', programa_id=9)
]

planesAsignatura = [
    PlanAsignatura(id=1, asignatura_id='IST7111', plan_id=1),
    PlanAsignatura(id=2, asignatura_id='IST4012', plan_id=1),
    PlanAsignatura(id=3, asignatura_id='IST7191', plan_id=1),
    PlanAsignatura(id=4, asignatura_id='IST4360', plan_id=1)
]

docentes = [
    Docente(id=1, nombre='Luis Llach', direccion='su casa', email='llach@uninorte.edu.co', cedula='72174800', departamento_id=9),
    Docente(id=2, nombre='Ricardo Villanueva', direccion='Pto', email='rvillanueva@uninorte.edu.co', cedula='72348481', departamento_id=9),
    Docente(id=3, nombre='Eduardo Zurek Varela', direccion='Soledad', email='ezurek@uninorte.edu.co', cedula='72167852', departamento_id=9),
    Docente(id=4, nombre='Marlon Pineres', direccion='atlantico', email='mpineres@uninorte.edu.co', cedula='72054493', departamento_id=9),
    Docente(id=5, nombre='Miguel Jimeno', direccion='Oracle', email='mjimeno@uninorte.edu.co', cedula='72245666', departamento_id=9)
]

cursos = [
    Curso(id=8087, docente_id=2, asignatura_id='IST4012'),
    Curso(id=8081, docente_id=1, asignatura_id='IST7111'),
    Curso(id=8082, docente_id=5, asignatura_id='IST7111'),
    Curso(id=8050, docente_id=3, asignatura_id='IST4360'),
    Curso(id=8051, docente_id=3, asignatura_id='IST4360'),
]

estudiantes = [
    Estudiante(id=1, nombre='Raul Lopez', direccion='su casa', email='jlopezr@uninorte.edu.co', cedula='1001805233', telefono='123', plan_id=1, periodo_id=1)
]

EMC = [
    EstudianteMatriculaCurso(id=1, curso_id=8087, periodo_id=1, estudiante_id=1),
    EstudianteMatriculaCurso(id=2, curso_id=8081, periodo_id=1, estudiante_id=1),
    EstudianteMatriculaCurso(id=3, curso_id=8050, periodo_id=1, estudiante_id=1),
]

salones = [
    Salon(id='31G2'),
    Salon(id='33E'),
    Salon(id='25E'),
    Salon(id='23D'),
    Salon(id='VIRTUAL'),
    Salon(id='31K')
]

clases = [
    Clase(curso_id=8087, inicio=datetime.now() + timedelta(minutes=2), fin=datetime.now() + timedelta(minutes=122), salon_id='VIRTUAL'),
    Clase(curso_id=8050, inicio=datetime.now() + timedelta(minutes=5), fin=datetime.now() + timedelta(minutes=125), salon_id='31K'),
]

try:
    [db.session.add_all(deps)]
    [db.session.add_all(salones)]
    [db.session.add_all(asignaturas)]
    [db.session.add_all(periodos)]
    [db.session.add_all(progsAcad)]
    [db.session.add_all(planesEstudio)]
    [db.session.add_all(planesAsignatura)]
    [db.session.add_all(docentes)]
    [db.session.add_all(cursos)]
    [db.session.add_all(estudiantes)]
    [db.session.add_all(EMC)]
    [db.session.add_all(clases)]
    db.session.commit()
except Exception as e:
    print(e)
    db.session.rollback()