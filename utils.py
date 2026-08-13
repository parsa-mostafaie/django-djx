from django.utils.timesince import timesince
import re

def persian_timesince(dt):
    if not dt:
        return ""

    en_time = timesince(dt)

    replacements = {
        'years': 'سال',
        'year': 'سال',
        'months': 'ماه',
        'month': 'ماه',
        'weeks': 'هفته',
        'week': 'هفته',
        'days': 'روز',
        'day': 'روز',
        'hours': 'ساعت',
        'hour': 'ساعت',
        'minutes': 'دقیقه',
        'minute': 'دقیقه',
        'seconds': 'ثانیه',
        'second': 'ثانیه',
        'ago': 'پیش',
    }

    fa_time = en_time
    for en, fa in replacements.items():
        fa_time = fa_time.replace(en, fa)

    persian_numbers = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }
    for en_num, fa_num in persian_numbers.items():
        fa_time = fa_time.replace(en_num, fa_num)

    fa_time = fa_time.replace('،', ' و')
    fa_time = re.sub(r'\s+', ' ', fa_time).strip()

    if fa_time == '۰ روز پیش':
        return 'امروز'
    elif fa_time == '۱ روز پیش':
        return 'دیروز'

    return fa_time