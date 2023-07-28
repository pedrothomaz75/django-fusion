from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Huey Freeman',
            'email': 'huey@gmail.com',
            'assunto': 'meu assunto',
            'mensagem': 'teste',
        }

        self.cliente = Client()
    
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)
    

    def test_form_invalid(self):
        dados = {
            'nome': 'Huey Freeman',
            'assunto': 'meu assunto',
        }

        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)