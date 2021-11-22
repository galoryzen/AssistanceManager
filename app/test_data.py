from datetime import datetime, timedelta
from flask_appbuilder.cli import create_admin
from flask import current_app
import logging

from sqlalchemy.sql.sqltypes import DateTime
from app import db
from app.models import Asignatura, Clase, Curso, Departamento, Docente, Estudiante, EstudianteMatriculaCurso, Periodo, PlanAsignatura, PlanEstudio, ProgramaAcademico, Salon, Asistencia
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
    Asignatura(id='IST7191', nombre='Redes de computacion', departamento_id=9),
    Asignatura(id='IST4360', nombre='Soluciones computacionales', departamento_id=9),
    Asignatura(id='IST4012', nombre='Estructura del computador I', departamento_id=9),
    Asignatura(id='IST2088', nombre='Algoritmia y programacion I', departamento_id=9),
    Asignatura(id='IST4031', nombre='Estructura de datos II-IS', departamento_id=9),
    Asignatura(id='IST4330', nombre='Estructuras discretas', departamento_id=9),
    Asignatura(id='IST7420', nombre='Optimizacion', departamento_id=9),
    Asignatura(id='ELP8044', nombre='Planeacion y org E-learning', departamento_id=9),
    Asignatura(id='IST2089', nombre='Algoritmia y programacion II', departamento_id=9),
    Asignatura(id='IST7410', nombre='Compiladores', departamento_id=9),
    Asignatura(id='IDS0025', nombre='Ciencia tecnologia y genero', departamento_id=9),
    Asignatura(id='IST7072', nombre='Diseño digital', departamento_id=9),
    Asignatura(id='IST0010', nombre='Introduccion a la ingenieria', departamento_id=9),
    Asignatura(id='ELP7196', nombre='Networking con Linux', departamento_id=9),
    Asignatura(id='IST4310', nombre='Algoritmos y complejidad', departamento_id=9),
    Asignatura(id='IST2110', nombre='Programacion orientada a objetos', departamento_id=9),
    Asignatura(id='IST7121', nombre='Diseño de software I', departamento_id=9),
    Asignatura(id='ELP8012', nombre='Inteligencia artificial', departamento_id=9),
    Asignatura(id='IST7102', nombre='Estructura del computador II', departamento_id=9),
    Asignatura(id='IST7081', nombre='Sistemas operacionales', departamento_id=9),
    Asignatura(id='IDS0040', nombre='Ciberetica', departamento_id=9),
    Asignatura(id='IST4452', nombre='Desarrollo aplicaciones web backend', departamento_id=9),
    Asignatura(id='ELP8011', nombre='Criptografia', departamento_id=9),
    Asignatura(id='INV7363', nombre='Proyecto final', departamento_id=9),
    Asignatura(id='IST4021', nombre='Estructura de datos I-IS', departamento_id=9),
    Asignatura(id='ELP8480', nombre='Gestion integrada en t.i', departamento_id=9),
    Asignatura(id='ELP2040', nombre='Fund de computacion grafica', departamento_id=9),
    Asignatura(id='IST4453', nombre='Desarrollo aplicaciones web frontend', departamento_id=9),
    Asignatura(id='ELP8124', nombre='Mineria de datos', departamento_id=9),
    Asignatura(id='IST7122', nombre='Diseño de software II', departamento_id=9),
    Asignatura(id='ELP7195', nombre='Redes de alta velocidad', departamento_id=9),
    Asignatura(id='ELP8510', nombre='Programacion mobil', departamento_id=9)
]

periodos = [
    Periodo(id=1, nombre='2021-10'),
    Periodo(id=2, nombre='2021-30'),
    Periodo(id=3, nombre='2022-10'),
    Periodo(id=4, nombre='2022-30')
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
    PlanEstudio(id=1, nombre='Ingenieria de Sistemas', programa_id=9),
    PlanEstudio(id=2, nombre='Ingenieria de Industrial', programa_id=10),
    PlanEstudio(id=3, nombre='Ingenieria de Electronica', programa_id=11)
]

