# Generated by Django 4.0.4 on 2022-06-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empolyee', '0002_empolyeeexperience_empolyeeeducation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company1desig',
        ),
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company1duration',
        ),
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company1name',
        ),
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company1salary',
        ),
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company2desig',
        ),
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company2duration',
        ),
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company2name',
        ),
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company2salary',
        ),
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company3desig',
        ),
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company3duration',
        ),
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company3name',
        ),
        migrations.RemoveField(
            model_name='empolyeeeducation',
            name='company3salary',
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company1desig',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company1duration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company1name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company1salary',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company2desig',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company2duration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company2name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company2salary',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company3desig',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company3duration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company3name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empolyeeexperience',
            name='company3salary',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
