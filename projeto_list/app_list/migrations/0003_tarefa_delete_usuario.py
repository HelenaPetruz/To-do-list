# Generated by Django 5.1.3 on 2024-12-01 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_list', '0002_rename_usuarios_usuario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.TextField(max_length=100)),
                ('descricao', models.TextField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
