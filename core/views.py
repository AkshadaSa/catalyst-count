from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import csv
from .models import Company

def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def upload_view(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        uploaded_file_url = fs.url(filename)

        # Process the uploaded CSV file
        with open(fs.path(filename), 'r', encoding='utf-8') as file:
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
                except Exception as e:
                    print(f'Error importing row {row}: {e}')
            
            if batch:
                Company.objects.bulk_create(batch)

        return HttpResponse(f'Successfully imported {row_count} rows from "{csv_file.name}"')
    
    return render(request, 'upload.html')

def query_builder_view(request):
    return render(request, 'query.html')

def users_view(request):
    return render(request, 'user.html')
