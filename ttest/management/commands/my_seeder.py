import random
from datetime import date, timedelta

from django_seed import Seed
from django.core.management.base import BaseCommand
from ttest.models import ForTest

class Command(BaseCommand):
    help = ' Just'

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        create_list = ['1', '2', '3', '4']

        x = 10000

        for j in range(6):
            for i in range(5000):

                pos_random = random.choice(create_list)
                head_random = random.randint(1, x)
                if ForTest.objects.get(pk=head_random).position > pos_random:

                    start_date = date(2016, 1, 1)
                    end_date = date(2022, 2, 1)

                    time_between_dates = end_date - start_date
                    days_between_dates = time_between_dates.days
                    random_number_of_days = random.randrange(days_between_dates)
                    random_date = start_date + timedelta(days=random_number_of_days)

                    seeder.add_entity(ForTest, 1, {
                        'name': lambda x: seeder.faker.first_name(),
                        'surname': lambda x: seeder.faker.last_name(),
                        'patronymic': lambda x: seeder.faker.first_name(),
                        'position': pos_random,
                        'date_of_receipt': lambda x: random_date,
                        'salary': lambda x: random.randint(400000, 1500000),
                        'head': ForTest.objects.get(pk=head_random)
                    })
                    x += 1

        inserted_pks = seeder.execute()


