# Generated by Django 3.2 on 2022-12-07 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='имя')),
                ('card_number', models.IntegerField(verbose_name='номер карточки')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='наименование бдюда')),
                ('start_price', models.IntegerField(verbose_name='цена')),
            ],
            options={
                'verbose_name': 'хавчик',
                'verbose_name_plural': 'хавчикс',
                'db_table': 'Food',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='ингридиент')),
                ('extra_price', models.IntegerField(verbose_name='надбавка')),
            ],
            options={
                'verbose_name': 'ингридиент',
                'verbose_name_plural': 'ингриденты',
                'db_table': 'Ingredient',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='имя')),
                ('position', models.CharField(max_length=30, verbose_name='должность')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DadyaFood.user')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
                'db_table': 'Worker',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date_time', models.DateTimeField(auto_now_add=True, verbose_name='время заказа')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DadyaFood.client')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DadyaFood.food')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DadyaFood.ingredient')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DadyaFood.worker')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'заказы',
                'db_table': 'Order',
            },
        ),
        migrations.AddField(
            model_name='food',
            name='ingredient',
            field=models.ManyToManyField(related_name='mill', through='DadyaFood.Order', to='DadyaFood.Ingredient'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DadyaFood.user'),
        ),
    ]
