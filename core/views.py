from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'login.html')

@login_required
def upload_data_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            # Process the uploaded file
            # Example: Save the file or handle its content
            handle_uploaded_file(uploaded_file)
            return redirect('success_page')  # Redirect to a success page or message
        else:
            return render(request, 'upload_data.html', {'error': 'No file uploaded.'})
    return render(request, 'upload_data.html')

def handle_uploaded_file(f):
    with open('some/file/path/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required
def query_builder_view(request):
    result = None
    if request.method == 'POST':
        query = request.POST.get('query')
        try:
            with connection.cursor() as cursor: # type: ignore
                cursor.execute(query)
                result = cursor.fetchall()
        except Exception as e:
            result = {'error': str(e)}
    
    return render(request, 'query_builder.html', {'result': result})

@login_required
def users_view(request):
    user_list = User.objects.all()
    paginator = Paginator(user_list, 10)  # type: ignore # Show 10 users per page.
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    return render(request, 'users.html', {'users': users})