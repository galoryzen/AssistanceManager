from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Date

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
class Record:
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    
    def __repr__(self):
        return self.nombre
    
class Departamento(Record, Model):
    __tablename__ = 'departamento'
    
class ProgramaAcademico(Record, Model):
    __tablename__ = 'prog_academico'
    departamento_id = Column(Integer, ForeignKey("departamento.id"), nullable=False)
    departamento = relationship("Departamento")
    
class Asignatura(Record, Model):
    __tablename__ = 'asignatura'
    departamento_id = Column(Integer, ForeignKey("departamento.id"), nullable=False)
    departamento = relationship("Departamento")
    
class PlanEstudio(Record, Model):
    __tablename__ = 'plan_estudio'
    programa_id = Column(Integer, ForeignKey("prog_academico.id"), nullable=False)
    programa = relationship("ProgramaAcademico")
    
class PlanAsignatura(Model):
    __tablename__ = 'plan_asignatura'
    
    asignatura_id = Column(Integer, ForeignKey("asignatura.id"), nullable=False)
    asignatura = relationship("Asignatura")
    plan_id = Column(Integer, ForeignKey("plan_estudio.id"), nullable=False)
    plan = relationship("PlanEstudio")

class Periodo(Record, Model):
    __tablename__ = 'periodo'
    
class Salon(Model):
    __tablename__ = 'salon'
    id = Column(String(100), primary_key=True, nullable=False)
    
    def __repr__(self):
        return self.id
    
class Docente(Record, Model):
    __tablename__ = 'docente'
    direccion = Column(String(100), nullable=False)
    cedula = Column(String(100), nullable=False, unique=True)
    departamento_id = Column(Integer, ForeignKey("departamento.id"), nullable=False)
    departamento = relationship("Departamento")
    
class Curso(Record, Model):
    __tablename__ = 'curso'
    docente_id = Column(Integer, ForeignKey("docente.id"), nullable=False)
    docente = relationship("Docente")
    asignatura_id = Column(Integer, ForeignKey("asignatura.id"), nullable=False)
    asignatura = relationship("Asignatura")    

class Clase(Model):
    __tablename__ = 'clase'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    curso_id = Column(Integer, ForeignKey("curso.id"), nullable=False)
    curso = relationship("Curso")
    inicio = Column(DateTime, nullable=False)
    duracion = Column(Integer, nullable=False)  # En minutos
    salon_id = Column(String(100), ForeignKey("salon.id"), nullable=False)
    salon = relationship("Salon") 
    
    #UniqueConstraint('curso_id', 'salon_id','inicio', name="PK")

    def __repr__(self):
        return self.curso_id

class EstudianteMatriculaCurso(Model):
    __tablename__ = 'estudiante_matricula'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    curso_id = Column(Integer, ForeignKey("curso.id"), nullable=False)
    curso = relationship("Curso")
    periodo_id = Column(Integer, ForeignKey("periodo.id"), nullable=False)
    periodo = relationship("Periodo")
    estudiante_id = Column(Integer, ForeignKey("estudiante.id"), nullable=False)
    estudiante = relationship("Estudiante")
    
class Estudiante(Model, Record):
    direccion = Column(String(100), nullable=False)
    cedula = Column(String(100), nullable=False, unique=True)
    telefono = Column(String(100), nullable=False, unique=True)
    plan_id = Column(Integer, ForeignKey("plan_estudio.id"), nullable=False)
    plan = relationship("PlanEstudio")
    periodo_id = Column(Integer, ForeignKey("periodo.id"), nullable=False)
    periodo = relationship("Periodo")
    
    
    def __repr__(self):
        return self.estudiante_id