planesAsignatura = [
    PlanAsignatura(id=1, asignatura_id='ELP2040', plan_id=1),
    PlanAsignatura(id=2, asignatura_id='ELP7195', plan_id=1),
    PlanAsignatura(id=3, asignatura_id='ELP7196', plan_id=1),
    PlanAsignatura(id=4, asignatura_id='ELP8011', plan_id=1),
    PlanAsignatura(id=5, asignatura_id='ELP8012', plan_id=1),
    PlanAsignatura(id=6, asignatura_id='ELP8044', plan_id=1),
    PlanAsignatura(id=7, asignatura_id='ELP8124', plan_id=1),
    PlanAsignatura(id=8, asignatura_id='ELP8480', plan_id=1),
    PlanAsignatura(id=9, asignatura_id='ELP8510', plan_id=1),
    PlanAsignatura(id=10, asignatura_id='IDS0025', plan_id=1),
    PlanAsignatura(id=11, asignatura_id='IDS0040', plan_id=1),
    PlanAsignatura(id=12, asignatura_id='INV7363', plan_id=1),
    PlanAsignatura(id=13, asignatura_id='IST0010', plan_id=1),
    PlanAsignatura(id=14, asignatura_id='IST2088', plan_id=1),
    PlanAsignatura(id=15, asignatura_id='IST2089', plan_id=1),
    PlanAsignatura(id=16, asignatura_id='IST2110', plan_id=1),
    PlanAsignatura(id=17, asignatura_id='IST4012', plan_id=1),
    PlanAsignatura(id=18, asignatura_id='IST4021', plan_id=1),
    PlanAsignatura(id=19, asignatura_id='IST4031', plan_id=1),
    PlanAsignatura(id=20, asignatura_id='IST4310', plan_id=1),
    PlanAsignatura(id=21, asignatura_id='IST4330', plan_id=1),
    PlanAsignatura(id=22, asignatura_id='IST4360', plan_id=1),
    PlanAsignatura(id=23, asignatura_id='IST4452', plan_id=1),
    PlanAsignatura(id=24, asignatura_id='IST4453', plan_id=1),
    PlanAsignatura(id=25, asignatura_id='IST7072', plan_id=1),
    PlanAsignatura(id=26, asignatura_id='IST7081', plan_id=1),
    PlanAsignatura(id=27, asignatura_id='IST7102', plan_id=1),
    PlanAsignatura(id=28, asignatura_id='IST7111', plan_id=1),
    PlanAsignatura(id=29, asignatura_id='IST7121', plan_id=1),
    PlanAsignatura(id=30, asignatura_id='IST7122', plan_id=1),
    PlanAsignatura(id=31, asignatura_id='IST7191', plan_id=1),
    PlanAsignatura(id=32, asignatura_id='IST7410', plan_id=1),
    PlanAsignatura(id=33, asignatura_id='IST7420', plan_id=1)
]

