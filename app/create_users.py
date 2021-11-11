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

current_app.appbuilder.sm.add_user(
    "jlopezr", "Raul", "Lopez", "jlopezr@uninorte.edu.co", roles["Estudiante"], "123"
)

current_app.appbuilder.sm.add_user(
    "llach", "Luis", "Llach", "llach@uninorte.edu.co", roles["Profesor"], "123"
    )