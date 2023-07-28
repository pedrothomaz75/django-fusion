import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'
    

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


 
class ServicoTestCase(TestCase):
    # FUnção de configuração
    def setUp(self):
        self.servico = mommy.make('Servico')
    
    def teste_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)


class CargoTestCase(TestCase):
    # FUnção de configuração
    def setUp(self):
        self.cargo = mommy.make('Cargo')
    
    def teste_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):
    # FUnção de configuração
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')
    
    def teste_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)


class PrecosTestCase(TestCase):
    # FUnção de configuração
    def setUp(self):
        self.precos = mommy.make('Precos')
    
    def teste_str(self):
        self.assertEquals(str(self.precos), self.precos.plano)


class RecursosTestCase(TestCase):
    # FUnção de configuração
    def setUp(self):
        self.recursos = mommy.make('Recursos')
    
    def teste_str(self):
        self.assertEquals(str(self.recursos), self.recursos.nome)

