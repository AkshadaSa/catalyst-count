import csv
from django.core.management.base import BaseCommand
from core.models import Company

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_file']
        self.stdout.write(f'Starting import from {file_path}')
        
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                batch_size = 1000
                batch = []
                row_count = 0
                for row in reader:
                    try:
                        company = Company(
                            number=row.get('number'),
                            name=row.get('name'),
                            domain=row.get('domain'),
                            year_founded=row.get('year_founded'),
                            industry=row.get('industry'),
                            size_range=row.get('size_range'),
                            locality=row.get('locality'),
                            country=row.get('country'),
                            linkedin_url=row.get('linkedin_url'),
                            current_employee_estimate=row.get('current_employee_estimate'),
                            total_employee_estimate=row.get('total_employee_estimate')
                        )
                        batch.append(company)
                        row_count += 1
                        if len(batch) >= batch_size:
                            Company.objects.bulk_create(batch)
                            batch = []
                            self.stdout.write(f'Inserted {row_count} rows...')
                    except Exception as e:
                        self.stdout.write(f'Error importing row {row}: {e}')
                
                if batch:
                    Company.objects.bulk_create(batch)
                    self.stdout.write(f'Inserted {row_count} rows...')

                self.stdout.write(f'Successfully imported {row_count} rows from "{file_path}"')
        except FileNotFoundError:
            self.stdout.write(f'File not found: {file_path}')
        except Exception as e:
            self.stdout.write(f'An error occurred: {e}')
