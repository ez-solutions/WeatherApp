from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('sky_description', models.CharField(blank=True, max_length=255, null=True)),
                ('precipitation_description', models.CharField(blank=True, max_length=255, null=True)),
                ('precipitation_probability', models.IntegerField(blank=True, null=True)),
                ('temperature_description', models.CharField(blank=True, max_length=255, null=True)),
                ('temperature_high', models.IntegerField(blank=True, null=True)),
                ('temperature_low', models.IntegerField(blank=True, null=True)),
                ('uv_description', models.CharField(blank=True, max_length=255, null=True)),
                ('air_description', models.CharField(blank=True, max_length=255, null=True)),
                ('wind_speed', models.IntegerField(blank=True, null=True)),
                ('wind_direction_description', models.CharField(blank=True, max_length=255, null=True)),
                ('dew_point', models.CharField(blank=True, max_length=255, null=True)),
                ('humidity', models.CharField(blank=True, max_length=255, null=True)),
                ('comfort', models.CharField(blank=True, max_length=255, null=True)),
                ('visibility', models.CharField(blank=True, max_length=255, null=True)),
                ('rainfall', models.CharField(blank=True, max_length=255, null=True)),
                ('snowfall', models.CharField(blank=True, max_length=255, null=True)),
                ('icon_name', models.CharField(blank=True, max_length=255, null=True)),
                ('beaufort_description', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forecasts', to='app.City')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.City')),
            ],
        ),
    ]
