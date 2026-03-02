from django.test import TestCase
from escola.models import Estudante,Curso,Matricula

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixtures(self):
        """Teste para verificar o carregamento da fixtures"""
        estudante = Estudante.objects.get(cpf='80564078395')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular, '26 99222-7754')
        self.assertEqual(curso.codigo, 'F01')