from peewee import *
from os import path
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection,"mycollege.db"))
class Users(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    class Meta:
      database=db
Users.create_table(fail_silently=True)
#Users.create(name="king", email="kinggmail12443.com",password="king")
users=Users.select()
for user in users:
    print(user.email)


class products(Model):
    name= CharField()
    qtty= CharField()
    price= CharField()
    discount=CharField()
    class Meta:
        database= db
products.create_table(fail_silently=True)
products.create(name="sugar",qtty="1kg",price="ksh 100.00",discount="ksh10")
products = products.select()
for product in products:
     print(product.name)