docentes = [
    Docente(id=1, nombre='Acevedo Garcia Felipe', direccion='Cl 47 21-118',email='fjacevedo@uninorte.edu.co' , cedula='1', departamento_id=9),
    Docente(id=2, nombre='Ardila Hernandez Carlos', direccion='Av 6 A 0 - 102',email='cardila@uninorte.edu.co', cedula='2', departamento_id=9),
    Docente(id=3, nombre='Avila Hernandez Karen', direccion='Cl 45 39-48',email='karena@uninorte.edu.co', cedula='3', departamento_id=9),
    Docente(id=4, nombre='Ballesteros Cantillo Blessed', direccion='Cr38 52-158',email='bballest@uninorte.edu.co', cedula='4', departamento_id=9),
    Docente(id=5, nombre='Calle Ariza Ingrid', direccion='Cr43 45-102 L 5 y 6',email='icalle@uninorte.edu.co', cedula='5', departamento_id=9),
    Docente(id=6, nombre='Camacho Diaz Amparo', direccion='Cl 76 43B Esq L-1',email='acamacho@uninorte.edu.co', cedula='6', departamento_id=9),
    Docente(id=7, nombre='Capacho Portilla Jose', direccion='Cr38 52-158',email='jcapacho@uninorte.edu.co', cedula='7', departamento_id=9),
    Docente(id=8, nombre='Delgado Osorio Erika', direccion='Cr7 D 45-06',email='edelgado@uninorte.edu.co', cedula='8', departamento_id=9),
    Docente(id=9, nombre='Diaz Duarte Sandra', direccion='Cr26 C7-79-33',email='sdiaz@uninorte.edu.co', cedula='9', departamento_id=9),
    Docente(id=10, nombre='Duarte Hernandez Marlene', direccion='Av 6 A 0 - 102',email='mduarte@uninorte.edu.co', cedula='10', departamento_id=9),
    Docente(id=11, nombre='Garcia Ramos Lucy', direccion='Cl 45 39-48',email='lucyr@uninorte.edu.co', cedula='11', departamento_id=9),
    Docente(id=12, nombre='Gonzalez Hernandez Liliana', direccion='Av González Valencia 52 - 69',email='gliliana@uninorte.edu.co', cedula='12', departamento_id=9),
    Docente(id=13, nombre='Guzman Reyes Luis', direccion='Calle 38 Sur N- 47 – 07',email='lgguzman@uninorte.edu.co', cedula='13', departamento_id=9),
    Docente(id=14, nombre='Jabba Molinares Daladier', direccion='Calle 36 # 24-40 ',email='djabba@uninorte.edu.co', cedula='14', departamento_id=9),
    Docente(id=15, nombre='Jimeno Paba Miguel', direccion='Cl 3 Oe 34 - 33',email='majimeno@uninorte.edu.co', cedula='15', departamento_id=9),
    Docente(id=16, nombre='Julliard Amador Pierre', direccion='Cr80 19-82',email='pjulliar@uninorte.edu.co', cedula='16', departamento_id=9),
    Docente(id=17, nombre='Leal Narvaez Nallig', direccion='Cr43 33 S-50 ',email='nleal@uninorte.edu.co', cedula='17', departamento_id=9),
    Docente(id=18, nombre='Llach Lopez Luis', direccion='Cr51 73 - 64',email='lllach@uninorte.edu.co', cedula='18', departamento_id=9),
    Docente(id=19, nombre='Mancilla Herrera Alfonso', direccion='Cr39 23 - 64', email='amancilla@uninorte.edu.co',cedula='19', departamento_id=9),
    Docente(id=20, nombre='Marquez Diaz Jose', direccion='Cr 80 #50-150',email='jmarquez@uninorte.edu.co', cedula='20', departamento_id=9),
    Docente(id=21, nombre='Martinez Troncoso Carlos', direccion='Carrera 42 # 21-14',email='cmartinez@uninorte.edu.co', cedula='21', departamento_id=9),
    Docente(id=22, nombre='Miranda Garcia Stella', direccion='Carrera 22 # 35-01',email='stellam@uninorte.edu.co', cedula='22', departamento_id=9),
    Docente(id=23, nombre='Nieto Bernal Wilson', direccion='Carrera 47g # 78d Sur 18',email='wnieto@uninorte.edu.co', cedula='23', departamento_id=9),
    Docente(id=24, nombre='Niño Ruiz Elias', direccion='Carrera 45 #73-31',email='enino@uninorte.edu.co', cedula='24', departamento_id=9),
    Docente(id=25, nombre='Piñeres Melo Marlon', direccion='Calle 13 # 24- 47', email='pineresm@uninorte.edu.co',cedula='25', departamento_id=9),
    Docente(id=26, nombre='Racedo Valbuena Sebastian', direccion='Cra 9 #49-47',email='racedo@uninorte.edu.co', cedula='26', departamento_id=9),
    Docente(id=27, nombre='Ramirez Parra Diego', direccion='Carrera 92 #4-89',email='rdiego@uninorte.edu.co', cedula='27', departamento_id=9),
    Docente(id=28, nombre='Ramos Rodriguez Rocio', direccion='Cl 1#5A-08',email='rramos@uninorte.edu.co', cedula='28', departamento_id=9),
    Docente(id=29, nombre='Saavedra Antolinez Ivan', direccion='Cl. 37 Sur, #72m49',email='saavedrai@uninorte.edu.co', cedula='29', departamento_id=9),
    Docente(id=30, nombre='Salazar Silva Augusto', direccion='Cl 127 C 15 - 02',email='augustosalazar@uninorte.edu.co', cedula='30', departamento_id=9),
    Docente(id=31, nombre='Teheran Sierra Jeny', direccion='Carrera 43 #82 - 66',email='jenyt@uninorte.edu.co', cedula='31', departamento_id=9),
    Docente(id=32, nombre='Villanueva Polanco Ricardo', direccion='Cr17 41-33',email='rpolanco@uninorte.edu.co', cedula='32', departamento_id=9),
    Docente(id=33, nombre='Wightman Rojas Pedro', direccion='Cr70 C 3-43',email='pwightman@uninorte.edu.co', cedula='33', departamento_id=9),
    Docente(id=34, nombre='Zurek Varela Eduardo', direccion='Cr17 10-21',email='ezurek@uninorte.edu.co', cedula='34', departamento_id=9)
]

