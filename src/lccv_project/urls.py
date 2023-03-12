"""lccv_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from lccv_app.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet)
router.register('professores', ProfessorViewSet)
router.register('disciplina', DisciplinaViewSet)
router.register('frequencia', FrequenciaViewSet)
router.register('plano_aula', PlanoAulaViewSet)
router.register('atividade', AtividadeViewSet)
router.register('add_disciplina', DisciplinaAlunoViewSet)
router.register('add_frequencia', FrequenciaAlunoViewSet)
router.register('add_atividade', AtividadeAlunoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
