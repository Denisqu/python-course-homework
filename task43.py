# DONE


#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.

import calendar
from datetime import date, timedelta

def get_hermitage_discount_days(year):
    discount_days = []
    start_date = date(year, 1, 1)
    end_date = date(year+1, 1, 1)
    delta = timedelta(days=1)

    thursday_counter = 0
    current_month = start_date.month

    while start_date < end_date:
        if current_month != start_date.month:
            thursday_counter = 0
            current_month = start_date.month
            continue

        if start_date.weekday() == calendar.THURSDAY:
            thursday_counter += 1

        if thursday_counter == 3 and start_date.weekday() == calendar.THURSDAY:
            discount_days.append(start_date)

        start_date += delta

    return discount_days

print(get_hermitage_discount_days(2023))