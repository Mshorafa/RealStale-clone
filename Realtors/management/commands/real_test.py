import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed

from Realtors import models



class Command(BaseCommand):
    def add_arguments(self, parser):
        """
        Entry point for subclassed commands to add custom arguments.
        """
        help = ' This code For test seeds code on DB'
        parser.add_argument('--times', type=int, default=1, help='how many time do you want to repeat this ')

    def handle(self, *args, **options):
        """
        The actual logic of the command. Subclasses must implement
        this method.
        """
        times = options.get('times')
        seeder = Seed.seeder()
        seeder.add_entity(models.Realtor, times, {
            'name' : lambda x : seeder.faker.name() ,
            'description' : lambda x : seeder.faker.paragraph() ,
            'phone' : lambda x : seeder.faker.phone_number(),
            'email' : lambda x :seeder.faker.email(),
            'avater' : lambda x : f'avater/{random.randint(0,6)}.jpg',
        })
        created_reol = seeder.execute()
        clean_rel= flatten(list(created_reol.values()))
        print(clean_rel)
        self.stdout.write(self.style.SUCCESS(f'this code run for {times} Successfully '))
