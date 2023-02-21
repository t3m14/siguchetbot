from .models import *
from peewee import *
from datetime import date
# Стоит оптимизировать с помощью get_or_create
def create_user_if_not_exists(id):
    if is_user_exists(id):
        User.create(telegram_id=id)
        return True
    return False

def is_user_exists(id):
    try:
        User.select().where(User.telegram_id == id).get()
    except DoesNotExist as de:
        return True
    return False
def get_user_by_id(id):
    return User.select().where(User.telegram_id == id).get()
# Стоит оптимизировать с помощью get_or_create
def renew_counter(id):
    exist = True
    try:
        user = get_user_by_id(id)
        day = Day.select().where((Day.user == user) & (Day.date == date.today())).get()
    except DoesNotExist as de:
        exist = False
    if not exist:
        user = User.select().where(User.telegram_id == id).get()
        Day.create(user=user, sigarets_count=0, date=date.today())
        return True
def add_counter(id):
    try:
        renew_counter(id)
        user = get_user_by_id(id)
        day = Day.select().where((Day.user == user) & (Day.date == date.today())).get()
        day.sigarets_count += 1
        day.save()
        return True
    except Exception as e:
        print(e)
        return False
def reduse_counter(id):
    try:
        renew_counter(id)
        user = get_user_by_id(id)
        day = Day.select().where((Day.user == user) & (Day.date == date.today())).get()
        day.sigarets_count = day.sigarets_count - 1
        day.save()
        return True
    except Exception as e:
        print(e)
        return False
def get_today_counter(id):
    user = get_user_by_id(id)
    day = Day.select().where((Day.user == user) & (Day.date == date.today())).get()
    return day.sigarets_count
def get_counter_by_date(id, date):
    user = get_user_by_id(id)
    day = Day.select().where((Day.user == user) & (Day.date == date)).get()
    return day.sigarets_count