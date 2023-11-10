# Generated by Django 4.2.3 on 2023-10-16 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Содержание комментария')),
            ],
            options={
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/photos/', verbose_name='Изображение товара')),
            ],
            options={
                'verbose_name_plural': 'Фотографии продуктов',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True, verbose_name='Название состояния')),
            ],
            options={
                'verbose_name_plural': 'Статусы товаров',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Картошка, помидор и т.п.', max_length=300, verbose_name='Наименование товара')),
                ('price', models.FloatField(verbose_name='Цена товара')),
                ('quantity', models.FloatField(verbose_name='Количество товара')),
                ('comments', models.ManyToManyField(to='products.comment')),
                ('photos', models.ManyToManyField(to='products.photo')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.status', verbose_name='Состояние товара')),
            ],
            options={
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
