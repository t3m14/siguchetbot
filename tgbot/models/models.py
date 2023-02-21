from peewee import *
import datetime

db = SqliteDatabase('main.db')
    
class User(Model):
    telegram_id = IntegerField()
    class Meta:
        database = db
class Day(Model):
    user = ForeignKeyField(User)
    sigarets_count = IntegerField()
    date = DateField(default=datetime.datetime.now().date())
    class Meta:
        database = db
        


