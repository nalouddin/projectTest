from django.urls import path
from .views import project, projects

urlpatterns = [
    path('projects/', projects, name='projects'),
    path('project/<uuid:id>', project, name='project')
]
