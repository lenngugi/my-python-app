
from peewee import *
from os import path
connection=path.dirname(path.realpath(__file__))
db=sqlitedatabase(path.join(connection,"mycollege.db"))
class users(model):
    name= charfield()
    email=charfield(unique=true)
    password=charfield()
    class meta:
      database=db
users.create_table(fail_silently=true)
users.create(name="ing", email="kinggmail.com",password="king")
print("user saved succefully")
