# Generated by Django 2.2.12 on 2020-07-01 03:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borehole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bhole_date_of_drilling', models.DateField(null=True, verbose_name='bholeDateOfDrilling')),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.TextField(blank=True, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SealingMaterialTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SealingTypeTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WellStatusTypeTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SealingComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sealing_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groundwater.SealingMaterialTerm', verbose_name='sealingMaterial')),
                ('sealing_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groundwater.SealingTypeTerm', verbose_name='sealingType')),
            ],
        ),
        migrations.CreateModel(
            name='GWWell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gw_well_name', models.TextField(verbose_name='gwWellName')),
                ('gw_well_location', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='gwWellLocation')),
                ('gw_well_contribution_zone', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326, verbose_name='gwWellContributionZone')),
                ('gw_well_total_length', models.FloatField(blank=True, null=True, verbose_name='gwWellTotalLength')),
                ('gw_well_construction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groundwater.Borehole', verbose_name='gwWellConstruction')),
                ('gw_well_static_water_depth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groundwater.Quantity', verbose_name='gwWellStaticWaterDepth')),
                ('gw_well_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groundwater.WellStatusTypeTerm', verbose_name='gwWellStatus')),
            ],
        ),
        migrations.CreateModel(
            name='GWGeologyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phenomenon_time', models.DateTimeField(blank=True, null=True, verbose_name='phenomenonTime')),
                ('result_time', models.DateTimeField(blank=True, null=True, verbose_name='resultTime')),
                ('parameter', models.TextField(blank=True, null=True)),
                ('gw_level', models.FloatField(blank=True, null=True, verbose_name='gw_level')),
                ('reference', models.TextField(blank=True, null=True, verbose_name='reference')),
                ('end_depth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='endDepth', to='groundwater.Quantity', verbose_name='endDepth')),
                ('gw_well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groundwater.GWWell', verbose_name='gwWell')),
                ('start_depth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='startDepth', to='groundwater.Quantity', verbose_name='startDepth')),
            ],
        ),
        migrations.AddField(
            model_name='borehole',
            name='bhole_nominal_diameter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groundwater.Quantity', verbose_name='bholeNominalDiameter'),
        ),
    ]
