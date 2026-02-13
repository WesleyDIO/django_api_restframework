from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate(self, dados):
        if 'cpf' in dados:
            cpf = dados['cpf']
            if len(cpf) != 11:
                raise serializers.ValidationError({'cpf':'O CPF deve conter exatamente 11 caracteres.'})
        if 'nome' in dados:
            nome = dados['nome']
            if not nome.isalpha():
                raise serializers.ValidationError({'nome':'O nome deve conter somente letras.'})
        if 'celular' in dados:
            celular = dados['celular']
            if len(celular) != 13:
                raise serializers.ValidationError({'celular':'O número de celular deve conter exatamente 13 caracteres.'})
        return dados

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve conter exatamente 11 caracteres.")
        return cpf
    
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("O nome deve conter somente letras.")
        return nome
    
    def validate_celular(self, celular):
        if len(celular) != 13:
            raise serializers.ValidationError("O número de celular deve conter exatamente 13 caracteres.")
        return celular

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class listaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj): 
        return obj.get_periodo_display()
    
class listaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']
    