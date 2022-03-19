#!/usr/bin/env python3

import calendar
from calendar import monthrange
from itertools import count

start = {'day': 7, 'month': 3, 'year': 2022}
week_order = ['David', 'Alex', 'BrunoRS', 'BrunoA']
sat_order = ['Alex', 'BrunoRS', 'David', 'BrunoA']

def oncall_sched():
    count_week = 0
    rotation_count = 0
    next_res_week = 0
    next_res_sat = 0
    start_date = 0

    print("date,name")
    
    for month in range(start['month'], 13):
        if month == start['month']:
            start_date = start['day']
        else:
            start_date = 1

        for day in range(start_date, monthrange(start['year'], month)[1] + 1):
                if calendar.weekday(start['year'], month, day) == 5:
                    print("{}/{}/{},{}".format(day,month,start['year'],sat_order[0 + next_res_sat]))
                else:
                    print("{}/{}/{},{}".format(day,month,start['year'],week_order[0 + next_res_week]))
                
                count_week += 1
                if count_week == 7:
                    next_res_week += 1
                    next_res_sat += 1
                    count_week = 0
                    if rotation_count == len(week_order) - 1:
                        rotation_count = 0
                        next_res_week = 0
                        next_res_sat = 0
                    else:
                        rotation_count += 1

oncall_sched()