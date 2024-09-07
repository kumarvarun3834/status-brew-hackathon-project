from django.shortcuts import render
from django.http import HttpResponse
from .models import Resource
from .utils import read_menu_data  # Assuming you placed the function in a utils.py file
import os
# Create your views here.

# Path to your CSV file (adjust this based on your project structure)
# CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'menu_data.csv')

# step 0: getstarted page
def home_view(request):
    menu_data = read_menu_data()  # Read menu from CSV
    semesters = list(menu_data.keys())  # Get all available semesters
    return render(request, 'home.html')

# Step 1: Display all available semesters
def semester_view(request):
    menu_data = read_menu_data()  # Read menu from CSV
    semesters = list(menu_data.keys())  # Get all available semesters
    return render(request, 'semester.html', {'semesters': semesters})

# Step 2: Display subjects for the selected semester
def subject_view(request, semester):
    menu_data = read_menu_data()
    subjects = list(menu_data.get("/" + semester, {}).keys())  # Get subjects for the selected semester
    return render(request, 'subject.html', {'semester': semester, 'subjects': subjects})

# Step 3: Display years for the selected semester and subject
def year_view(request, semester, subject):
    menu_data = read_menu_data()
    years = menu_data.get("/" + semester, {}).get("/" + subject, [])  # Get years for the selected semester and subject
    return render(request, 'year.html', {'semester': semester, 'subject': subject, 'years': years})

# Step 4: Display resource types for the selected semester, subject, and year
def resource_type_view(request, semester, subject, year):
    resource_types = ['notes', 'books', 'pyq']  # Resource types can be static
    return render(request, 'resource_type.html', {'semester': semester, 'subject': subject, 'year': year, 'resource_types': resource_types})

# Step 5: Display files for the selected semester, subject, year, and resource type
def file_view(request, semester, subject, year, resource_type):
    resources = Resource.objects.filter(semester=semester, resource_type=resource_type, year=year)
    return render(request, 'files.html', {'resources': resources, 'semester': semester, 'subject': subject, 'year': year, 'resource_type': resource_type})
