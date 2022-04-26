from enum import unique
from peewee import *

data_base = MySQLDatabase(
    'FastAPI',
    user = 'root', password = 'password',
    host = 'localhost', port = 3306

)

class user2(Model):
    username = CharField(max_length=50, unique = True)
    email = CharField(max_length=50)

    def __str__(self):
        return self.username
    
    class Meta:
        database = data_base
        table_name = 'user2'
