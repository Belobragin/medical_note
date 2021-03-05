""" model module for hometask"""

from sqlalchemy.ext.declarative import declarative_base
import time, sys, os, json, uuid, datetime, random, string
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import create_engine, Column, Integer, String, Table,\
                       DateTime, ForeignKey

from hardcode import *

Base = declarative_base()

class FK(Base):
    """ simple model to import foreign key"""
    __tablename__ = helptable
    id = Column(UUID(as_uuid=True), default=uuid.uuid4(), primary_key=True)
    

class ModelTable(Base):
    """ Model as in part 1 of the hometask """
    __tablename__ = tablename
    
    id = Column(UUID(as_uuid=True), default=uuid.uuid4(), primary_key=True)
    title = Column('title', String(256), nullable = False)
    parent_id = Column(
        UUID(as_uuid=True),
        ForeignKey('fk.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    registered_in = Column(DateTime, default=datetime.datetime.utcnow)    


class TaskTable(Base):
    """ this is a model with tree structure """
    __tablename__ = taskname
    
    id = Column(UUID(as_uuid=True), default=uuid.uuid4(), primary_key=True)
    title = Column('title', String(256), nullable = False)
    parent_id = Column(
        UUID(as_uuid=True),
        ForeignKey('fk.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    registered_in = Column(DateTime, default=datetime.datetime.utcnow)
    level1 = Column(String(16), nullable = False)
    level2 = Column(String(16), nullable = False)
    level3 = Column(String(16), nullable = False)
    level4 = Column(String(16), nullable = False)
    level5 = Column(String(16), nullable = False)