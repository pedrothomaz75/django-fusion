# Generated by Django 4.2.3 on 2023-07-26 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='ativos',
            new_name='ativo',
        ),
        migrations.RenameField(
            model_name='cargo',
            old_name='modificados',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='ativos',
            new_name='ativo',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='modificados',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='servico',
            old_name='ativos',
            new_name='ativo',
        ),
        migrations.RenameField(
            model_name='servico',
            old_name='modificados',
            new_name='modificado',
        ),
    ]
