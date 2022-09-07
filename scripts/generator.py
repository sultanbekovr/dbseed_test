from test1.person.models import Employee
import json
import random
import datetime as DT
import pandas as pd

""" Я сначала писал скрипт для заполнения бл вручную, потом увидел
    что можно использовать db seeder, этот файл решил оставить"""

start_date = DT.datetime(2017, 1, 5)
end_date = DT.datetime(2022, 15, 15)

date_of_r = pd.date_range(
    min(start_date, end_date),
    max(start_date, end_date)
).strftime('%Y-%m-%d').tolist()

with open('russian_names.json', encoding='utf-8-sig') as f:
    data1 = json.load(f)

with open('russian_surnames.json', encoding='utf-8-sig') as f:
    data2 = json.load(f)

create_list = ['1', '2', '3', '4']
# head_list = ['2', '3', '4', '5']

x = 8

for i in range(70000):
    pos_random = random.choice(create_list)
    head_random = random.randint(5, x)
    if Employee.objects.get(pk=head_random).position > pos_random:
        salary_start = 0
        salary_end = 0
        match pos_random:
            case '1':
                salary_start = 300000
                salary_end = 600000
            case '2':
                salary_start = 600000
                salary_end = 800000
            case '3':
                salary_start = 800000
                salary_end = 1200000
            case '4':
                salary_start = 1200000
                salary_end = 1800000

        Employee.objects.create(name=random.choice(data1), surname=random.choice(data2), patronymic=random.choice(data1),
                                position=random.choice(create_list), date_of_receipt=random.choice(date_of_r),
                                salary=random.randint(salary_start, salary_end, 50000), head=Employee.objects.get(pk=head_random))
        x += 1