# Generated by Django 3.1.4 on 2021-01-01 21:09

from django.db import migrations, models
import prediction.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineShoppersIntentions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Administrative', models.IntegerField()),
                ('AdministrativeDuration', models.FloatField()),
                ('Informational', models.IntegerField()),
                ('InformationalDuration', models.FloatField()),
                ('ProductRelated', models.IntegerField()),
                ('ProductRelatedDuration', models.FloatField()),
                ('SpecialDay', models.FloatField()),
                ('Month', models.CharField(choices=[('Feb', 'February'), ('Mar', 'March'), ('May', 'May'), ('June', 'June'), ('Jul', 'July'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')], max_length=4)),
                ('OperatingSystems', models.IntegerField()),
                ('Browser', models.IntegerField()),
                ('Region', models.IntegerField()),
                ('VisitorType', models.CharField(choices=[('Returning_Visitor', 'Returning visitor'), ('New_Visitor', 'New visitor')], max_length=17)),
                ('Weekend', models.BooleanField()),
                ('Revenue', models.BooleanField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
