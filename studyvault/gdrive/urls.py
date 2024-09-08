from django.urls import path

from . import views

# exist for internal app config
# and linking internally

# this urlpatterns name is also fixed
# urlpatterns = [
#     # step 0: main start page
#     path('', views.home_view, name='home'),

#     # Step 1: Display all semesters at /home/
#     path('home/', views.semester_view, name='semester_view'),
    
#     # Step 2: Display subjects for the selected semester
#     path('home/<str:semester>/', views.subject_view, name='subject_view'),
    
#     # Step 3: Display years for the selected semester and subject
#     path('home/<str:semester>/<str:subject>/', views.year_view, name='year_view'),
    
#     # Step 4: Display resources for the selected semester, subject, and year
#     path('home/<str:semester>/<str:subject>/<str:year>/', views.resource_type_view, name='resource_type_view'),
    
#     # Step 5: Display files for the selected semester, subject, year, and resource type
#     path('home/<str:semester>/<str:subject>/<str:year>/<str:resource_type>/', views.file_view, name='file_view'),
# ]


urlpatterns = [
    # Main home/start page
    path('', views.home_view, name='home'),

    # Step-by-step URL structure
    # path('', views.semester_view, name='semester_view'),
    path('<str:semester>/', views.subject_view, name='subject_view'),
    path('<str:semester>/<str:subject>/', views.year_view, name='year_view'),
    path('<str:semester>/<str:subject>/<str:year>/', views.resource_type_view, name='resource_type_view'),
    path('<str:semester>/<str:subject>/<str:year>/<str:resource_type>/', views.file_view, name='file_view'),
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
#     path('semester/', views.semester_view, name='semester'),
#     path('semester/<str:semester>/', views.subject_view, name='subject'),
#     path('semester/<str:semester>/subject/<str:subject>/', views.year_view, name='year'),
#     path('semester/<str:semester>/subject/<str:subject>/year/<str:year>/', views.resource_type_view, name='resource_type'),
#     path('semester/<str:semester>/subject/<str:subject>/year/<str:year>/resource/<str:resource_type>/', views.file_view, name='file'),
# ]


