from .models import *
from peewee import *
from datetime import datetime, timedelta


def get_today_date():
    return datetime.now().date()
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
        day = Day.select().where((Day.user == user) & (Day.date == get_today_date())).get()
    except DoesNotExist as de:
        exist = False
    if not exist:
        user = User.select().where(User.telegram_id == id).get()
        Day.create(user=user, sigarets_count=0, date=get_today_date())
        return True


def add_counter(id):
    try:
        renew_counter(id)
        user = get_user_by_id(id)
        day = Day.select().where((Day.user == user) & (Day.date == get_today_date())).get()
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
        day = Day.select().where((Day.user == user) & (Day.date == get_today_date())).get()
        day.sigarets_count = day.sigarets_count - 1
        day.save()
        return True
    except Exception as e:
        print(e)
        return False


def get_today_counter(id):
    user = get_user_by_id(id)
    day = Day.select().where((Day.user == user) & (Day.date == get_today_date())).get()
    return day.sigarets_count


def get_counter_by_date(id, date):
    user = get_user_by_id(id)
    day = Day.select().where((Day.user == user) & (Day.date == date)).get()
    return day.sigarets_count


def get_yesterday_counter(id):
    try:
        return get_counter_by_date(id, get_today_date() - timedelta(days=1))
    except:
        return 0


def get_month_counter(id):
    more_than_month = True
    all_sum = 0
    user = User.select().where(User.telegram_id==id)
    try:
        Day.select().where((Day.date == get_today_date() - timedelta(days=30)) & (Day.user == user))
    except DoesNotExist as de:
        more_than_month = False
    if more_than_month:
        for day in Day.select().where((Day.date > get_today_date() - timedelta(days=30)) & (Day.user == user)):
            all_sum += day.sigarets_count
    else:
        for day in Day.select():
            all_sum += day.sigarets_count
    return all_sum
