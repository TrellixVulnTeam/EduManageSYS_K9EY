# Generated by Django 2.2.1 on 2019-05-03 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_selection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('couid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('course', models.ManyToManyField(to='course_selection.Course')),
                ('stuid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course_selection.User')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_selection.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ManyToManyField(to='course_selection.Subject'),
        ),
    ]
