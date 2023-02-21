from models import *
import peewee

if __name__ == '__main__':
    try:
        db.connect()
        User.create_table()
        Day.create_table()
    except peewee.InternalError as px:
        print(str(px))
