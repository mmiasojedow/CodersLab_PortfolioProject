# Generated by Django 2.2.10 on 2020-02-15 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'Fundacja'), (2, 'Organizacja pozarządowa'), (3, 'Zbiórka lokalna')], default=1)),
                ('categories', models.ManyToManyField(to='OddamWDobreRece.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=128)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=128)),
                ('zip_code', models.CharField(max_length=6)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pick_up_comment', models.TextField()),
                ('categories', models.ManyToManyField(to='OddamWDobreRece.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OddamWDobreRece.Institution')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
