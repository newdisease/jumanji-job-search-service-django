# Generated by Django 3.2.7 on 2021-09-26 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0002_alter_vacancy_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('status', models.CharField(
                    choices=[
                        ('Не ищу работу', 'Not Looking For'),
                        ('Рассматриваю предложения', 'Check'),
                        ('Ищу работу', 'Looking For')
                    ],
                    default='Рассматриваю предложения',
                    max_length=24)),
                ('salary', models.IntegerField()),
                ('grade', models.CharField(
                    choices=[
                        ('Стажер', 'Trainee'),
                        ('Джуниор', 'Junior'),
                        ('Миддл', 'Middle'),
                        ('Синьор', 'Senior'),
                        ('Лид', 'Lead')],
                    default='Джуниор',
                    max_length=10)),
                ('education', models.TextField()),
                ('experience', models.TextField()),
                ('portfolio', models.URLField()),
                ('specialty', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='resume',
                    to='vacancies.specialty')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
