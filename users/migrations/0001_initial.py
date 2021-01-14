# Generated by Django 3.0.8 on 2020-09-10 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Securities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('company', models.CharField(blank=True, default='', max_length=500)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_name', models.CharField(default='', max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('portfolio_author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('portfolio_symbols', models.ManyToManyField(to='Securities.Stock')),
            ],
            options={
                'verbose_name_plural': 'Portfolio',
            },
        ),
    ]