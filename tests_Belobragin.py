"""unittests for hometask"""

import unittest, time, sys, os, requests, json, warnings

import sqlalchemy 
import sqlalchemy.orm as orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists

warnings.simplefilter("ignore")

from hardcode import *
from models import FK, TaskTable
from htask_Belobragin import OurSweatFoo

class TableCreationTest(unittest.TestCase):
    """
    tests:
    1. psql table creation with fields on-demand
    2. table data fill
    """         

    def setUp(self):
        self.engine = engine
        Session = orm.sessionmaker(bind=engine)
        self.session = Session()

        warnings.simplefilter("ignore")

    def test_mnote_db(self):
        """ tests mnote validness """
        self.assertTrue(database_exists(self.engine.url))
        self.assertTrue(engine.dialect.has_table(engine, taskname))
        temp = self.engine.execute(f"select column_name, data_type\
                                    from information_schema.columns\
                                    where table_name = '{taskname}';").fetchall()
        self.assertTrue(temp[0][0] == 'id')
        self.assertTrue(temp[1][0] == 'title')
        self.assertTrue(temp[2][0] == 'parent_id')
        self.assertTrue(temp[3][0] == 'registered_in')
        self.assertTrue(temp[4][0] == 'level1')
        self.assertTrue(temp[5][0] == 'level2')
        self.assertTrue(temp[6][0] == 'level3')
        self.assertTrue(temp[7][0] == 'level4')
        self.assertTrue(temp[8][0] == 'level5')
        self.assertTrue(self.session.query(TaskTable).count() == 3125)
        
        #we can also test types, if urged: temp[...][1].__class__.__name__
    
    def test_fk_db(self):
        """ tests fk validness"""
        self.assertTrue(database_exists(self.engine.url))
        self.assertTrue(engine.dialect.has_table(engine, helptable))
        temp = self.engine.execute(f"select column_name, data_type\
                                    from information_schema.columns\
                                    where table_name = '{helptable}';").fetchall()
        self.assertTrue(temp[0][0] == 'id')
        self.assertTrue(self.session.query(FK).count() == 1)

    def test_mysweatfoo_start_node(self):
        """ tests OurSweatFoo start_node parameter"""        
        #test correct number of elements:
        result = OurSweatFoo(start_node = 'ABCD')
        self.assertTrue(len(result) == 5)
        [self.assertTrue(res.level1 == 'A') for res in result]
        [self.assertTrue(res.level2 == 'B') for res in result]
        [self.assertTrue(res.level3 == 'C') for res in result]
        [self.assertTrue(res.level4 == 'D') for res in result]
        #two levels elements:
        result = OurSweatFoo(start_node = 'ABC')
        self.assertTrue(len(result) == 25)
        [self.assertTrue(res.level1 == 'A') for res in result]
        [self.assertTrue(res.level2 == 'B') for res in result]
        [self.assertTrue(res.level3 == 'C') for res in result]
        #three levels elements:
        result = OurSweatFoo(start_node = 'AB')
        self.assertTrue(len(result) == 125)
        [self.assertTrue(res.level1 == 'A') for res in result]
        [self.assertTrue(res.level2 == 'B') for res in result]
        #four levels elements:
        result = OurSweatFoo(start_node = 'A')
        self.assertTrue(len(result) == 625)
        [self.assertTrue(res.level1 == 'A') for res in result]
         #five levels elements:
        result = OurSweatFoo()
        self.assertTrue(len(result) == 3125)

    def test_mysweatfoo_sort_dir(self):
        """ tests correct usage of "group by" statement in OurSweatFoo """   
        result = OurSweatFoo(start_node = 'AB')
        #we can take any field, 'title' just for сlarity:
        res_asc = [res.title for res in result]  #ascendency order
        result = OurSweatFoo(start_node = 'AB', sort_dir = DESC, ) 
        res_desc = [res.title for res in result] #descendency order - must be reverse to previous
        self.assertTrue(list(reversed(res_desc)) == res_asc)
        


