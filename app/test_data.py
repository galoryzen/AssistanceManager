from app import db
from flask_appbuilder.cli import create_admin
from flask import current_app
import logging
log = logging.getLogger(__name__)

roles = {
    "Admin": current_app.appbuilder.sm.find_role(
        current_app.appbuilder.sm.auth_role_admin
    ),
    "Public": current_app.appbuilder.sm.find_role("Public"),
}

try:
    user = current_app.appbuilder.sm.add_user(
        "admin", "admin", "admin", "admin@admin.com", roles['Admin'], "admin"
    )
    log.info("Creado usuario administrador")
    db.session.commit()
except Exception:
    db.session.rollback()