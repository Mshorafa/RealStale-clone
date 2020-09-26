import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed

from Lsitings import models as lsitings_model
from Realtors import models as realtors_model



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
        Realtors = realtors_model.Realtor.objects.all()
        seeder.add_entity(lsitings_model.Listings, times, {
            'title' : lambda x :seeder.faker.sentence(nb_words=random.randint(3,10)),
            'address' : lambda x  : seeder.faker.address(),
            'city' : lambda x : seeder.faker.city(),
            'state' : lambda x : seeder.faker.country(),
            'zipcode' : lambda x : seeder.faker.postcode() ,
            'description' : lambda x :seeder.faker.sentence() ,
            'price' : lambda x : int(f'{random.randint(20,50)}000') ,
            'bedroom' : lambda x : random.randint(0,3),
            'bathroom' : lambda x : random.randint(0,3),
            'garage' : lambda x : random.randint(0,3),
            'sqft' : lambda x : random.randint(0,3),
            'lot_size' : lambda x : random.uniform(1, 5),
            'realtors' : lambda x :random.choice(Realtors),
        })
        created_reol = seeder.execute()
        clean_rel= flatten(list(created_reol.values()))
        for pk in clean_rel:
            lsitings = lsitings_model.Listings.objects.get(pk=pk)
            for i in range(0,8):
                if i == 0:
                    lsitings_model.Photo.objects.create(
                        name=seeder.faker.name(),
                        img=f'photos/home-{random.randint(1,6)}.jpg',
                        listing=lsitings,
                        main_photo=True,
                        )
                else:
                    lsitings_model.Photo.objects.create(
                        name=seeder.faker.name(),
                        img=f'photos/home-inside-{random.randint(1, 6)}.jpg',
                        listing=lsitings,
                        main_photo=False,
                    )

        self.stdout.write(self.style.SUCCESS(f'this code run for {times} Successfully '))