cursos = [
    Curso(id=9854,  docente_id=3, asignatura_id='IST2088',periodo_id=1),
    Curso(id=8045,  docente_id=7, asignatura_id='IST2088',periodo_id=1),
    Curso(id=8042,  docente_id=8, asignatura_id='IST2088',periodo_id=1),
    Curso(id=8041,  docente_id=9, asignatura_id='IST2088',periodo_id=1),
    Curso(id=8043,  docente_id=11, asignatura_id='IST2088',periodo_id=1),
    Curso(id=8044,  docente_id=14, asignatura_id='IST2088',periodo_id=1),
    Curso(id=9851,  docente_id=28, asignatura_id='IST2088',periodo_id=1),
    Curso(id=9853,  docente_id=28, asignatura_id='IST2088',periodo_id=1),
    Curso(id=9852,  docente_id=28, asignatura_id='IST2088',periodo_id=1),
    Curso(id=8040,  docente_id=30, asignatura_id='IST2088',periodo_id=1),
    Curso(id=8038,  docente_id=32, asignatura_id='IST2088',periodo_id=1),
    Curso(id=8046,  docente_id=14, asignatura_id='IST2089',periodo_id=1),
    Curso(id=8055,  docente_id=7, asignatura_id='IST4310',periodo_id=1),
    Curso(id=8056,  docente_id=7, asignatura_id='IST4310',periodo_id=1),
    Curso(id=8081,  docente_id=18, asignatura_id='IST7111',periodo_id=1),
    Curso(id=7677,  docente_id=11, asignatura_id='IDS0040',periodo_id=1),
    Curso(id=7675,  docente_id=11, asignatura_id='IDS0025',periodo_id=1),
    Curso(id=8088,  docente_id=20, asignatura_id='IST7410',periodo_id=1),
    Curso(id=7255,  docente_id=31, asignatura_id='ELP8011',periodo_id=1),
    Curso(id=8082,  docente_id=23, asignatura_id='IST7121',periodo_id=1),
    Curso(id=8083,  docente_id=23, asignatura_id='IST7121',periodo_id=1),
    Curso(id=8084,  docente_id=16, asignatura_id='IST7122',periodo_id=1),
    Curso(id=8085,  docente_id=16, asignatura_id='IST7122',periodo_id=1),
    Curso(id=8075,  docente_id=17, asignatura_id='IST7072',periodo_id=1),
    Curso(id=8076,  docente_id=17, asignatura_id='IST7072',periodo_id=1),
    Curso(id=8074,  docente_id=12, asignatura_id='IST4453',periodo_id=1),
    Curso(id=8073,  docente_id=22, asignatura_id='IST4452',periodo_id=1),
    Curso(id=8054,  docente_id=28, asignatura_id='IST4031',periodo_id=1),
    Curso(id=8053,  docente_id=10, asignatura_id='IST4021',periodo_id=1),
    Curso(id=8052,  docente_id=10, asignatura_id='IST4021',periodo_id=1),
    Curso(id=8051,  docente_id=10, asignatura_id='IST4021',periodo_id=1),
    Curso(id=8050,  docente_id=34, asignatura_id='IST4012',periodo_id=1),
    Curso(id=8079,  docente_id=30, asignatura_id='IST7102',periodo_id=1),
    Curso(id=8080,  docente_id=30, asignatura_id='IST7102',periodo_id=1),
    Curso(id=8058,  docente_id=19, asignatura_id='IST4330',periodo_id=1),
    Curso(id=8057,  docente_id=19, asignatura_id='IST4330',periodo_id=1),
    Curso(id=7240,  docente_id=27, asignatura_id='ELP2040',periodo_id=1),
    Curso(id=7264,  docente_id=6, asignatura_id='ELP8480',periodo_id=1),
    Curso(id=9850,  docente_id=24, asignatura_id='IST0010',periodo_id=1),
    Curso(id=9848,  docente_id=24, asignatura_id='IST0010',periodo_id=1),
    Curso(id=9849,  docente_id=24, asignatura_id='IST0010',periodo_id=1),
    Curso(id=7256,  docente_id=34, asignatura_id='ELP8012',periodo_id=1),
    Curso(id=7262,  docente_id=29, asignatura_id='ELP8124',periodo_id=1),
    Curso(id=7248,  docente_id=21, asignatura_id='ELP7196',periodo_id=1),
    Curso(id=8090,  docente_id=2, asignatura_id='IST7420',periodo_id=1),
    Curso(id=8089,  docente_id=24, asignatura_id='IST7420',periodo_id=1),
    Curso(id=7261,  docente_id=4, asignatura_id='ELP8044',periodo_id=1),
    Curso(id=7265,  docente_id=30, asignatura_id='ELP8510',periodo_id=1),
    Curso(id=8048,  docente_id=15, asignatura_id='IST2110',periodo_id=1),
    Curso(id=8049,  docente_id=15, asignatura_id='IST2110',periodo_id=1),
    Curso(id=8047,  docente_id=33, asignatura_id='IST2110',periodo_id=1),
    Curso(id=8009,  docente_id=23, asignatura_id='INV7363',periodo_id=1),
    Curso(id=7247,  docente_id=5, asignatura_id='ELP7195',periodo_id=1),
    Curso(id=8086,  docente_id=20, asignatura_id='IST7191',periodo_id=1),
    Curso(id=8087,  docente_id=32, asignatura_id='IST7191',periodo_id=1),
    Curso(id=8077,  docente_id=20, asignatura_id='IST7081',periodo_id=1),
    Curso(id=8078,  docente_id=33, asignatura_id='IST7081',periodo_id=1),
    Curso(id=8066,  docente_id=1, asignatura_id='IST4360',periodo_id=1),
    Curso(id=8059,  docente_id=2, asignatura_id='IST4360',periodo_id=1),
    Curso(id=8061,  docente_id=2, asignatura_id='IST4360',periodo_id=1),
    Curso(id=8062,  docente_id=13, asignatura_id='IST4360',periodo_id=1),
    Curso(id=8064,  docente_id=19, asignatura_id='IST4360',periodo_id=1),
    Curso(id=8068,  docente_id=25, asignatura_id='IST4360',periodo_id=1),
    Curso(id=8065,  docente_id=25, asignatura_id='IST4360',periodo_id=1),
    Curso(id=8063,  docente_id=25, asignatura_id='IST4360',periodo_id=1),
    Curso(id=8070,  docente_id=25, asignatura_id='IST4360',periodo_id=1),
    Curso(id=8067,  docente_id=25, asignatura_id='IST4360',periodo_id=1),
    Curso(id=8069,  docente_id=26, asignatura_id='IST4360',periodo_id=1),
    Curso(id=8060,  docente_id=2, asignatura_id='IST4360',periodo_id=1)
]

