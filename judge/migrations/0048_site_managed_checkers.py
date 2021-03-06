# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-10 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0047_site_managed_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemdata',
            name='checker',
            field=models.CharField(blank=True, choices=[(b'standard', 'Standard'), (b'floats', 'Floats'), (b'floatsabs', 'Floats (absolute)'), (b'floatsrel', 'Floats (relative)'), (b'rstripped', 'Non-trailing spaces'), (b'sorted', 'Unordered'), (b'identical', 'Byte identical')], max_length=10, verbose_name='checker'),
        ),
        migrations.AddField(
            model_name='problemdata',
            name='checker_args',
            field=models.TextField(blank=True, help_text='checker arguments as a JSON object', verbose_name='checker arguments'),
        ),
        migrations.AddField(
            model_name='problemtestcase',
            name='checker',
            field=models.CharField(blank=True, choices=[(b'standard', 'Standard'), (b'floats', 'Floats'), (b'floatsabs', 'Floats (absolute)'), (b'floatsrel', 'Floats (relative)'), (b'rstripped', 'Non-trailing spaces'), (b'sorted', 'Unordered'), (b'identical', 'Byte identical')], max_length=10, verbose_name='checker'),
        ),
        migrations.AddField(
            model_name='problemtestcase',
            name='checker_args',
            field=models.TextField(blank=True, help_text='checker arguments as a JSON object', verbose_name='checker arguments'),
        ),
    ]
