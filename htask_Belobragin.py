""" 
hometask assignment for position at medicalnote company 
- we suggest:
    A) unix user named postgres to use the postgres role
"""


import uuid, datetime, random, string

from typing import Tuple

from hardcode import * 
from models import FK, ModelTable, TaskTable, Base

SortDir: Tuple[str, str] = (ASC, DESC)


import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Table,\
                       DateTime, ForeignKey, desc
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_utils import database_exists, create_database


from sqlalchemy.dialects.postgresql import UUID

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

def create_our_db():
    """ creates database, if nothing """
    if not database_exists(engine.url):
        create_database(engine.url)    
    return

def create_all_tables():
    """ creates tables """
    Base.metadata.create_all(engine)
    return 

def rand_st(N):
    """ 
    populate table field with N symbol random value
    (uppercase + digits)
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

def populate_tables():
    """
    populates tables and inserts foreign keys
    """
    temp_id = uuid.uuid4()
    row_in = FK(id = temp_id)
    session.add(row_in)
    session.commit()

    #populate model TaskTable with test data:
    for i in NODE_NAMES:
        for j in NODE_NAMES:
            for k in NODE_NAMES:
                for p in NODE_NAMES:
                    for z in NODE_NAMES:
                        row_to_insert =  TaskTable(id = uuid.uuid4(),                     
                                                    title = rand_st(5),
                                                    parent_id = temp_id,
                                                    level1 = i,
                                                    level2 = j,
                                                    level3 = k,
                                                    level4 = p,
                                                    level5 = z,
                                                    )     
                        session.add(row_to_insert)    
    session.commit()
    return

def OurSweatFoo(SweatModel = TaskTable, 
                sore_fld = 'title',
                sort_dir: SortDir = ASC,
                depth : int = 1,
                start_node = None,
                ):
    """
    this foo returns demanded levels, sorted , and starting with given node
    - sore_fld :: field for sort
    - sort_dir :: asc/desc, asc by default
    - depth :: how many down levels to return
    - start_node :: node to start, None (default) - start from root
        ! Attn.: nodes are designated by 1 - 5 letters, for example:
            A - 1st node 1st level
            B - 2nd node 1st level
            CD - 4th node 2nd level (starting with 3rd node on level 1)
            EDCBA - 1st element (5th level, no descendents) of 2 nd node level4 
                    of 3rd node level 3 of 4th node level2 of 5th node level 1
            etc.
    """
    filter_list = []
    my_query = session.query(SweatModel)
    
    if depth.__class__.__name__ != 'int': raise ValueError('depth must be integer')
    
    if depth > 5:
        depth = 5 
    elif depth <= 1:
        depth = 0 

    # select elements of the given node:
    if start_node:
        for i, temp_node in enumerate(start_node):
            field_name = 'level' + str(i+1)            
            filter_list.append(getattr(SweatModel, field_name) == temp_node)
    temp = my_query.filter(*filter_list)
    
    #restrict output by depth parameter:
    #filter_list = filter_list[:depth]
    #depth argument is controversial and can not be reasonably interpreted
    
    #return sorted query:    
    if sort_dir == DESC: 
        return temp.order_by(getattr(SweatModel,sore_fld).desc()).all()

    return temp.order_by(getattr(SweatModel,sore_fld)).all()


if __name__ == '__main__':
    #create database:
    create_our_db()

    #create tables:
    create_all_tables()

    #populate tables:
    populate_tables()

    #make selection and sorting:
    temp = OurSweatFoo(start_node = 'ABCD',
                       sort_dir = DESC, 
                    )    
    #enjoy result:
    print([res.title for res in temp])
    

            
            