estudiantes = [
    Estudiante(id=1, nombre='Gonzalez Benitez Sebastian', direccion='Vía 40 No 36 – 135', email='gonzalezes@uninorte.edu.co', cedula='5200135574', telefono='13510415 ', plan_id=1, periodo_id=1),
    Estudiante(id=2, nombre='Hernandez Lopez Marcela', direccion='Carrera 43 # 47 – 53.',email='vmhernandez@uninorte.edu.co', cedula='1200048588', telefono='453348202', plan_id=1, periodo_id=1),
    Estudiante(id=3, nombre='Howard Ortega Jack', direccion='Km 1.5 Prolongación Cl Murillo',email='howardj@uninorte.edu.co', cedula='2200131175', telefono='353230034', plan_id=1, periodo_id=1),
    Estudiante(id=4, nombre='Lopez Grau Raul', direccion='Carrera 36 Calle 87 Esquina',email='jlopezr@uninorte.edu.co', cedula='3200134732', telefono='253483009', plan_id=1, periodo_id=1),
    Estudiante(id=5, nombre='Mendez Ortega Juan', direccion='Carrera 46 # 53-34 L-16',email='jpmendez@uninorte.edu.co', cedula='4200119629', telefono='153499292', plan_id=1, periodo_id=1)
]

EMC = [
    EstudianteMatriculaCurso(curso_id=7248, periodo_id=2, estudiante_id=1),
    EstudianteMatriculaCurso(curso_id=7248, periodo_id=2, estudiante_id=2),
    EstudianteMatriculaCurso(curso_id=7248, periodo_id=2, estudiante_id=4),
    EstudianteMatriculaCurso(curso_id=8057, periodo_id=2, estudiante_id=1),
    EstudianteMatriculaCurso(curso_id=8057, periodo_id=2, estudiante_id=2),
    EstudianteMatriculaCurso(curso_id=8057, periodo_id=2, estudiante_id=4),
    EstudianteMatriculaCurso(curso_id=8081, periodo_id=2, estudiante_id=4),
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
    Clase(curso_id=7248, inicio=datetime.now() + timedelta(minutes=1), fin=datetime.now() + timedelta(minutes=120), salon_id='31K'),
    Clase(curso_id=7248, inicio=datetime(2021, 11, 19, 12, 30, 0, 0), fin=datetime(2021, 11, 19, 13, 30, 0, 0), salon_id='31G2'),
    Clase(curso_id=8057, inicio=datetime.now() + timedelta(minutes=1), fin=datetime.now() + timedelta(minutes=120), salon_id='VIRTUAL'),
    Clase(curso_id=8057, inicio=datetime(2021, 11, 19, 12, 30, 0, 0), fin=datetime(2021, 11, 19, 13, 30, 0, 0), salon_id='VIRTUAL'),
    # Estructuras Discretas
    Clase(curso_id=8057, inicio=datetime(2021, 11, 9, 10, 30, 0, 0), fin=datetime(2021, 11, 16, 9, 30, 0, 0), salon_id='VIRTUAL', estado=True),
    Clase(curso_id=8057, inicio=datetime(2021, 11, 11, 10, 30, 0, 0), fin=datetime(2021, 11, 11, 12, 30, 0, 0), salon_id='VIRTUAL', estado=True),
    
    Clase(curso_id=8057, inicio=datetime(2021, 11, 16, 10, 30, 0, 0), fin=datetime(2021, 11, 16, 11, 30, 0, 0), salon_id='VIRTUAL', estado=True),
    Clase(curso_id=8057, inicio=datetime(2021, 11, 18, 10, 30, 0, 0), fin=datetime(2021, 11, 16, 12, 30, 0, 0), salon_id='VIRTUAL', estado=True),
    
    #Bases de datos
    Clase(curso_id=8081, inicio=datetime(2021, 11, 9, 18, 30, 0, 0), fin=datetime(2021, 11, 16, 20, 30, 0, 0), salon_id='31G2', estado=True),
    Clase(curso_id=8081, inicio=datetime(2021, 11, 11, 18, 30, 0, 0), fin=datetime(2021, 11, 11, 20, 30, 0, 0), salon_id='31K', estado=True),
    
    Clase(curso_id=8081, inicio=datetime(2021, 11, 16, 18, 30, 0, 0), fin=datetime(2021, 11, 16, 20, 30, 0, 0), salon_id='31G2', estado=True),
    Clase(curso_id=8081, inicio=datetime(2021, 11, 18, 18, 30, 0, 0), fin=datetime(2021, 11, 16, 20, 30, 0, 0), salon_id='31K', estado=True),
]

