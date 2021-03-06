# Generated by Django 3.0.3 on 2020-06-25 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20200625_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='activity_period',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.AddField(
            model_name='activity_period',
            name='stime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.User'),
        ),
    ]
