import sys
import peewee
from models import *

''' relates inputs to model names '''
models_dict = {'school': School, 'batch': Batch, 'student': Student}

''' creates tables of all models from models.py '''
def create():
    my_models_db.create_tables([School, Batch, User, Student])

''' prints all rows of specified table '''
def prints():
    if len(sys.argv) < 3:
        print ("Please specify a table to print")
    else:
        rows = models_dict[sys.argv[2]].select()
        for r in rows:
            print r

''' inserts row in specified table '''
def insert():
    if len(sys.argv) < 3:
        print ("Please specify a table")
        return

    ''' if inserting row into School table '''
    if sys.argv[2] == "school":
        if len(sys.argv) < 4:
            print ("Please provide a name for the school")
            return
        entry = School.create(name=sys.argv[3])
        print ("New school: " + str(entry))  

    ''' if inserting row into Batch table '''
    if sys.argv[2] == "batch":
        if len(sys.argv) < 5:
            print ("Please provide a school id and/or name")
            return
        entry = Batch.create(school_id=sys.argv[3], name=sys.argv[4])
        print ("New batch: " + str(entry))

    ''' if inserting row into Student table '''
    if sys.argv[2] == "student":
        if len(sys.argv) < 7:
            print ("Please provide all the attributes for a student")
            return
        entry = Student.create(batch_id=sys.argv[3], age=sys.argv[4], last_name=sys.argv[5], first_name=sys.argv[6])
        print ("New student: " + str(entry))

def delete():
    if len(sys.argv) < 4:
        print ("Please specify a model and/or object id to delete")
    else:
        Model = models_dict[sys.argv[2]]
        row = Model.delete().where(Model.id == sys.argv[3])
        row.execute()

dict = { 'create': create, 'print': prints, 'insert': insert, 'delete': delete }

if len(sys.argv) < 2:
    print ("Please enter an action")
else:
    for key in dict:
        if key == sys.argv[1]:
            dict[key]()
            sys.exit()
    print ("Undefined action %s" % sys.argv[1])

