import datetime


def strftime(time):
    return datetime.datetime.strftime(time, '%Y-%m-%d %H:%M:%S')


def get_now():
    now = datetime.datetime.now()
    return strftime(now)

