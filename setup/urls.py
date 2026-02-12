from django.contrib import admin
from django.urls import include, path
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'estudantes', EstudanteViewSet,basename='estudantes')
router.register(r'cursos', CursoViewSet, basename='cursos')
router.register(r'matriculas', MatriculaViewSet, basename='matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view(), name='lista-matriculas-estudante'),
]
