from models import *
from peewee import *
import datetime

# Стоит оптимизировать с помощью get_or_create
def create_user_if_not_exists(id):
    if is_user_exists(id):
        User.Create(telegram_id=id)
        return True
    return False

def is_user_exists(id):
    exist = True
    try:
        User.select().where(User.telegram_id == id).get()
    except DoesNotExist as de:
        exist = False
    return exist

# Стоит оптимизировать с помощью get_or_create
def renew_counter(id):
    exist = True
    try:
        day = Day.select().where((Day.user.telegram_id == id) & (Day.date=datetime.datetime.now().date())).get()
    except DoesNotExist as de:
        exist = False
    if not exist:
        user = User.select().where(User.telegram_id == id).get()
        Day.create(user=user, sigarets_count=0, date=datetime.datetime.now().date())
        return True
def add_counter(id):
    try:
        renew_counter(id)
        day = Day.select().where((Day.user.telegram_id) == id & (Day.date=datetime.datetime.now().date())).get()
        day.sigarets_count += 1
        day.save()
        return True
    except:
        return False
def reduse_counter(id):
    try:
        renew_counter(id)
        day = Day.select().where((Day.user.telegram_id) == id & (Day.date=datetime.datetime.now().date())).get()
        day.sigarets_count -= 1
        day.save()
        return True
    except:
        return False
def get_today_counter(id):
    day = Day.select().where((Day.user.telegram_id) == id & (Day.date=datetime.datetime.now().date())).get()
    return day.sigarets_count
def get_counter_by_date(id, date):
    day = Day.select().where((Day.user.telegram_id) == id & (Day.date=date).get()
    return day.sigarets_count