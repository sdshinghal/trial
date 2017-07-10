# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-03 09:01
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utm_source', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('utm_medium', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('utm_campaign', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('utm_content', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('utm_keyword', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('campaign_name', models.CharField(blank=True, max_length=255, null=True)),
                ('campaign_date', models.DateField(db_index=True)),
                ('unique_visits', models.IntegerField(blank=True, null=True)),
                ('visits', models.IntegerField(blank=True, null=True)),
                ('bounce_count', models.IntegerField(blank=True, null=True)),
                ('actions_count', models.IntegerField(blank=True, null=True)),
                ('total_spent', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('platform_source', models.CharField(default=1, max_length=255)),
                ('platform_ad_id', models.BigIntegerField(blank=True, null=True)),
                ('platform_campaign_id', models.BigIntegerField(blank=True, null=True)),
                ('platform_adset_id', models.BigIntegerField(blank=True, null=True)),
                ('platform_url', models.TextField(blank=True, max_length=200, null=True)),
                ('platform_campaign_status', models.TextField(blank=True, max_length=200, null=True)),
                ('platform_ad_status', models.TextField(blank=True, max_length=200, null=True)),
                ('ad_introduction_text', models.TextField(blank=True, max_length=400, null=True)),
                ('ad_headline_text', models.TextField(blank=True, max_length=400, null=True)),
                ('ad_line_text', models.TextField(blank=True, max_length=400, null=True)),
                ('image_url', models.URLField(blank=True, max_length=255, null=True)),
                ('cost_per_mile', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('cost_per_click', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('cost_per_action', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('cost_per_pixel', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('click_through_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('impressions', models.IntegerField(blank=True, null=True)),
                ('clicks', models.IntegerField(blank=True, null=True)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('shares', models.IntegerField(blank=True, null=True)),
                ('follows', models.IntegerField(blank=True, null=True)),
                ('comments', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'campaigns',
            },
        ),
        migrations.CreateModel(
            name='CampaignConversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_date', models.DateField(db_index=True)),
                ('utm_source', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('utm_medium', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('utm_campaign', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('utm_content', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('initiated', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('registered', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('documents_received', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('activated', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('invested', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'campaign_conversions',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2017, 7, 3, 9, 1, 41, 770279, tzinfo=utc))),
                ('created_at', models.DateField(default=datetime.datetime(2017, 7, 3, 9, 1, 41, 770365, tzinfo=utc))),
                ('updated_at', models.DateField(default=datetime.datetime(2017, 7, 3, 9, 1, 41, 770423, tzinfo=utc))),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(choices=[('outbrain', 'Outbrain'), ('taboola', 'Taboola'), ('adwords', 'AdWords'), ('timesinternet', 'Times Internet')], default='adwords', max_length=100)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='templating.File'),
        ),
    ]