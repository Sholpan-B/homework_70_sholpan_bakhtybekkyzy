# Generated by Django 4.1.7 on 2023-03-10 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_status_name_remove_task_status_alter_task_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('title', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('description', models.TextField(blank=True, max_length=2500, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AddField(
            model_name='task',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='webapp.project', verbose_name='Проект'),
        ),
    ]
