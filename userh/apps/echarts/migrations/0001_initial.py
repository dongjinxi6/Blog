# Generated by Django 4.0.4 on 2022-05-21 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='echarts_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ec_name', models.CharField(max_length=40)),
            ],
        ),
    ]