asistencias = [
    #Estructuras Discretas
    Asistencia(id='test1', clase_id=5, docente_id=19, hora_asistencia=datetime(2021, 11, 9, 10, 31, 0, 0), estado='Asistencia', curso_id=8057),
    Asistencia(id='test2', clase_id=6, docente_id=19, hora_asistencia=datetime(2021, 11, 11, 10, 31, 0, 0), estado='Asistencia', curso_id=8057),
    Asistencia(id='test3', clase_id=7, docente_id=19, hora_asistencia=datetime(2021, 11, 16, 10, 31, 0, 0), estado='Asistencia', curso_id=8057),
    Asistencia(id='test4', clase_id=8, docente_id=19, hora_asistencia=datetime(2021, 11, 18, 10, 31, 0, 0), estado='Asistencia', curso_id=8057),
    
    Asistencia(id='test5', clase_id=5, estudiante_id=4, hora_asistencia=datetime(2021, 11, 9, 10, 31, 30, 0), estado='Asistencia', curso_id=8057),
    Asistencia(id='test6', clase_id=6, estudiante_id=4, hora_asistencia=datetime(2021, 11, 11, 10, 32, 0, 0), estado='Asistencia', curso_id=8057),
    Asistencia(id='test7', clase_id=7, estudiante_id=4, hora_asistencia=datetime(2021, 11, 16, 10, 33, 0, 0), estado='Asistencia', curso_id=8057),
    Asistencia(id='test8', clase_id=8, estudiante_id=4, hora_asistencia=datetime(2021, 11, 18, 10, 34, 0, 0), estado='Asistencia', curso_id=8057),
    
    #Bases de datos
    Asistencia(id='test9', clase_id=9, docente_id=18, hora_asistencia=datetime(2021, 11, 9, 18, 31, 0, 0), estado='Asistencia', curso_id=8081),
    Asistencia(id='test10', clase_id=10, docente_id=18, hora_asistencia=datetime(2021, 11, 11, 18, 31, 0, 0), estado='Asistencia', curso_id=8081),
    Asistencia(id='test11', clase_id=11, docente_id=18, hora_asistencia=datetime(2021, 11, 16, 18, 31, 0, 0), estado='Asistencia', curso_id=8081),
    Asistencia(id='test12', clase_id=12, docente_id=18, hora_asistencia=datetime(2021, 11, 18, 18, 31, 0, 0), estado='Asistencia', curso_id=8081),
    
    Asistencia(id='test13', clase_id=9, estudiante_id=4, hora_asistencia=datetime(2021, 11, 9, 18, 31, 30, 0), estado='Asistencia', curso_id=8081),
    Asistencia(id='test14', clase_id=10, estudiante_id=4, hora_asistencia=datetime(2021, 11, 11, 18, 32, 0, 0), estado='Asistencia', curso_id=8081),
    Asistencia(id='test15', clase_id=11, estudiante_id=4, hora_asistencia=datetime(2021, 11, 16, 18, 33, 0, 0), estado='Asistencia', curso_id=8081),
    Asistencia(id='test16', clase_id=12, estudiante_id=4, hora_asistencia=None, estado='Ausencia', curso_id=8081),
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
    [db.session.add_all(asistencias)]
    db.session.commit()
except Exception as e:
    print(e)
    db.session.rollback()