import csv
from django.core.management.base import BaseCommand
from django.apps import apps
import os

class Command(BaseCommand):
    help = 'Load data from CSV files into models'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='Name of the Django app containing the models')

    def handle(self, *args, **options):
        app_name = options['app_name']
        success_models = []
        error_models = []

        # Obtén una lista de todos los modelos en la aplicación
        models = apps.get_app_config(app_name).get_models()

        for model in models:
            csv_file = f'{model.__name__}.csv'

            if os.path.exists(csv_file):
                with open(csv_file, 'r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        try:
                            obj, created = model.objects.get_or_create(
                                **row
                            )
                            if created:
                                success_models.append(model.__name__)
                                self.stdout.write(self.style.SUCCESS(f'Created {model.__name__}: {obj}'))
                            else:
                                self.stdout.write(self.style.WARNING(f'{model.__name__} already exists: {obj}'))
                        except Exception as e:
                            error_models.append(model.__name__)
                            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            else:
                self.stdout.write(self.style.WARNING(f'CSV file for {model.__name__} not found'))

        self.stdout.write(self.style.SUCCESS('Models processed successfully:'))
        self.stdout.write(', '.join(success_models))
        self.stdout.write(self.style.ERROR('Models with errors:'))
        self.stdout.write(', '.join(error_models))
