""" constants module for hometask """

from sqlalchemy import create_engine

NODE_NAMES = 'ABCDE'
ASC = 'asc'
DESC = 'dsc'

dblogin = 'postgres'
dbpassw = 'admin1'
dbanme = 'mnote'

tablename = 'mt'
taskname = 'taskt'
helptable = 'fk'

engine = create_engine(f"postgres://{dblogin}:{dbpassw}@localhost/{dbanme}")
