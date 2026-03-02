from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']


    def setUp(self):
        #self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.usuario = User.objects.get(username='wesley')
        self.url = reverse('Estudante-list')
        self.client.force_authenticate(user=self.usuario)
        #self.estudante_01 = Estudante.objects.create(
        #nome='Estudante Teste 01',
        #email = 'estudante01@teste.com',
        #cpf = '30672316005',
        #data_nascimento = '2000-01-01',
        #celular = '86 99999-9999'
        #)
        self.estudante_01 = Estudante.objects.get(pk=1)
        #self.estudante_02 = Estudante.objects.create(       
        #nome='Estudante Teste 02',
        #email = 'estudante02@teste.com',
        #cpf = '06964819010',
        #data_nascimento = '2000-01-01',
        #celular = '86 99999-9999'
        #)
        self.estudante_02 = Estudante.objects.get(pk=2)

    def test_requisicao_get_estudantes(self):
        """Teste para verificar a requisição GET de estudantes"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_requisicao_get_para_listar_um_estudante(self):
        """Teste de requisição GET para um estudante"""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(istance=dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados)

    def test_requisicao_post_para_criar_um_estudante(self):
        """Teste de requisição POST para criar um estudante"""
        dados = {
            'nome': 'Estudante Teste 03',
            'email': 'estudante03@teste.com',
            'cpf': '74262534065',
            'data_nascimento': '2000-01-01',
            'celular': '86 99999-9999'
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_estudante(self):
        """Teste de requisição DELETE para criar um estudante"""

        response = self.client.delete(f'{self.url}2/')#/estudantes/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_estudante(self):
        """Teste de requisição PUT para atualizar um estudante"""
        dados = {
            'nome': 'Estudante Teste 02 Atualizado',    
            'email': 'estudante02atualizado@teste.com',
            'cpf': '01472001052',
            'data_nascimento': '2000-01-01',
            'celular': '86 99999-9999'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)