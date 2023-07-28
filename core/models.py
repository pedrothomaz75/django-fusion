import uuid

from django.db import models
from stdimage.models import StdImageField

# Função que modifica o nome de arquivos para que não haja arquivos de mesmo nome para cópias de arquivos
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo ?', default=True)

    class Meta:
        abstract = True


# Class que contém os icones dos serviços sendo trazidos do backend
class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'engrenagem'),
        ('lni-stats-up', 'gráfico'),
        ('lni-user', 'usuário'),
        ('lni-layers', 'design'),
        ('lni-mobile', 'celular'),
        ('lni-rocket', 'foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
    def __str__(self):
        return self.servico


# Class de cargo dos funcionários
class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo



class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width':480, 'height':480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
    
    def __str__(self):
        return self.nome
    
    
class Precos(Base):
    ICONE_CHOICES = (
        ('lni-package', 'pacote'),
        ('lni-drop', 'gota'),
        ('lni-star', 'estrela'),
    )
    preco_plano = models.CharField('Preço', max_length=100)
    plano = models.CharField('Plano', max_length=20)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

    def __str__(self):
        return self.plano

class Recursos(Base):
    ICONE_CHOICES = (
        ('lni-rocket' , 'foguete'),
        ('lni-laptop-phone' , 'celular-notebook'),
        ('lni-cog' , 'engrenagem'),
        ('lni-leaf' , 'folha'),
        ('lni-layers' , 'camadas'),
    )
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=20,choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.nome
