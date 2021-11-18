from datetime import datetime, timedelta
from flask_appbuilder.cli import create_admin
from flask import current_app
import logging

from sqlalchemy.sql.sqltypes import DateTime
from app import db
from app.models import Asignatura, Clase, Curso, Departamento, Docente, Estudiante, EstudianteMatriculaCurso, Periodo, PlanAsignatura, PlanEstudio, ProgramaAcademico, Salon
log = logging.getLogger(__name__)


roles = {
    "Admin": current_app.appbuilder.sm.find_role(
        current_app.appbuilder.sm.auth_role_admin
    ),
    "Estudiante": current_app.appbuilder.sm.find_role("Estudiante"),
    "Profesor": current_app.appbuilder.sm.find_role("Profesor"),
}

current_app.appbuilder.sm.add_user(
    "admin", "admin", "admin", "admin@admin.com", roles["Admin"], "admin"
)

data = db.session.query(Docente.nombre, Docente.email).all()

d = []
    
for profesor in data:
    s = profesor[0].split(" ")
    nombre = s[2]
    apellidos = s[0] + " " + s[1]
    usuario = profesor[1].split("@")[0]
    d.append((nombre, apellidos, usuario, profesor[1]))

for profesor in d:
    current_app.appbuilder.sm.add_user(
        profesor[2], profesor[0], profesor[1], profesor[3], roles["Profesor"], profesor[2]
    )

data2 = db.session.query(Estudiante.nombre, Estudiante.email).all()
    
a = []

for estudiante in data2:
    s = estudiante[0].split(" ")
    nombre = s[2]
    apellidos = s[0] + " " + s[1]
    usuario = estudiante[1].split("@")[0]
    a.append((nombre, apellidos, usuario, estudiante[1]))
    
for estudiante in a:
    current_app.appbuilder.sm.add_user(
        estudiante[2], estudiante[0], estudiante[1], estudiante[3], roles["Estudiante"], estudiante[2]
    )