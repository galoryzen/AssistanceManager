from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Sequence
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
    
class Asignatura(Model):
    __tablename__ = 'asignatura'
    id = Column(String(7), primary_key=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    departamento_id = Column(Integer, ForeignKey("departamento.id"), nullable=False)
    departamento = relationship("Departamento")
    
    def __repr__(self):
        return self.nombre
    
class PlanEstudio(Record, Model):
    __tablename__ = 'plan_estudio'
    programa_id = Column(Integer, ForeignKey("prog_academico.id"), nullable=False)
    programa = relationship("ProgramaAcademico")
    
class PlanAsignatura(Model):
    __tablename__ = 'plan_asignatura'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    asignatura_id = Column(String(7), ForeignKey("asignatura.id"), nullable=False)
    asignatura = relationship("Asignatura")
    plan_id = Column(Integer, ForeignKey("plan_estudio.id"), nullable=False)
    plan = relationship("PlanEstudio")

class Periodo(Record, Model):
    __tablename__ = 'periodo'
    
class Salon(Model):
    __tablename__ = 'salon'
    id = Column(String(20), primary_key=True)
    
    def __repr__(self):
        return self.id
    
class Docente(Record, Model):
    __tablename__ = 'docente'
    direccion = Column(String(100), nullable=False)
    cedula = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    departamento_id = Column(Integer, ForeignKey("departamento.id"), nullable=False)
    departamento = relationship("Departamento")
    
class Curso(Model):
    __tablename__ = 'curso'
    id = Column(Integer, primary_key=True, nullable=False)
    docente_id = Column(Integer, ForeignKey("docente.id"), nullable=False)
    docente = relationship("Docente")
    asignatura_id = Column(String(7), ForeignKey("asignatura.id"), nullable=False)
    asignatura = relationship("Asignatura")
    periodo_id = Column(Integer, ForeignKey("periodo.id"), nullable=False)
    periodo = relationship("Periodo")
    
    def __repr__(self):
        return str(self.docente) + " - "+str(self.asignatura)  + " - " + str(self.id)    

class Clase(Model):
    __tablename__ = 'clase'
    id = Column(Integer, Sequence('id_seq', start=1), primary_key=True)
    curso_id = Column(Integer, ForeignKey("curso.id"), nullable=False)
    curso = relationship("Curso")
    inicio = Column(DateTime, nullable=False)
    fin = Column(DateTime, nullable=False)
    salon_id = Column(String(20), ForeignKey("salon.id"), nullable=False)
    salon = relationship("Salon") 

    def __repr__(self):
        return self.curso+" - " + self.inicio + " - " + self.salon

class EstudianteMatriculaCurso(Model):
    __tablename__ = 'estudiante_matricula'
    id = Column(Integer, Sequence('id_seq', start=1), primary_key=True)
    curso_id = Column(Integer, ForeignKey("curso.id"), nullable=False)
    curso = relationship("Curso")
    periodo_id = Column(Integer, ForeignKey("periodo.id"), nullable=False)
    periodo = relationship("Periodo")
    estudiante_id = Column(Integer, ForeignKey("estudiante.id"), nullable=False)
    estudiante = relationship("Estudiante")
    
    def __repr__(self):
        return str(self.curso_id)
    
    
class Estudiante(Model, Record):
    direccion = Column(String(100), nullable=False)
    cedula = Column(String(100), nullable=False, unique=True)
    telefono = Column(String(100), nullable=False, unique=True)
    plan_id = Column(Integer, ForeignKey("plan_estudio.id"), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    plan = relationship("PlanEstudio")
    periodo_id = Column(Integer, ForeignKey("periodo.id"), nullable=False)
    periodo = relationship("Periodo")
    
    
class Asistencia(Model):
    id = Column(Integer, Sequence('id_seq', start=1), primary_key=True)
    estudiante_id = Column(Integer, ForeignKey("estudiante.id"), nullable=True)
    estudiante = relationship("Estudiante")
    docente_id = Column(Integer, ForeignKey("docente.id"), nullable=True)
    docente = relationship("Docente")
    hora_asistencia = Column(DateTime, nullable=True)
    estado = Column(String(10), nullable = True)
    curso_id = Column(Integer, ForeignKey("curso.id"), nullable=False)
    curso = relationship("Curso")
    
    def __repr__(self):
        if self.estudiante_id == None:
            return self.estudiante_id + " - " + self.hora_asistencia + " - " + self.estado + " - " + self.curso_id