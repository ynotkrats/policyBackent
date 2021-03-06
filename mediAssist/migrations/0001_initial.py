# Generated by Django 4.0.4 on 2022-04-23 14:55

from django.db import migrations, models
import django.db.models.deletion
import mediAssist.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('customer_gender', models.CharField(max_length=1)),
                ('customer_marital_status', models.BooleanField()),
                ('customer_region', models.CharField(max_length=10)),
                ('customer_income_group', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_segment_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('vehicle_segment', models.CharField(max_length=1)),
                ('fuel', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('policy_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date_of_purchase', models.DateField()),
                ('bil', models.BooleanField()),
                ('premium', models.IntegerField(default=0, validators=[mediAssist.validators.validate_premium])),
                ('pip', models.BooleanField()),
                ('pdl', models.BooleanField()),
                ('collision', models.BooleanField()),
                ('comprehensive', models.BooleanField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediAssist.customer')),
                ('vehicle_segment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediAssist.vehicle')),
            ],
        ),
    ]
